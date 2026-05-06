from fastapi import FastAPI
from pydantic import BaseModel
from katalyst_logic import katalyst_agent

app = FastAPI(title="Katalyst Stability Agent")

class InputData(BaseModel):
    query: str
    stochastic_noise: float = 0

@app.post("/process")
def process(data: InputData):
    return katalyst_agent(data.query, data.stochastic_noise)