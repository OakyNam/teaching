-- Lesson 05 Solutions: data modeling and normalization

-- A denormalized staging table to show why normalized tables are useful.
DROP TABLE IF EXISTS raw_order_lines CASCADE;
DROP TABLE IF EXISTS order_items CASCADE;
DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS products CASCADE;
DROP TABLE IF EXISTS customers CASCADE;

CREATE TABLE raw_order_lines (
    order_id INT,
    order_date DATE,
    order_status TEXT,
    customer_name TEXT,
    customer_email TEXT,
    customer_country CHAR(2),
    product_sku TEXT,
    product_name TEXT,
    product_category TEXT,
    unit_price NUMERIC(10, 2),
    quantity INT
);

INSERT INTO raw_order_lines VALUES
    (1001, DATE '2024-04-01', 'paid', 'Alice Johnson', 'alice@example.com', 'US', 'SKU-LAP-15', 'Laptop Pro 15', 'Electronics', 1299.00, 1),
    (1001, DATE '2024-04-01', 'paid', 'Alice Johnson', 'alice@example.com', 'US', 'SKU-MOU-WL', 'Wireless Mouse', 'Accessories', 25.50, 2),
    (1002, DATE '2024-04-03', 'shipped', 'Bob Smith', 'bob@example.com', 'EG', 'SKU-KEY-MECH', 'Mechanical Keyboard', 'Accessories', 79.00, 1),
    (1002, DATE '2024-04-03', 'shipped', 'Bob Smith', 'bob@example.com', 'EG', 'SKU-NBK-SQL', 'SQL Practice Notebook', 'Books', 18.00, 3),
    (1003, DATE '2024-04-05', 'delivered', 'Alice Johnson', 'alice@example.com', 'US', 'SKU-DSK-OAK', 'Standing Desk', 'Furniture', 450.00, 1),
    (1004, DATE '2024-04-07', 'paid', 'Carla Gomez', 'carla@example.com', 'BR', 'SKU-MON-27', '27-inch Monitor', 'Electronics', 310.00, 2);

-- Task 1 solution
CREATE TABLE customers (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    country CHAR(2) NOT NULL
);

-- Task 2 solution
CREATE TABLE products (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    sku TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    current_price NUMERIC(10, 2) NOT NULL CHECK (current_price >= 0)
);

-- Task 3 solution
CREATE TABLE orders (
    id INT PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES customers(id),
    order_date DATE NOT NULL,
    status TEXT NOT NULL
);

CREATE TABLE order_items (
    order_id INT NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    product_id INT NOT NULL REFERENCES products(id),
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC(10, 2) NOT NULL CHECK (unit_price >= 0),
    PRIMARY KEY (order_id, product_id)
);

-- Task 4 solution
INSERT INTO customers (name, email, country)
SELECT DISTINCT customer_name, customer_email, customer_country
FROM raw_order_lines
ORDER BY customer_email;

INSERT INTO products (sku, name, category, current_price)
SELECT DISTINCT product_sku, product_name, product_category, unit_price
FROM raw_order_lines
ORDER BY product_sku;

INSERT INTO orders (id, customer_id, order_date, status)
SELECT DISTINCT rol.order_id, c.id, rol.order_date, rol.order_status
FROM raw_order_lines rol
JOIN customers c ON c.email = rol.customer_email
ORDER BY rol.order_id;

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
SELECT rol.order_id, p.id, rol.quantity, rol.unit_price
FROM raw_order_lines rol
JOIN products p ON p.sku = rol.product_sku
ORDER BY rol.order_id, p.id;

-- Task 5 solution
SELECT
    (SELECT COUNT(*) FROM raw_order_lines WHERE customer_email = 'alice@example.com') AS raw_rows_for_alice,
    (SELECT COUNT(*) FROM customers WHERE email = 'alice@example.com') AS normalized_rows_for_alice;
-- Expected result: raw_rows_for_alice > 1, normalized_rows_for_alice = 1
