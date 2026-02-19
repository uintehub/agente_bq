# agent_engine_app.py
from vertexai.preview.agent_engines import AdkApp
from agent import root_agent

adk_app = AdkApp(agent=root_agent)