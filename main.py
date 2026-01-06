from fastapi import FastAPI, Body
from typing import List
from hardware_sim import HardwareSimulator
from log_parser import LogAnalyzer

app = FastAPI()
hw = HardwareSimulator()
parser = LogAnalyzer()


@app.get("/")
def root():
    return {"msg": "Wiwynn Project Service is Running"}


@app.get("/sensor")
def get_sensor_data():
    return hw.get_metrics()


@app.post("/analyze-log")
def analyze_log(logs: List[str] = Body(...)):
    return parser.analyze(logs)
