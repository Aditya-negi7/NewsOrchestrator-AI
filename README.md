🚀 Multi-Agent AI News Generation System
CrewAI + Google Gemini 1.5 Flash + Tool-Augmented LLM Architecture
🧠 Overview

This project implements a production-style multi-agent AI system using CrewAI and Google Gemini (1.5 Flash) that autonomously researches and generates structured blog articles on emerging trends.

The system simulates collaborative teamwork between AI agents:

🔎 Research Agent – Gathers real-time insights using web search tools

✍️ Writer Agent – Synthesizes research into a structured, engaging article

Unlike many LLM projects that rely on paid APIs, this system is built entirely using free-tier APIs, demonstrating cost-efficient AI architecture design.

🏗 System Architecture
User Topic
     ↓
Research Agent (Gemini + Search Tool)
     ↓
Structured Research Report
     ↓
Writer Agent (Gemini)
     ↓
Markdown Blog Output
Workflow Type: Sequential Agent Orchestration

Task 1 → Research & analysis

Task 2 → Content generation

Output saved as .md file

🤖 Agents
🔎 Research Agent

Role: Senior Technology Researcher

Capabilities:

Real-time web search

Trend identification

Market risk analysis

Memory-enabled

Delegation allowed

✍️ Writer Agent

Role: Professional Tech Journalist

Capabilities:

Structured narrative writing

Markdown formatting

Clear industry-focused explanations

Independent task execution

🛠 Tech Stack
Component	Technology
LLM	Google Gemini 1.5 Flash
Agent Framework	CrewAI
Tool Integration	Serper (Google Search API)
LLM Interface	LangChain
Environment	Python 3.10
Deployment (Optional)	Streamlit / FastAPI
