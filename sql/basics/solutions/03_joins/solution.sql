-- Lesson 03 Solutions: JOINs

-- Shared e-commerce dataset used throughout the SQL basics lessons.
DROP TABLE IF EXISTS order_items CASCADE;
DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS products CASCADE;
DROP TABLE IF EXISTS customers CASCADE;

CREATE TABLE customers (
    id INT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    country CHAR(2) NOT NULL,
    signup_date DATE NOT NULL,
    referred_by_customer_id INT REFERENCES customers(id)
);

CREATE TABLE products (
    id INT PRIMARY KEY,
    sku TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price NUMERIC(10, 2) NOT NULL CHECK (price >= 0)
);

CREATE TABLE orders (
    id INT PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES customers(id),
    order_date DATE NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('pending', 'paid', 'shipped', 'delivered', 'cancelled')),
    shipping_country CHAR(2) NOT NULL
);

CREATE TABLE order_items (
    order_id INT NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    product_id INT NOT NULL REFERENCES products(id),
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC(10, 2) NOT NULL CHECK (unit_price >= 0),
    PRIMARY KEY (order_id, product_id)
);

INSERT INTO customers (id, name, email, country, signup_date, referred_by_customer_id) VALUES
    (1, 'Alice Johnson', 'alice@example.com', 'US', DATE '2024-01-10', NULL),
    (2, 'Bob Smith', 'bob@example.com', 'EG', DATE '2024-02-05', 1),
    (3, 'Carla Gomez', 'carla@example.com', 'BR', DATE '2024-02-20', 1),
    (4, 'Daniel Lee', 'daniel@example.com', 'US', DATE '2024-03-02', 2),
    (5, 'Fatma Hassan', 'fatma@example.com', 'EG', DATE '2024-03-15', 2);

INSERT INTO products (id, sku, name, category, price) VALUES
    (1, 'SKU-LAP-15', 'Laptop Pro 15', 'Electronics', 1299.00),
    (2, 'SKU-MOU-WL', 'Wireless Mouse', 'Accessories', 25.50),
    (3, 'SKU-KEY-MECH', 'Mechanical Keyboard', 'Accessories', 79.00),
    (4, 'SKU-DSK-OAK', 'Standing Desk', 'Furniture', 450.00),
    (5, 'SKU-MON-27', '27-inch Monitor', 'Electronics', 310.00),
    (6, 'SKU-NBK-SQL', 'SQL Practice Notebook', 'Books', 18.00),
    (7, 'SKU-CHR-ERG', 'Ergonomic Chair', 'Furniture', 220.00);

INSERT INTO orders (id, customer_id, order_date, status, shipping_country) VALUES
    (1001, 1, DATE '2024-04-01', 'paid', 'US'),
    (1002, 2, DATE '2024-04-03', 'shipped', 'EG'),
    (1003, 1, DATE '2024-04-05', 'delivered', 'US'),
    (1004, 3, DATE '2024-04-07', 'paid', 'BR'),
    (1005, 4, DATE '2024-04-10', 'cancelled', 'US'),
    (1006, 5, DATE '2024-04-11', 'shipped', 'EG');

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
    (1001, 1, 1, 1299.00),
    (1001, 2, 2, 25.50),
    (1002, 3, 1, 79.00),
    (1002, 6, 3, 18.00),
    (1003, 4, 1, 450.00),
    (1003, 2, 1, 25.50),
    (1003, 6, 2, 18.00),
    (1004, 5, 2, 310.00),
    (1004, 2, 1, 25.50),
    (1005, 1, 1, 1299.00),
    (1006, 3, 2, 79.00),
    (1006, 5, 1, 310.00);

-- Task 1 solution
SELECT o.id AS order_id, c.name AS customer_name, o.shipping_country
FROM orders o
INNER JOIN customers c ON c.id = o.customer_id
ORDER BY o.id;

-- Task 2 solution
SELECT c.name, COUNT(o.id) AS order_count
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
GROUP BY c.id, c.name
ORDER BY order_count DESC, c.name ASC;

-- Task 3 solution
SELECT p.sku, p.name, COALESCE(SUM(oi.quantity), 0) AS total_quantity
FROM order_items oi
RIGHT JOIN products p ON p.id = oi.product_id
GROUP BY p.id, p.sku, p.name
ORDER BY total_quantity DESC, p.name ASC;
-- Expected unsold product: Ergonomic Chair with 0 quantity

-- Task 4 solution
SELECT c.name AS customer_name, ref.name AS referred_by
FROM customers c
LEFT JOIN customers ref ON ref.id = c.referred_by_customer_id
ORDER BY c.id;
