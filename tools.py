from crewai_tools import SerperDevTool
import streamlit as st


def get_search_tool():
    """Creates the Serper search tool using Streamlit secrets."""
    return SerperDevTool(
        api_key=st.secrets["SERPER_API_KEY"],
        n_results=10
    )
