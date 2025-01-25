# Financial-Information-Assistant-Using-Agentic-AI
This project provides an interactive financial assistant built using Phi AI, Groq, YFinance, and DuckDuckGo. The assistant can retrieve real-time stock prices, analyst recommendations, company news, and much more. It uses advanced AI models to provide accurate and concise responses to finance-related queries.

## What is Agentic AI?

Agentic AI refers to a class of AI systems designed to autonomously perform tasks, make decisions, and interact with various tools or external environments based on instructions or goals. Unlike traditional AI models that simply process and respond to inputs, Agentic AI systems are equipped with the capability to use external tools, search the web, access databases, and even interact with APIs in real-time. These systems can execute a wide range of actions, including retrieving real-time data, performing calculations, or making recommendations based on specific criteria.

In this project, **Phi AI Agent** is used as an Agentic AI system to handle queries related to financial information. The AI is equipped with tools such as **DuckDuckGo** for web search and **YFinance** for financial data, making it capable of autonomously fetching relevant information and responding to user queries.

## How It Works

1. **Web Search**: 
   The **Web Search Agent** utilizes the **DuckDuckGo** search engine tool to fetch relevant information from the web. This allows the system to gather the latest news, articles, or other publicly available resources to answer specific user queries.

2. **Financial Data**:
   The **Finance AI Agent** uses the **YFinance API** to access real-time stock prices, analyst recommendations, company news, and financial fundamentals for a given stock. By integrating these tools, the system can autonomously retrieve and present complex financial information in an easily understandable format.

3. **Groq Model**:
   The **Groq model** (based on **llama-3.3-70b-versatile**) is a state-of-the-art language model used by both agents. This model helps generate human-like responses and ensure the information provided is coherent and accurate.

4. **Multi-Agent Collaboration**:
   In this setup, both agents (the **Web Search Agent** and the **Finance AI Agent**) are working together under the control of the **multi-ai-agent**. The multi-agent system allows for a more flexible, powerful solution by integrating web search capabilities with financial data retrieval to ensure the most comprehensive response possible.

## Features

- **Web Search**: Fetches information from the web using DuckDuckGo.
- **Stock Market Information**: Provides stock prices, analyst recommendations, fundamentals, and news using YFinance.
- **AI-powered Assistance**: Utilizes the **Groq** model (based on **llama-3.3-70b-versatile**) to generate responses.
- **Interactive Command Line Interface**: Users can input queries and receive real-time results from both the web search and financial tools.

## Requirements

To run this project, make sure you have the following dependencies installed:

- Python 3.7+
- [phidata]([https://github.com/phi-agent/phi](https://docs.phidata.com/introduction))
- `yfinance` library
- `duckduckgo` library
- `python-dotenv` for environment variable management

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/financial-information-assistant.git
cd financial-information-assistant
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
3. Set up environment variables:
Create a .env file in the root directory with the following keys:
```
PHI_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_gemini_api_key
```
Replace your_pinecone_api_key, your_gemini_api_key, and your_llama_api_key with the appropriate keys.
