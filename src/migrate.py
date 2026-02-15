import pyodbc
import os

# פרטי התחברות - בשלב ה-CI זה יעבור למשתני סביבה (Secrets)
DB_CONFIG = {
    'server': 'localhost',
    'database': 'Manual Scripting',
    'user': 'sa',
    'password': 'Ron26190!'
}


def run_migrations():
    conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={DB_CONFIG['server']};DATABASE={DB_CONFIG['database']};UID={DB_CONFIG['user']};PWD={DB_CONFIG['password']}"

    try:
        conn = pyodbc.connect(conn_str)
        conn.autocommit = True
        cursor = conn.cursor()

        # זה הולך צעד אחד אחורה לתיקיית האב ואז נכנס ל-db_scripts
        script_path = os.path.join(os.path.dirname(__file__), '..', 'db_scripts')
        scripts = sorted([f for f in os.listdir(script_path) if f.endswith('.sql')])

        for script in scripts:
            print(f"Executing {script}...")
            # הוספנו encoding='utf-8' כדי לתמוך בכל סוגי התווים
            with open(os.path.join(script_path, script), 'r', encoding='utf-8') as f:
                cursor.execute(f.read())

        print("✅ Migration completed successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()


if __name__ == "__main__":
    run_migrations()