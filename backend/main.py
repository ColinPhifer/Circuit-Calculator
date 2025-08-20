# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from logic import ohms_law, voltage_divider, rc_time_constant, series_resistance, parallel_resistance

app = FastAPI(title="Circuit Calculator")

class OhmsLawRequest(BaseModel):
    voltage: float
    resistance: float

class VoltageDividerRequest(BaseModel):
    input_voltage: float = None
    r1: float = None
    r2: float = None

class RCRequest(BaseModel):
    resistance: float = None
    capacitance: float = None

class SeriesResistanceRequest(BaseModel):
    resistances: list[float] = None

class ParallelResistanceRequest(BaseModel):
    resistances: list[float] = None

@app.post("/ohms_law")
def calculate_ohms_law(request: OhmsLawRequest):
    current = request.voltage / request.resistance
    return {"current": current}
    
@app.post("/voltage_divider")
def calculate_voltage_divider(request: VoltageDividerRequest):
    if request.input_voltage is not None and request.r1 is not None and request.r2 is not None:
        return {"result": voltage_divider(input_voltage=request.input_voltage, r1=request.r1, r2=request.r2)}
    else:
        raise ValueError("All parameters must be provided.")
    
@app.post("/rc_time_constant")
def calculate_rc_time_constant(request: RCRequest):
    if request.resistance is not None and request.capacitance is not None:
        return {"result": rc_time_constant(resistance=request.resistance, capacitance=request.capacitance)}
    else:
        raise ValueError("Both resistance and capacitance must be provided.")

@app.post("/series_resistance")
def calculate_series_resistance(request: SeriesResistanceRequest):
    if request.resistances is not None:
        return {"result": series_resistance(resistances=request.resistances)}
    else:
        raise ValueError("Resistances must be provided.")

@app.post("/parallel_resistance")
def calculate_parallel_resistance(request: ParallelResistanceRequest):
    if request.resistances is not None:
        return {"result": parallel_resistance(resistances=request.resistances)}
    else:
        raise ValueError("Resistances must be provided.")
