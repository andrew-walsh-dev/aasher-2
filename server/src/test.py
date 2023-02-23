from pymongo import MongoClient
from secrets import mongo_uri

mongo_client = MongoClient(mongo_uri)
db = mongo_client.aasher

def test(db):
    try:
        from services.user_service import UserService

        test_user = {
            "first_name": "Andrew",
            "last_name": "Walsh",
            "email": "andrew.jordan.walsh@gmail.com",
            "phone": "8144185942"
        }
        user_service = UserService(db)
        id = user_service.insert(test_user)
        if id:
            print(id)
    except Exception as e:
        print(e)

if __name__=="__main__":
    test(db)
