DROP TABLE IF EXISTS dim_customers;
DROP TABLE IF EXISTS dim_products;
DROP TABLE IF EXISTS dim_regions;
DROP TABLE IF EXISTS fact_sales;

CREATE TABLE dim_customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    email TEXT
);

CREATE TABLE dim_products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT
);

CREATE TABLE dim_regions (
    region_id INTEGER PRIMARY KEY,
    region_name TEXT
);

CREATE TABLE fact_sales (
    sale_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    region_id INTEGER,
    quantity INTEGER,
    unit_price REAL,
    total_sales REAL,
    sale_date DATE
);