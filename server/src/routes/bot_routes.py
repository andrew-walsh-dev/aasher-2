from fastapi import Body
from main import app, db
from services.bot_service import BotService

api_path = "/bots"
bot_service = BotService(db)

@app.post(f"{api_path}")
def create_bot(body = Body()):
    try:
        created_id = bot_service.insert(body)
        return {"created_id": created_id}
    except Exception as e:
        return {"error": str(e)}, 500

@app.get(f"{api_path}")
def get_bots():
    try:
        bots = bot_service.get_all()
        return {"bots": bots}
    except Exception as e:
        return {"error": str(e)}, 500
    
@app.get(f"{api_path}/{id}")
def get_bot(id: str):
    try:
        bot = bot_service.get_by_id(id)
        return {"bot": bot}
    except Exception as e:
        return {"error": str(e)}, 500

@app.put(f"{api_path}/{id}")
def edit_bot(id: str, body = Body()):
    try:
        result = bot_service.update(id, body)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}, 500

@app.delete(f"{api_path}/{id}")
def delete_bot(id: str):
    try:
        result = bot_service.delete(id)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}, 500