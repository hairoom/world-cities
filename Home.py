import streamlit as st
from pathlib import Path

st.set_page_config(page_title="World Cities Streamlit App", layout="centered")

st.title("🌎 World Cities Explorer")
st.write(
    """
    Welcome to the World Cities Streamlit App!
    
    Use this application to explore and analyze city data from around the globe.
    """
)

# Button to navigate to app.py in the "pages" directory
# Streamlit's multipage navigation is handled automatically if app.py exists in "pages"
pages_dir = Path(__file__).parent / "pages"
app_page_path = pages_dir / "app.py"

if app_page_path.exists():
    if st.button("Go to Main App"):
        st.switch_page("pages/app.py")
else:
    st.info("The main app page (pages/app.py) has not been added yet.")
