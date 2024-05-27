from configs.database import DB

class BaseModel:
    db = ''
    collection = ''
    def __init__(self, collection_name):
        self.db = DB()
        self.collection = self.db[collection_name]

    def insert(self, data):
        if type(data) == dict:
            return self.collection.insert_one(data).inserted_id
        elif type(data) == list:
            return self.collection.insert_many(data).inserted_ids
        else:
            return None

    def update(self, filter, data, update_all=False):
        if update_all:
            return self.collection.update_many(filter, {'$set': data}).modified_count
        else:
            return self.collection.update_one(filter, {'$set': data}).modified_count

    def get_all(self, limit=0, skip=0):
        data = self.collection.find().sort('_id',-1)
        if limit > 0:
            data = data.limit(limit)
        if skip > 0:
            data = data.skip(skip)

        return_data = []
        for field in data:
            field['_id'] = str(field['_id'])
            return_data.append(field)

        return return_data

    def delete(self, filter):
        return self.collection.delete_many(filter).deleted_count

    def find_all(self, filter, skip=0, limit=0):
        data = self.collection.find(filter)
        if limit > 0:
            data = data.limit(limit)
        if skip > 0:
            data = data.skip(skip)

        return_data = []
        for field in data:
            field['_id'] = str(field['_id'])
            return_data.append(field)

        return return_data


    def find_one(self, filter):
        return self.collection.find_one(filter)

    def count(self, filter):
        return self.collection.count_documents(filter)

    def distinct(self, field):
        return self.collection.distinct(field)
