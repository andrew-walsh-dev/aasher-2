from bson import ObjectId


class BotService():
    def __init__(self, db):
        self.collection = db.bots

    def insert(self, bot):
        result = self.collection.insert_one(bot)
        return str(result.inserted_id)

    def get_all(self):
        bots = []
        for bot in self.collection.find():
            bot["_id"] = str(bot["_id"])
            bots.append(bot)
        return bots

    def get_by_id(self, id):
        bot = self.collection.find_one({"_id": ObjectId(id)})
        if bot is not None:
            bot["_id"] = str(bot["_id"])
            return bot

    def update(self, id, updated_bot):
        updated_bot["_id"] = ObjectId(updated_bot["_id"])
        result = self.collection.update_one({"_id": ObjectId(id)}, {"$set": updated_bot})
        return result.modified_count > 0

    def delete(self, id):
        result = self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0