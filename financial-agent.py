from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv
import traceback

load_dotenv()

websearch_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

financial_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(
            stock_price=True, 
            analyst_recommendations=True, 
            stock_fundamentals=True,
            company_news=True
        )
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent = Agent(
    team=[websearch_agent, financial_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources", "Use table to display the data"],
    show_tool_calls=True,
    markdown=True
)

def main():
    print("Financial Information Assistant")
    print("--------------------------------")
    
    while True:
        try:
            user_query = input("Enter your query (or 'quit' to exit): ")
            
            if user_query.lower() == 'quit':
                print("Exiting the program.")
                break
            
            # Validate input
            if not user_query.strip():
                print("Please enter a valid query.")
                continue
            
            # Execute the query
            multi_ai_agent.print_response(user_query, stream=True)
            print("\n")
        
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Traceback:")
            traceback.print_exc()
            print("\nPlease try again or check your input.")

if __name__ == "__main__":
    main()
