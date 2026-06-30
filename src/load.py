import sqlite3
from logger import logger
from config import DATABASE_NAME, SCHEMA_FILE


def load_data(df):
    """
    Load transformed data into a dimensional warehouse.
    """

    logger.info("Loading data into warehouse...")

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Create warehouse schema
    with open(SCHEMA_FILE, "r") as file:
        cursor.executescript(file.read())

    # ==========================
    # CUSTOMERS DIMENSION
    # ==========================
    customers = (
        df[["customer_name", "email"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    customers["customer_id"] = customers.index + 1

    customers = customers[
        ["customer_id", "customer_name", "email"]
    ]

    customers.to_sql(
        "dim_customers",
        conn,
        if_exists="append",
        index=False
    )

    # ==========================
    # PRODUCTS DIMENSION
    # ==========================
    products = (
        df[["product"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    products.columns = ["product_name"]

    products["product_id"] = products.index + 1

    products = products[
        ["product_id", "product_name"]
    ]

    products.to_sql(
        "dim_products",
        conn,
        if_exists="append",
        index=False
    )

    # ==========================
    # REGIONS DIMENSION
    # ==========================
    regions = (
        df[["region"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    regions.columns = ["region_name"]

    regions["region_id"] = regions.index + 1

    regions = regions[
        ["region_id", "region_name"]
    ]

    regions.to_sql(
        "dim_regions",
        conn,
        if_exists="append",
        index=False
    )

    # ==========================
    # FACT SALES
    # ==========================
    fact_sales = df.merge(
        customers,
        on=["customer_name", "email"]
    )

    fact_sales = fact_sales.merge(
        products,
        left_on="product",
        right_on="product_name"
    )

    fact_sales = fact_sales.merge(
        regions,
        left_on="region",
        right_on="region_name"
    )

    fact_sales = fact_sales[
        [
            "sale_id",
            "customer_id",
            "product_id",
            "region_id",
            "quantity",
            "unit_price",
            "total_sales",
            "sale_date"
        ]
    ]

    fact_sales.to_sql(
        "fact_sales",
        conn,
        if_exists="append",
        index=False
    )

    logger.info("Dimension tables loaded successfully.")
    logger.info("Fact table loaded successfully.")

    conn.commit()
    conn.close()

    logger.info("Warehouse loaded successfully.")