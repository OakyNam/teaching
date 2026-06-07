"""Reference solution for a tool-calling agent exercise."""

from __future__ import annotations


def get_weather(city: str) -> str:
    return f"Mock weather for {city}: sunny"


def execute_tool(tool_name: str, tool_input: str) -> str:
    if tool_name == "get_weather":
        return get_weather(tool_input)
    return f"Unknown tool: {tool_name}"


def agent_loop(user_message: str) -> str:
    if "weather" in user_message.lower():
        city = user_message.split()[-1].strip("?.!")
        return execute_tool("get_weather", city)
    return "No tool needed."


def main() -> None:
    print(agent_loop("What is the weather in Seoul?"))


if __name__ == "__main__":
    main()
