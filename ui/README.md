# Intelligent Incident Response Dashboard

This Streamlit dashboard provides a real-time interface for monitoring agent activity and managing production incidents.

## Features
- **Real-Time Updates**: Polls every 2 seconds for the latest data.
- **Metrics Overview**: Displays key incident metrics.
- **Quick Actions**: Simulate incidents, run tests, and view history.
- **Incident Details**: Expandable panel for active incidents.
- **Agent Activity Feed**: Live feed of agent actions.
- **Recent Incidents**: Table of past incidents.
- **System Health Sidebar**: Displays server and connection statuses.

## Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the dashboard:
   ```bash
   streamlit run dashboard.py
   ```

## Configuration
- Update `config.py` for API endpoints and database paths.
- Customize `styles.css` for additional styling.

## Bonus Features
- Plotly charts for incident trends.
- Export incident data to CSV.
- Sound notifications for new incidents.

## File Structure
- `dashboard.py`: Main Streamlit app.
- `requirements.txt`: Python dependencies.
- `config.py`: Configuration file.
- `styles.css`: Custom styling (optional).
- `README.md`: Documentation.