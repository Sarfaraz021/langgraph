from typing import Annotated
from langchain_tavily import TavilySearch
from typing_extensions import TypedDict
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
# from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.tools import tool
from langgraph.types import Command, interrupt

# Import and load environment variables (like API keys) from .env file
from dotenv import load_dotenv
load_dotenv()

# initializing model definition
llm = ChatOpenAI(model="gpt-4.1", temperature=0.7)

# initializing short term memory
# memory = InMemorySaver()

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

# --------- human in loop tool ----------

@tool
def human_assistance(query: str) -> str:
    """Request assistance from a human."""
    human_response = interrupt({"query": query})
    # Handle both dict-based and direct string resumes
    if isinstance(human_response, dict):
        return human_response.get("data", "")
    return str(human_response)

# --------- human in loop tool ----------

real_time_search = TavilySearch(max_results=2)
tools = [real_time_search, human_assistance]
llm_with_tools = llm.bind_tools(tools)


def chatbot(state: State):
    message = llm_with_tools.invoke(state["messages"])
    # Because we will be interrupting during tool execution,
    # we disable parallel tool calling to avoid repeating any
    # tool invocations when we resume.
    assert len(message.tool_calls) <= 1
    return {"messages": [message]}

graph_builder.add_node("chatbot", chatbot)

tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools", tool_node)

graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge("chatbot", END)
# graph = graph_builder.compile()
graph = graph_builder.compile()

