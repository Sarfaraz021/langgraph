# Import tools for type hints and adding metadata to types
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model

# Import and load environment variables (like API keys) from .env file
from dotenv import load_dotenv
load_dotenv()

# Create the chatbot's memory structure
class State(TypedDict):
    #  Store all conversation messages as a list
    # add_messages tells the system to append new messages, not replace old ones
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)


llm = init_chat_model("anthropic:claude-3-5-sonnet-latest", temperature=0.7)

def chatbot(state: State):
    # Send all previous messages to AI and get response back
    return {"messages": [llm.invoke(state["messages"])]}


graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")

graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()