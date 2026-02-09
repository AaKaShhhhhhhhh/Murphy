# Incident Response Workflow

## Overview
The `incident-response` workflow orchestrates all agents to handle production incidents end-to-end. It ensures timely detection, investigation, resolution, and documentation of incidents.

## Workflow Stages

### 1. Alert & Initial Response
- **Agents**: Communicator, Detective
- **Actions**:
  - Communicator posts an initial alert to Slack.
  - Detective begins investigating the incident.

### 2. Investigation
- **Agent**: Detective
- **Actions**:
  - Analyze metrics.
  - Correlate with recent changes.
  - Identify the root cause.

### 3. Communication Update
- **Agent**: Communicator
- **Actions**:
  - Post root cause findings to Slack.

### 4. Fix Proposal & Approval Gate
- **Agents**: Detective, Communicator
- **Actions**:
  - Detective proposes a fix.
  - Communicator posts an approval request.
  - Human approval required before proceeding.

### 5. Fix Execution
- **Agent**: Detective
- **Actions**:
  - Execute fix if approved.
  - Escalate if rejected or timed out.

### 6. Verification
- **Agent**: Detective
- **Actions**:
  - Verify metrics have returned to normal.
  - Loop back to investigation if unresolved.

### 7. Resolution & Documentation
- **Agents**: Communicator, Learning
- **Actions**:
  - Communicator announces resolution.
  - Learning agent writes a post-mortem and creates action items.

## Error Handling
- **Agent Timeout**: Escalate to human.
- **Approval Timeout**: Auto-reject for safety.
- **Fix Failure**: Automatic rollback.
- **Verification Failure**: Re-investigation.

## Testing
Use the `incident_response_test.yaml` configuration to test the workflow with mock data.

## Directories
- `diagrams/`: Visual workflow diagrams.
- `triggers/`: Webhook payload examples.

## Outputs
- **Incident ID**: Unique identifier for the incident.
- **Resolution Time**: Total time taken to resolve the incident.
- **Root Cause**: Identified root cause of the incident.
- **Post-Mortem URL**: Link to the post-mortem report.