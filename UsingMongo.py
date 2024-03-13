import pymongo
password = 'backspac3'
client = pymongo.MongoClient("mongodb+srv://theandriod:{password}@theandriod.i5wb5np.mongodb.net/?retryWrites=true&w=majority&appName=theandriod")

d = client['school_db']

collection = d['school_collection']


# inserts documents into school_collection
data = {"name": 'emmanuelss', "Age": 30, "School_name": 'Bizmarrow'}

insert_data = collection.insert_one(data)

print(f"Inserted document id: {insert_data.inserted_id}")