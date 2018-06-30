from pymongo import MongoClient
import pprint
import datetime

client = MongoClient('localhost', 27017)

db = client.web335

user = {
    "first_name": "Kevin",
    "last_name": "James",
    "email": "kjames@mail.com",
    "employee_id": "1234108",
    "date_created": datetime.datetime.utcnow()
}



pprint.pprint(db.users.find_one({"employee_id": "1234108"}))