import random
import time
from datetime import datetime, timedelta
from typing import List, Dict
from .models import Metric, MetricHistory, Alert, ServiceHealth

class MonitoringSimulator:
    def __init__(self):
        self.baselines = {
            "api_response_time": 120,
            "error_rate": 0.5,
            "cpu_usage": 30,
            "memory_usage": 40,
            "database_query_time": 50,
            "active_connections": 100,
            "throughput": 500,
        }
        self.alerts = []
        self.incident_active = False

    def get_current_metrics(self) -> List[Metric]:
        metrics = []
        for name, baseline in self.baselines.items():
            value = baseline + random.uniform(-baseline * 0.1, baseline * 0.1)
            unit = self._get_unit(name)
            metrics.append(Metric(name=name, value=round(value, 2), unit=unit))
        return metrics

    def get_metric_history(self, metric_name: str, duration: str = "1h") -> List[MetricHistory]:
        duration_map = {"15m": 15, "1h": 60, "6h": 360, "24h": 1440}
        minutes = duration_map.get(duration, 60)
        now = datetime.now()
        history = []
        for i in range(minutes):
            timestamp = (now - timedelta(minutes=i)).isoformat()
            value = self.baselines[metric_name] + random.uniform(-5, 5)
            history.append(MetricHistory(timestamp=timestamp, value=round(value, 2)))
        return history

    def check_alerts(self) -> List[Alert]:
        return self.alerts

    def get_service_health(self) -> List[ServiceHealth]:
        services = ["api-server", "database", "cache", "queue", "storage"]
        health = []
        for service in services:
            status = random.choices(["healthy", "degraded", "down"], weights=[0.7, 0.2, 0.1])[0]
            latency = random.uniform(10, 300) if status != "down" else 0
            error_rate = random.uniform(0, 5) if status != "healthy" else 0
            health.append(ServiceHealth(service=service, status=status, latency=round(latency, 2), error_rate=round(error_rate, 2)))
        return health

    def simulate_incident(self, severity: str, incident_type: str):
        if self.incident_active:
            return

        self.incident_active = True
        if incident_type == "slow_database":
            self.baselines["database_query_time"] *= 2
            self.baselines["api_response_time"] *= 1.5
        elif incident_type == "high_error_rate":
            self.baselines["error_rate"] *= 5
        elif incident_type == "memory_leak":
            self.baselines["memory_usage"] += 50
        elif incident_type == "api_timeout":
            self.baselines["api_response_time"] *= 3

        self.alerts.append(Alert(
            severity=severity,
            metric=incident_type,
            threshold=0,
            current_value=0,
            started_at=datetime.now().isoformat()
        ))

    def resolve_incident(self):
        self.incident_active = False
        self.baselines = {
            "api_response_time": 120,
            "error_rate": 0.5,
            "cpu_usage": 30,
            "memory_usage": 40,
            "database_query_time": 50,
            "active_connections": 100,
            "throughput": 500,
        }
        self.alerts = []

    def _get_unit(self, metric_name: str) -> str:
        units = {
            "api_response_time": "ms",
            "error_rate": "%",
            "cpu_usage": "%",
            "memory_usage": "%",
            "database_query_time": "ms",
            "active_connections": "count",
            "throughput": "req/sec",
        }
        return units.get(metric_name, "")