import re
import os
import json
import boto3
import datetime
import uuid
from datetime import datetime
import json
from faker import Faker
import random
import faker

def get_referrer():
 
    x = random.randint(1, 5)
    x = x * 50
    y = x + 30
    data = {}
    data["user_id"] = random.randint(x, y)
    data["device_id"] = random.choice(
        ["mobile", "computer", "tablet", "mobile", "computer"]
    )
    data["client_event"] = random.choice(
        [
            "beer_vitrine_nav",
            "beer_checkout",
            "beer_product_detail",
            "beer_products",
            "beer_selection",
            "beer_cart",
        ]
    )
    now = datetime.now()
    str_now = now.isoformat()
    data["client_timestamp"] = str_now
    return data


for i in range(1, 120):
    data = get_referrer()
    print(data)