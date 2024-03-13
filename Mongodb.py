
import pymongo

password = 5

client = pymongo.MongoClient(f"mongodb+srv://stringsafrika:{password}@cluster0.xukeyq5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

database = client['product_database']

collection_one = database['product_collection']


# insert data into collection_one
data = {'brandName': 'Iphone', "Model": 'Iphone 15', "Color": 'black', "price":150000000}
# insert_data = collection_one.insert_one(data)
# print(f'inserted document id: {insert_data.inserted_id}')


# to insert multiple items into collection_one

multiple_documents = [
    {"name": "Alice", "age": 30, "city": "San Francisco"},
    {"name": "Bob", "age": 22, "city": "Los Angeles"},
    {"name": "Charlie", "age": 28, "city": "Chicago"}
]

result = collection_one.insert_many(multiple_documents)

print(f"insert multiple documents into collection id: {result.inserted_ids}")

selected_documents = collection_one.find({"age": {"$gt":25}})

for doc in selected_documents:
    print(doc)


# Define a query criteria (equivalent to WHERE clause)
query_criteria = {"name": "emmanuel"}

# Find documents in the collection that satisfy the query criteria
result = collection_one.find(query_criteria)

# Print each matching document
for document in result:
    print(document)

# sorting in mongodb or pymongo 
result = collection_one.find().sort("name", pymongo.DESCENDING)
for document in result:
    print(document)

# Find all documents in the 'students' collection, sorted first by 'age' in ascending order and then by 'name' in descending order
result = collection_one.find().sort([("age", pymongo.ASCENDING), ("name", pymongo.DESCENDING)])

# Print each document in the result set
for document in result:
    print(document)

# Delete/ Drop
    
# Delete a document with a specific condition (e.g., delete the student with name 'John')
delete_result = collection_one.delete_one({"name": "John"})

# Delete multiple documents based on a condition (e.g., delete all students with age greater than 25)
delete_result = collection_one.delete_many({"age": {"$gt": 25}})


# Drop the entire 'students' collection
# collection_one.drop()


update_result = collection_one.update_one(
    {"name": "John"},
    {"$set": {"age": 30}}
)

# Update multiple documents based on a condition (e.g., update the age for all students with age less than 25)
update_result = collection_one.update_many(
    {"age": {"$lt": 25}},
    {"$set": {"age": 25}}
)


result = collection_one.find().limit(5)

for i in result:
    print('this is the limit',i)




