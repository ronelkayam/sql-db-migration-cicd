-- יצירת טבלה נוספת עם קשר (Foreign Key) לטבלת המשתמשים
CREATE TABLE orders (
    order_id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT FOREIGN KEY REFERENCES users(id),
    amount DECIMAL(10, 2),
    order_date DATETIME DEFAULT GETDATE()
);