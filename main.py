from fastapi import FastAPI
from random import randint

app = FastAPI()


@app.get('/watch/pulse-check')
def get_pulse():
    return {
        "pulse": randint(50, 150)
    }
