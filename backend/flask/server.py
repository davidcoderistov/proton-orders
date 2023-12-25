#!/usr/bin/env python
import os

from flask import Flask
from pymongo import MongoClient
from pandas import read_csv
from datetime import datetime
from pymongo.errors import ConnectionFailure
from mongo_utils import encode_and_decode
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = MongoClient('mongo:27017')
db = client['proton_db']
proton_orders = db['proton_orders']


def seed_db():
    try:
        if 'proton_db' not in client.list_database_names():
            df = read_csv('homework_order_lines.csv', index_col=0)
            orders = df.to_dict(orient='records')
            orders = [
                {
                    key.lower().replace(' ', '_'): datetime.strptime(value, '%Y-%m-%d') if key == 'Date' else value
                    for key, value in sale.items()
                }
                for sale in orders
            ]
            proton_orders.insert_many(orders)
            print("Database seeded successfully.")
    except ConnectionFailure as e:
        print(f"Failed to connect to MongoDB: {e}")
    except Exception as e:
        print(f"An error occurred during database seeding: {e}")


@app.route('/api/orders')
def get_orders():
    orders = proton_orders.find().sort('Date', -1)
    return encode_and_decode(list(orders))


if __name__ == "__main__":
    seed_db()
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
