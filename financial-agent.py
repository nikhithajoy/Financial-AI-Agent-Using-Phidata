# Import necessary libraries and modules
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv
import traceback
import phi.api
from phi.playground import Playground, serve_playground_app

# Load environment variables
load_dotenv()
phi.api = os.getenv("PHI_API_KEY")

# Web Search Agent setup
websearch_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

# Financial AI Agent setup
financial_agent = Agent(
    name="Finance AI Agent",
    role="You know everything related to finance. Search the web about the financial information.",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

# Multi-Agent system combining both agents
multi_ai_agent = Agent(
    team=[websearch_agent, financial_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources", "Use table to display the data"],
    show_tool_calls=True,
    markdown=True
)

# Setup and serve the Playground app
app = Playground(agents=[financial_agent, websearch_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
