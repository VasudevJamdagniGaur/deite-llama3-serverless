from fastapi import FastAPI
from pydantic import BaseModel
from llama_cpp import Llama

# Load model once on cold start
model = Llama(model_path='/mnt/models/llama3-8b-q4_0.gguf')

app = FastAPI()

class Request(BaseModel):
    prompt: str

@app.post('/run')
async def run(req: Request):
    full_prompt = 'You are a kind, empathetic therapist. ' + req.prompt
    out = model(full_prompt, max_tokens=200, stream=False)
    return {'text': out.choices[0].text}
