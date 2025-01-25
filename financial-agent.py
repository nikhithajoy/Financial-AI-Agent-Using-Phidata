# Import necessary libraries and modules
from phi.agent import Agent  # Agent class to create AI agents
from phi.model.groq import Groq  # Groq model to generate responses based on the 'llama-3.3-70b-versatile' model
from phi.tools.yfinance import YFinanceTools  # YFinance tools to fetch stock market data
from phi.tools.duckduckgo import DuckDuckGo  # DuckDuckGo for web search functionality
import os  # For interacting with the operating system (file management)
from dotenv import load_dotenv  # To load environment variables from a .env file
import traceback  # To print detailed error messages for debugging

# Load environment variables from a .env file
load_dotenv()

# Creating the Web Search Agent
websearch_agent = Agent(
    name="Web Search Agent",  # The agent's name
    role="Search the web for the information",  # The agent's role is to perform web searches
    model=Groq(id="llama-3.3-70b-versatile"),  # Assigning a Groq model (llama-3.3-70b-versatile)
    tools=[DuckDuckGo()],  # This agent will use DuckDuckGo for web searches
    instructions=["Always include sources"],  # The agent is instructed to always include sources in its responses
    show_tool_calls=True,  # This flag will show the calls made to tools (like DuckDuckGo) in the logs
    markdown=True  # This flag allows the agent to use Markdown formatting in its responses
)

# Creating the Financial AI Agent
financial_agent = Agent(
    name="Finance AI Agent",  # The agent's name
    model=Groq(id="llama-3.3-70b-versatile"),  # Using the same Groq model for financial tasks
    tools=[  # Using YFinanceTools to access financial data
        YFinanceTools(
            stock_price=True,  # Enable retrieving stock prices
            analyst_recommendations=True,  # Enable retrieving analyst recommendations
            stock_fundamentals=True,  # Enable retrieving stock fundamentals
            company_news=True  # Enable retrieving company news
        )
    ],
    instructions=["Use tables to display the data"],  # Instructing the agent to format financial data in tables
    show_tool_calls=True,  # Show tool calls (like the financial data tools) in logs
    markdown=True  # Allow Markdown formatting for the financial data
)

# Creating the Multi-Agent System combining both agents
multi_ai_agent = Agent(
    team=[websearch_agent, financial_agent],  # Assign both the websearch and financial agents to the multi-agent team
    model=Groq(id="llama-3.3-70b-versatile"),  # Using the Groq model for the combined team
    instructions=["Always include sources", "Use table to display the data"],  # General instructions for the multi-agent system
    show_tool_calls=True,  # Show tool calls in the log
    markdown=True  # Use Markdown formatting
)

# Main function to interact with the user
def main():
    print("Financial Information Assistant")  # Print a greeting message
    print("--------------------------------")  # Print a separator line
    
    while True:
        try:
            # Take user input as a query
            user_query = input("Enter your query (or 'quit' to exit): ")
            
            # If the user types 'quit', exit the loop and the program
            if user_query.lower() == 'quit':
                print("Exiting the program.")  # Display exit message
                break  # Break the loop to exit the program
            
            # Validate user input: ensure that the query is not just empty spaces
            if not user_query.strip():
                print("Please enter a valid query.")  # If no valid query entered
                continue  # Continue to the next iteration of the loop
            
            # Execute the query using the multi-agent system
            # The multi_ai_agent will handle the query by using the websearch_agent and financial_agent
            multi_ai_agent.print_response(user_query, stream=True)
            print("\n")  # Print a newline for better readability of the output
        
        except Exception as e:
            # If an exception occurs (e.g., incorrect query or a tool fails), print the error details
            print(f"An error occurred: {e}")  # Print the error message
            print("Traceback:")  # Print traceback to get detailed error information
            traceback.print_exc()  # Display the traceback of the error for debugging
            print("\nPlease try again or check your input.")  # Prompt the user to try again or check input

# Entry point of the program
if __name__ == "__main__":
    main()  # Call the main function to start the program
