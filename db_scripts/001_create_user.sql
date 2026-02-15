-- יצירת טבלת משתמשים בסיסית
CREATE TABLE users (
    id INT IDENTITY(1,1) PRIMARY KEY,
    username NVARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT GETDATE()
);