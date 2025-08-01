from setuptools import setup, find_packages

setup(
    name="chatbot",
    version="0.1.0",
    description="A conversational agent using LangGraph",
    packages=find_packages(),
    package_dir={"": "."},
    python_requires=">=3.11",
    install_requires=[
        "langchain",
      "langchain-anthropic",
      "langchain-community",
      "langchain-core",
      "langchain-openai",
      "langchain-tavily",
      "langchain-text-splitters",
      "langgraph",
      "langgraph-api",
      "langgraph-checkpoint",
      "langgraph-cli",
      "langgraph-prebuilt",
      "langgraph-runtime-inmem",
      "langgraph-sdk",
      "langgraph-supervisor",
      "langsmith",
      "langmem",
    ],
)
