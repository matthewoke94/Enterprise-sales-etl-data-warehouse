# Enterprise Sales ETL Data Warehouse

## Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built using Python. The pipeline extracts sales data from CSV files, validates and transforms the data, then loads it into a dimensional data warehouse following a star schema design.

---

## Project Architecture

CSV Data
↓
Extract
↓
Validate
↓
Transform
↓
Load
↓
SQLite Data Warehouse

---

## Features

- Extracts sales data from CSV files
- Validates data quality
- Cleans duplicate and missing records
- Calculates total sales
- Builds a dimensional warehouse
- Creates Customer, Product and Region dimensions
- Loads a Fact Sales table
- Modular ETL architecture
- Logging throughout the pipeline

---

## Technologies Used

- Python
- Pandas
- SQLite
- SQLAlchemy
- Faker

---

## Project Structure

```
Enterprise-sales-etl-data-warehouse/
│
├── data/
│   └── raw/
│
├── sql/
│   └── warehouse_schema.sql
│
├── src/
│   ├── config.py
│   ├── database.py
│   ├── extract.py
│   ├── validate.py
│   ├── transform.py
│   ├── load.py
│   ├── logger.py
│   ├── utils.py
│   └── main.py
│
├── generate_data.py
├── requirements.txt
└── README.md
```

---

## Data Warehouse Schema

### Dimension Tables

- dim_customers
- dim_products
- dim_regions

### Fact Table

- fact_sales

---

## How to Run

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Generate sample data

```bash
python generate_data.py
```

Run the ETL pipeline

```bash
python src/main.py
```

---

## Sample Pipeline Output

```
5100 records extracted

5100 records validated

4921 records transformed

4921 records loaded

ETL Pipeline completed successfully.
```

---

## Future Improvements

- PostgreSQL integration
- Docker support
- Airflow orchestration
- Automated testing
- Power BI dashboard
- Cloud deployment

---

## Author

Matthew James

Data Engineer