-- Lesson 05 Exercises: data modeling and normalization

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

-- Task 1: Create a customers table with a primary key, NOT NULL columns, and a UNIQUE email.
-- YOUR QUERY HERE

-- Task 2: Create a products table that stores each SKU once.
-- Include a positive-price CHECK constraint.
-- YOUR QUERY HERE

-- Task 3: Create orders and order_items tables with primary keys and foreign keys.
-- YOUR QUERY HERE

-- Task 4: Insert distinct customers from raw_order_lines into your normalized customers table.
-- YOUR QUERY HERE

-- Task 5: Write a validation query that proves Alice Johnson only appears once in customers
-- even though she appears on multiple raw_order_lines rows.
-- YOUR QUERY HERE
