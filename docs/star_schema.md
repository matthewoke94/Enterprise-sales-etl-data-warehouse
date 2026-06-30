# Enterprise Sales Data Warehouse Star Schema

```text
                     +----------------------+
                     |   dim_customers      |
                     +----------------------+
                     | customer_id (PK)     |
                     | customer_name        |
                     | email                |
                     +----------+-----------+
                                |
                                |
                                |
+----------------------+         |         +----------------------+
|   dim_products       |         |         |    dim_regions       |
+----------------------+         |         +----------------------+
| product_id (PK)      |         |         | region_id (PK)       |
| product_name         |         |         | region_name          |
+----------+-----------+         |         +----------+-----------+
           \                     |                    /
            \                    |                   /
             \                   |                  /
              \                  |                 /
               +-----------------v----------------+
               |          fact_sales              |
               +----------------------------------+
               | sale_id                          |
               | customer_id (FK)                |
               | product_id (FK)                 |
               | region_id (FK)                  |
               | quantity                        |
               | unit_price                      |
               | total_sales                     |
               | sale_date                       |
               +----------------------------------+
```