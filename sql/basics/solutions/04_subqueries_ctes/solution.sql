-- Lesson 04 Solutions: subqueries and CTEs

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
SELECT id, name
FROM customers
WHERE id IN (
    SELECT customer_id
    FROM orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 2
)
ORDER BY id;

-- Task 2 solution
SELECT
    p.id,
    p.name,
    (SELECT COUNT(*) FROM order_items oi WHERE oi.product_id = p.id) AS order_line_count
FROM products p
ORDER BY p.id;

-- Task 3 solution
SELECT order_totals.order_id, order_totals.order_total
FROM (
    SELECT o.id AS order_id, SUM(oi.quantity * oi.unit_price) AS order_total
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.id
    GROUP BY o.id
) AS order_totals
WHERE order_totals.order_total > 500
ORDER BY order_totals.order_total DESC;

-- Task 4 solution
WITH customer_totals AS (
    SELECT
        o.customer_id,
        SUM(oi.quantity * oi.unit_price) AS total_spend
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.id
    WHERE o.status <> 'cancelled'
    GROUP BY o.customer_id
)
SELECT c.name, ct.total_spend
FROM customer_totals ct
JOIN customers c ON c.id = ct.customer_id
ORDER BY ct.total_spend DESC
LIMIT 2;
-- Expected leaders: Alice Johnson, Carla Gomez
