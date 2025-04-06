# app/main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from repharse import get_response

app = FastAPI()

# Allow frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["bogakkgodbbpnbkchmclghcbfpongnlf"],  # or your specific origin like "http://localhost:5500"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    data: str

@app.post("/phrase")
async def rephrase_text(request: TextInput):
    input_text = request.data.strip()
    if not input_text:
        return {"error": "No text provided."}
    
    output = get_response(input_text)[0]
    return {"name": output}
