# Agents Directory

This directory contains configurations and resources for various AI agents used in the system.

## Detective Agent

### Role
The Detective Agent is responsible for investigating production incidents by analyzing metrics, logs, and recent changes. It identifies the root cause, assesses severity, and provides actionable recommendations.

### Configuration Files
- `detective.yaml`: Main configuration for the Detective Agent.
- `detective_test.yaml`: Test configuration using mock data.

### Prompts Directory
The `prompts/` directory contains iterations of prompt engineering for the Detective Agent.

### Example Conversations
#### Successful Root Cause Identification
**Input:**
- Incident: High error rate on API `/checkout`
- Metrics: Spike in 500 errors at 10:15 AM
- Deployment: New release at 10:00 AM

**Output:**
```
INCIDENT SUMMARY

What broke: Checkout API
When: 10:15 AM
Impact: Users unable to complete purchases

ROOT CAUSE

Primary cause: Bug in new release
Contributing factors: Lack of rollback mechanism
Evidence: Error logs, deployment timing

SEVERITY

Level: Critical
Users affected: 10,000+
Business impact: Revenue loss, customer dissatisfaction

RECOMMENDED ACTIONS

- Rollback to previous release
- Add rollback mechanism in CI/CD pipeline
```

#### Handling Ambiguous Data
**Input:**
- Incident: Intermittent latency on `/search`
- Metrics: Latency spikes at random intervals
- Deployment: No recent changes

**Output:**
```
INCIDENT SUMMARY

What broke: Search API
When: Random intervals
Impact: Slower search results

ROOT CAUSE

Primary cause: High database load
Contributing factors: Inefficient query
Evidence: Database metrics, query logs

SEVERITY

Level: Medium
Users affected: 5,000
Business impact: Minor user frustration

RECOMMENDED ACTIONS

- Optimize database query
- Add caching for frequent searches
```

#### Escalation to Humans
**Input:**
- Incident: Complete outage of `/login`
- Metrics: No data available
- Deployment: No recent changes

**Output:**
```
INCIDENT SUMMARY

What broke: Login API
When: Ongoing
Impact: Users unable to log in

ROOT CAUSE

Primary cause: Unknown
Contributing factors: Unknown
Evidence: No data available

SEVERITY

Level: Critical
Users affected: All
Business impact: Total service disruption

RECOMMENDED ACTIONS

- Escalate to on-call engineer
- Investigate infrastructure issues
```