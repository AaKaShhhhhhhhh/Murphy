import logging
from mcp import MCPServer
from .simulator import MonitoringSimulator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("monitoring_server")

class MonitoringServer(MCPServer):
    def __init__(self):
        super().__init__("monitoring-server")
        self.simulator = MonitoringSimulator()

    async def get_current_metrics(self):
        logger.info("Fetching current metrics")
        return self.simulator.get_current_metrics()

    async def get_metric_history(self, metric_name: str, duration: str = "1h"):
        logger.info(f"Fetching metric history for {metric_name} over {duration}")
        return self.simulator.get_metric_history(metric_name, duration)

    async def check_alerts(self):
        logger.info("Checking active alerts")
        return self.simulator.check_alerts()

    async def get_service_health(self):
        logger.info("Fetching service health status")
        return self.simulator.get_service_health()

    async def simulate_incident(self, severity: str, incident_type: str):
        logger.info(f"Simulating incident: {severity} - {incident_type}")
        self.simulator.simulate_incident(severity, incident_type)

    async def resolve_incident(self):
        logger.info("Resolving all incidents")
        self.simulator.resolve_incident()

if __name__ == "__main__":
    server = MonitoringServer()
    server.run()