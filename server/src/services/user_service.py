from bson import ObjectId


class UserService():
    def __init__(self, db):
        self.collection = db.users

    def insert(self, user):
        result = self.collection.insert_one(user)
        return str(result.inserted_id)

    def get_all(self):
        users = []
        for user in self.collection.find():
            user["_id"] = str(user["_id"])
            users.append(user)
        return users

    def get_by_id(self, id):
        user = self.collection.find_one({"_id": ObjectId(id)})
        if user is not None:
            user["_id"] = str(user["_id"])
            return user

    def update(self, id, updated_user):
        updated_user["_id"] = ObjectId(updated_user["_id"])
        result = self.collection.update_one({"_id": ObjectId(id)}, {"$set": updated_user})
        return result.modified_count > 0

    def delete(self, id):
        result = self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0