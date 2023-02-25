from fastapi import Body
from main import app, db
from services.user_service import UserService

api_path = "/users"
user_service = UserService(db)

@app.post(f"{api_path}")
def create_user(body = Body()):
    try:
        created_id = user_service.insert(body)
        return {"created_id": created_id}
    except Exception as e:
        return {"error": str(e)}, 500

@app.get(f"{api_path}")
def get_users():
    try:
        users = user_service.get_all()
        return {"users": users}
    except Exception as e:
        return {"error": str(e)}, 500
    
@app.get(f"{api_path}/{id}")
def get_user(id: str):
    try:
        user = user_service.get_by_id(id)
        return {"user": user}
    except Exception as e:
        return {"error": str(e)}, 500

@app.put(f"{api_path}/{id}")
def edit_user(id: str, body = Body()):
    try:
        result = user_service.update(id, body)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}, 500

@app.delete(f"{api_path}/{id}")
def delete_user(id: str):
    try:
        result = user_service.delete(id)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}, 500