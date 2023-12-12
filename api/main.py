from src.model import Falcon
from src.utils.utils import process_prompt_utils

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class InputPrompt(BaseModel):
    prompt: str


class ProcessedPrompt(BaseModel):
    processed_prompt: str


class OutputResponse(BaseModel):
    generated_text: str


falcon = Falcon()


@app.post("/generate/", response_model=OutputResponse)
def generate_text(prompt: InputPrompt):
    generated_text = falcon.generate(prompt.prompt)
    return {"generated_text": generated_text}


@app.post("/process_prompt", response_model=OutputResponse)
def process_prompt(prompt: InputPrompt):
    processed_prompt = process_prompt_utils(prompt.prompt)
    return {"generated_text": processed_prompt}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
