import streamlit as st
st.write("App Loaded Successfully")

import asyncio

try: 
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from main import run_crew

st.set_page_config(page_title="AI NewsOrchestrator🤖 App")

st.title("NewsOrchestrator AI 🤖📰")
with st.expander("ℹ️ About This Application"):
    st.markdown("""
    **NewsOrchestrator AI** is a Multi-Agent system built using CrewAI.

    It works by:
    1. Researching the latest updates on your topic
    2. Analyzing credible sources
    3. Structuring information
    4. Generating a polished news article

    Just enter a topic and click **Generate News** 🚀
    """)

topic = st.text_input("Enter a topic")


if st.button("Generate News"):
    if topic:
        with st.spinner("Generating..."):
            try:
                result = run_crew(topic)

                if hasattr(result, "raw"):
                    st.subheader("📰 Generated Article")
                    st.markdown(result.raw)
                else:
                    st.write(result)

            except Exception as e:
                st.error(f"Error: {str(e)}")

    else:
        st.warning("Please enter a topic")
