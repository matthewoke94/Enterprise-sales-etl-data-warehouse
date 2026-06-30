from faker import Faker
import pandas as pd
import random

fake = Faker()

rows = []

products = [
    "Laptop",
    "Monitor",
    "Keyboard",
    "Mouse",
    "Printer",
    "Tablet",
    "Router",
    "Phone"
]

regions = [
    "Lagos",
    "Abuja",
    "Port Harcourt",
    "Kano",
    "Ibadan"
]

for i in range(5000):
    rows.append({
        "sale_id": i + 1,
        "customer_name": fake.name(),
        "email": fake.email(),
        "product": random.choice(products),
        "region": random.choice(regions),
        "quantity": random.randint(1, 10),
        "unit_price": random.randint(100, 5000),
        "sale_date": fake.date_between(start_date="-2y", end_date="today")
    })

df = pd.DataFrame(rows)

# Add duplicate records
df = pd.concat([df, df.sample(100)], ignore_index=True)

# Add missing emails
df.loc[df.sample(80).index, "email"] = None

# Save dataset
df.to_csv("data/raw/sales_data.csv", index=False)

print("Sales dataset generated successfully!")