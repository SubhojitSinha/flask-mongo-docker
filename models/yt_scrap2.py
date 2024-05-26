from pymongo import MongoClient

# db_qry_str = f"mongodb://{db_user}:{db_password}@{db_host}"
# client = MongoClient(db_qry_str)
# connect_db = client[environ.get('DB_NAME_PROD')]

client = MongoClient("mongodb://root:12345@test_mongodb:27017/")
connect_db = client["test_db"]
try:
    db = connect_db
    collection = db['crm_platform_error_logs']
    collection.insert_one({'error':'test'})

except Exception as e:
    print('ERROR IN ERROR LOGS')
    print(e)