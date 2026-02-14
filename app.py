import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
import time

st.set_page_config(page_title="Greenhouse OS", page_icon="🌿", layout="wide")

st.title("🌿 Autonomous Greenhouse Control Center")

if 'moisture_log' not in st.session_state:
    st.session_state.moisture_log = pd.DataFrame(columns=['Time', 'Moisture_%', 'Pump_Status'])

placeholder = st.empty()

for _ in range(100):
    # Simulated Data from Arduino Uno
    moisture = round(np.random.uniform(30.0, 70.0), 1)
    temp = round(np.random.uniform(22.0, 32.0), 1)
    pump = "ON" if moisture < 40 else "OFF"
    
    new_data = pd.DataFrame([[datetime.now().strftime('%H:%M:%S'), moisture, pump]], 
                            columns=st.session_state.moisture_log.columns)
    st.session_state.moisture_log = pd.concat([st.session_state.moisture_log, new_data]).tail(20)

    with placeholder.container():
        c1, c2, c3 = st.columns(3)
        c1.metric("Soil Moisture", f"{moisture}%", delta="Critical" if moisture < 40 else "Stable")
        c2.metric("Ambient Temp", f"{temp} °C")
        c3.metric("Pump Status", pump)

        if pump == "ON":
            st.warning("💧 Action: Irrigation System Active...")

        fig = px.line(st.session_state.moisture_log, x='Time', y='Moisture_%', 
                      title="Soil Moisture Content Trend", markers=True)
        st.plotly_chart(fig, use_container_width=True)
        
    time.sleep(2)
