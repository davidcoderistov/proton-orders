#!/usr/bin/env python
import os

from flask import Flask
from pymongo import MongoClient
from pandas import read_csv
from datetime import datetime
from pymongo.errors import ConnectionFailure

app = Flask(__name__)

client = MongoClient('mongo:27017')
db = client['proton_db']
proton_sales = db['proton_sales']


def seed_db():
    try:
        if 'proton_db' not in client.list_database_names():
            df = read_csv('homework_order_lines.csv', index_col=0)
            sales = df.to_dict(orient='records')
            sales = [{**item, 'Date': datetime.strptime(item['Date'], '%Y-%m-%d')} for item in sales]
            proton_sales.insert_many(sales)
            print("Database seeded successfully.")
    except ConnectionFailure as e:
        print(f"Failed to connect to MongoDB: {e}")
    except Exception as e:
        print(f"An error occurred during database seeding: {e}")


if __name__ == "__main__":
    seed_db()
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
