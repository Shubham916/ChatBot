from fastapi import FastAPI
from pydantic import BaseModel
from model_training import predict_intent

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post('/chatbot')
def chatbot(message: Message):
    user_input = message.message
    intent = predict_intent(user_input)
    return {'intent': intent}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
