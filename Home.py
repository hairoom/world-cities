import streamlit as st

st.set_page_config(
    page_title="World Cities App",
    page_icon="🌍",
)

st.title("🌍 World Cities App")

st.write("""
Welcome to the World Cities application!

This app allows you to explore and visualize data about cities around the world. 
You can filter cities by population, capital status, and country, and view them on an interactive map.

### Features:
- 📊 Interactive data visualization
- 🗺️ Map view of cities
- 🔍 Filter by population, capital status, and country
- 📈 Population statistics by country

### Getting Started:
Use the sidebar to navigate to the **app** page to start exploring the data.
""")

st.info("👈 Select a page from the sidebar to get started!")
