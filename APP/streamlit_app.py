import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠")

st.title("📊 DU COACHING RACE Analyzer")
st.info("This analyzer is brought to you by coach Davide Ambrosini")
st.write(""" 
Use the sidebar to upload the data and perform your analysis
""")


    page = st.sidebar.selectbox("Choose a page", ["Home", "Upload"])

    if page == "Home":
        st.title("Home Page")
    elif page == "upload":
        st.title("upload")