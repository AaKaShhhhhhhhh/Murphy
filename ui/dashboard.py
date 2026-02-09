import streamlit as st
import time
import random
from datetime import datetime
import pandas as pd
import plotly.express as px

# Set Streamlit page configuration
st.set_page_config(
    page_title="Intelligent Incident Response System",
    layout="wide",
    initial_sidebar_state="collapsed",
    theme="dark"
)

# Simulated data for demonstration purposes
active_incidents = random.randint(0, 5)
avg_resolution_time = random.uniform(15, 45)
incidents_this_week = random.randint(10, 50)
incident_active = active_incidents > 0

# Header Section
st.title("🚨 Intelligent Incident Response System")
status = "System Operational" if not incident_active else "Incident Active"
st.markdown(f"### Status: **{status}**")
st.markdown(f"**Current Time:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Metrics Overview
st.markdown("---")
st.subheader("Metrics Overview")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Active Incidents", active_incidents, delta=f"{random.choice(['+1', '-1'])}")

with col2:
    st.metric("Avg Resolution Time (min)", f"{avg_resolution_time:.2f}", delta=f"{random.choice(['+2.5', '-1.5'])}")

with col3:
    st.metric("Incidents This Week", incidents_this_week, delta=f"{random.choice(['+3', '-2'])}")

# Quick Actions
st.markdown("---")
st.subheader("Quick Actions")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🔥 Simulate Critical Incident"):
        st.success("Critical Incident Simulated!")

with col2:
    if st.button("⚠️ Simulate Medium Incident"):
        st.success("Medium Incident Simulated!")

with col3:
    if st.button("🧪 Run System Test"):
        st.success("System Test Triggered!")

with col4:
    if st.button("📊 View All Incidents"):
        st.info("Redirecting to Incident History...")

# Current Incident Panel
if incident_active:
    with st.expander("Current Incident Details", expanded=True):
        st.markdown("### Incident ID: INC-12345")
        st.markdown("**Severity:** Critical")
        st.markdown("**Timeline:**")
        st.progress(random.uniform(0.2, 0.8))
        st.markdown("**Current Stage:** Investigation → Root Cause → Fix → Resolved")
        st.markdown(f"**Time Elapsed:** {random.randint(5, 120)} minutes")
        st.markdown("**Active Agents:**")
        st.markdown("- 🕵️ Detective: In Progress")
        st.markdown("- 📢 Communicator: Completed")
        st.markdown("- 📝 Learning: Pending")

# Agent Activity Feed
st.markdown("---")
st.subheader("Agent Activity Feed")

# Simulated activity feed data
activity_feed = [
    {"timestamp": datetime.now().strftime('%H:%M:%S'), "agent": "🕵️ Detective", "action": "Analyzing metrics", "status": "In Progress"},
    {"timestamp": datetime.now().strftime('%H:%M:%S'), "agent": "📢 Communicator", "action": "Posted initial alert", "status": "Completed"},
    {"timestamp": datetime.now().strftime('%H:%M:%S'), "agent": "📝 Learning", "action": "Drafting post-mortem", "status": "Pending"},
]

for activity in activity_feed:
    with st.container():
        col1, col2, col3, col4 = st.columns([1, 3, 2, 1])
        col1.markdown(f"**{activity['timestamp']}**")
        col2.markdown(f"{activity['agent']}")
        col3.markdown(f"{activity['action']}")
        col4.markdown(f"**{activity['status']}**")
        if st.button("Details", key=f"details-{activity['timestamp']}"):
            st.info(f"Details for action: {activity['action']}")

# Extend the dashboard with additional sections and features

# Approval Queue (If Pending)
if data["incident_active"]:
    st.markdown("---")
    st.subheader("Approval Queue")
    with st.container():
        st.markdown("**Action Requiring Approval:** Rollback recent deployment")
        st.markdown("**Risk Assessment:** Medium")
        st.markdown("**Estimated Duration:** 15 minutes")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("APPROVE ✅"):
                st.success("Action Approved!")
        with col2:
            if st.button("REJECT ❌"):
                st.error("Action Rejected!")

# Recent Incidents Table
st.markdown("---")
st.subheader("Recent Incidents")
recent_incidents_df = pd.DataFrame(data["recent_incidents"])
st.dataframe(recent_incidents_df)

# System Health Sidebar
st.sidebar.title("System Health")
st.sidebar.markdown("**MCP Server Status:** Online")
st.sidebar.markdown("**Archestra.AI Connection:** Online")
st.sidebar.markdown("**Slack Connection:** Online")
st.sidebar.markdown(f"**Last Update:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Add sound notification toggle
st.sidebar.markdown("---")
sound_notification = st.sidebar.checkbox("Enable Sound Notifications")
if sound_notification:
    st.sidebar.info("Sound notifications enabled for new incidents.")

# Add Plotly charts for incident trends
st.markdown("---")
st.subheader("Incident Trends")
incident_trends = pd.DataFrame({
    "Date": pd.date_range(start="2026-02-01", periods=7),
    "Incidents": [5, 3, 4, 6, 2, 7, 3]
})
fig = px.line(incident_trends, x="Date", y="Incidents", title="Incidents Over Time")
st.plotly_chart(fig)

# Real-time updates
st.markdown("---")
st.info("Dashboard updates every 2 seconds.")
time.sleep(2)