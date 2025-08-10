-- Create database
CREATE DATABASE ecommerce;
USE ecommerce;

-- Customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    country VARCHAR(50)
);

INSERT INTO customers VALUES
(1, 'Ayushi', 'Rana', 'India'),
(2, 'Rohit', 'Sharma', 'India'),
(3, 'Emily', 'Clark', 'USA'),
(4, 'John', 'Smith', 'UK');

-- Orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO orders VALUES
(101, 1, '2025-08-01', 1500.50),
(102, 1, '2025-08-05', 2000.00),
(103, 2, '2025-08-03', 3000.75),
(104, 3, '2025-08-07', 500.00);

-- Products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    price DECIMAL(10,2)
);

INSERT INTO products VALUES
(201, 'Laptop', 70000.00),
(202, 'Mobile', 20000.00),
(203, 'Headphones', 2500.00);

-- Order Details table
CREATE TABLE order_details (
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO order_details VALUES
(101, 201, 1),
(101, 203, 2),
(102, 202, 1),
(103, 201, 1),
(104, 203, 3);
-- 1. See all customers
SELECT * FROM customers;

-- 2. Orders from India
SELECT * FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
WHERE country = 'India';

-- 3. Total amount per customer
SELECT c.first_name, c.last_name, SUM(o.total_amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id;

-- 4. Average order value
SELECT AVG(total_amount) AS average_order
FROM orders;

-- 5. Orders with product details
SELECT o.order_id, c.first_name, p.product_name, od.quantity, p.price
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_details od ON o.order_id = od.order_id
JOIN products p ON od.product_id = p.product_id;
