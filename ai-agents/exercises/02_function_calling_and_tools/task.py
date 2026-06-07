"""Exercise starter for a tool-calling agent."""

from __future__ import annotations


def get_weather(city: str) -> str:
    raise NotImplementedError


def execute_tool(tool_name: str, tool_input: str) -> str:
    raise NotImplementedError


def agent_loop(user_message: str) -> str:
    raise NotImplementedError


def main() -> None:
    print(agent_loop("What is the weather in Seoul?"))


if __name__ == "__main__":
    main()
