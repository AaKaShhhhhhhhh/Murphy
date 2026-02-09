# Metrics Template for Learning Agent

## Key Metrics to Measure

### Incident Metrics
- **Incident Duration**: Total time from detection to resolution.
- **Detection Time**: Time taken to detect the incident.
- **Response Time**: Time taken to start investigation after detection.
- **Resolution Time**: Time taken to resolve the incident after identifying the root cause.

### Impact Metrics
- **User Impact**: Number of users affected.
- **Business Impact**: Revenue loss, SLA breaches, reputation damage.
- **Service Impact**: List of affected services and their downtime.

### Root Cause Metrics
- **Frequency of Similar Issues**: How often this type of issue has occurred.
- **Monitoring Gaps**: Metrics or logs that failed to detect the issue.
- **Testing Gaps**: Missing test cases that could have caught the issue.

### Preventive Metrics
- **Monitoring Improvements**: New metrics or alerts added.
- **Testing Enhancements**: New test cases or coverage improvements.
- **Process Changes**: Updates to incident response or deployment processes.

## Data Sources
- **Monitoring Tools**: Metrics and logs from monitoring-server.
- **GitHub**: Deployment history, code changes, and issues.
- **Slack**: Communication logs during the incident.

## Reporting
- Include these metrics in post-mortem reports.
- Use them to identify patterns and suggest preventive measures.