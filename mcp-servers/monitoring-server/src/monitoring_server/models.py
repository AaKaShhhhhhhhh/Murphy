from typing import List, Dict, Any
from pydantic import BaseModel

class Metric(BaseModel):
    name: str
    value: float
    unit: str

class MetricHistory(BaseModel):
    timestamp: str
    value: float

class Alert(BaseModel):
    severity: str
    metric: str
    threshold: float
    current_value: float
    started_at: str

class ServiceHealth(BaseModel):
    service: str
    status: str
    latency: float
    error_rate: float
