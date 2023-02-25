from bson import ObjectId
from pymongo.database import Database


class BotService():
    def __init__(self, db: Database):
        self.collection = db.bots

    def insert(self, bot: dict) -> str:
        result = self.collection.insert_one(bot)
        return str(result.inserted_id)

    def get_all(self) -> list:
        bots = []
        for bot in self.collection.find():
            bot["_id"] = str(bot["_id"])
            bots.append(bot)
        return bots

    def get_by_id(self, id: str) -> dict | None:
        bot = self.collection.find_one({"_id": ObjectId(id)})
        if bot is not None:
            bot["_id"] = str(bot["_id"])
            return bot

    def update(self, id: str, updated_bot: dict) -> bool:
        updated_bot["_id"] = ObjectId(updated_bot["_id"])
        result = self.collection.update_one({"_id": ObjectId(id)}, {"$set": updated_bot})
        return result.modified_count > 0

    def delete(self, id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0