# Monitoring MCP Server

This is a mock Monitoring MCP Server for simulating a monitoring system like Datadog or Grafana. It generates realistic metrics, alerts, and incidents for demo purposes.

## Features

- **Current Metrics**: Fetches simulated system metrics.
- **Metric History**: Provides time-series data for metrics.
- **Alerts**: Lists active alerts based on simulated incidents.
- **Service Health**: Reports health status of various services.
- **Incident Simulation**: Triggers predefined incidents for testing.
- **Incident Resolution**: Resets metrics and clears alerts.

## Setup

1. **Install dependencies**:

   ```bash
   uv pip install -e .
   ```

2. **Run the server**:

   ```bash
   uv run python src/monitoring_server/server.py
   ```

## Example Usage

### Get Current Metrics

```python
response = await server.get_current_metrics()
print(response)
```

### Get Metric History

```python
response = await server.get_metric_history(metric_name="cpu_usage", duration="1h")
print(response)
```

### Check Alerts

```python
response = await server.check_alerts()
print(response)
```

### Get Service Health

```python
response = await server.get_service_health()
print(response)
```

### Simulate Incident

```python
await server.simulate_incident(severity="critical", incident_type="slow_database")
```

### Resolve Incident

```python
await server.resolve_incident()
```