# Illustrates the basics of using PyMongo
from pymongo import MongoClient
import pprint

# Pretty Print Config
pp = pprint.PrettyPrinter(indent=4)

# Connect to the default, local MongoDB server
client = MongoClient()

# Connect to the Slack Database
db = client["slack"]
msg_collection = db["messages"]

# Create a message dict
message = {"channel": "dev", "author": "cerami", "text": "Hello, world!"}

# Insert One Record and Show the Inserted ID
# To insert multiple records at once, use insert_many()
result = msg_collection.insert_one(message)
print("Inserted:  %s" % result.inserted_id)

# Now get all documents back
for doc in msg_collection.find():
    pp.pprint(doc)

# Or get all documents in one channel
for doc in msg_collection.find({"channel": "dev"}):
    pp.pprint(doc)

# Or get all documents by specific author
for doc in msg_collection.find({"author": "cerami"}):
    pp.pprint(doc)

# Close connection
client.close()
