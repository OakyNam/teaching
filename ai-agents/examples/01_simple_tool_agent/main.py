"""Simple tool-using agent with OpenAI support and a local mock fallback."""

from __future__ import annotations

import ast
import operator
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Callable, Dict

try:
    from openai import OpenAI  # type: ignore
except ImportError:  # pragma: no cover - optional dependency
    OpenAI = None


ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
}


def get_current_time() -> str:
    return datetime.now(timezone.utc).isoformat()


def calculate(expression: str) -> str:
    def evaluate(node: ast.AST) -> float:
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)
        if isinstance(node, ast.BinOp) and type(node.op) in ALLOWED_OPERATORS:
            return ALLOWED_OPERATORS[type(node.op)](evaluate(node.left), evaluate(node.right))
        raise ValueError(f"Unsupported expression: {expression}")

    tree = ast.parse(expression, mode="eval")
    return str(evaluate(tree.body))


def get_weather(city: str) -> str:
    fake_weather = {
        "london": "Cloudy, 16°C",
        "seoul": "Sunny, 24°C",
        "new york": "Rain, 19°C",
    }
    return fake_weather.get(city.lower(), f"No live weather feed for {city}; use a real weather API in production.")


@dataclass
class Tool:
    name: str
    description: str
    fn: Callable[[str], str]


TOOLS: Dict[str, Tool] = {
    "get_current_time": Tool("get_current_time", "Get the current UTC time", lambda _: get_current_time()),
    "calculate": Tool("calculate", "Evaluate a simple math expression", calculate),
    "get_weather": Tool("get_weather", "Return mock weather for a city", get_weather),
}


def mock_agent(prompt: str) -> str:
    thought_log = []
    lowered = prompt.lower()
    if "time" in lowered:
        thought_log.append("Thought: I should call get_current_time.")
        result = TOOLS["get_current_time"].fn("")
        thought_log.append(f"Action: get_current_time -> {result}")
        thought_log.append(f"Final: The current UTC time is {result}.")
    elif any(op in prompt for op in ["+", "-", "*", "/"]):
        thought_log.append("Thought: I should call calculate.")
        result = TOOLS["calculate"].fn(prompt)
        thought_log.append(f"Action: calculate -> {result}")
        thought_log.append(f"Final: The result is {result}.")
    elif "weather" in lowered:
        city = prompt.split()[-1].strip("?.!")
        thought_log.append("Thought: I should call get_weather.")
        result = TOOLS["get_weather"].fn(city)
        thought_log.append(f"Action: get_weather -> {result}")
        thought_log.append(f"Final: Weather for {city}: {result}")
    else:
        thought_log.append("Thought: No tool is needed.")
        thought_log.append("Final: This demo only supports time, weather, and calculation prompts.")
    return "\n".join(thought_log)


def openai_agent(prompt: str) -> str:
    if OpenAI is None or not os.getenv("OPENAI_API_KEY"):
        return mock_agent(prompt)

    client = OpenAI()
    tools = [
        {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "parameters": {
                    "type": "object",
                    "properties": {"input": {"type": "string"}},
                    "required": [],
                },
            },
        }
        for tool in TOOLS.values()
    ]
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Use tools when helpful. Answer clearly after any tool call."},
            {"role": "user", "content": prompt},
        ],
        tools=tools,
        tool_choice="auto",
    )
    message = response.choices[0].message
    if not message.tool_calls:
        return message.content or "No answer returned."

    outputs = []
    for tool_call in message.tool_calls:
        raw_input = ""
        if tool_call.function.arguments:
            import json
            raw_input = json.loads(tool_call.function.arguments).get("input", "")
        outputs.append(f"{tool_call.function.name} -> {TOOLS[tool_call.function.name].fn(raw_input)}")
    return "\n".join(outputs)


def main() -> None:
    prompt = os.getenv("AGENT_PROMPT", "What is the weather in Seoul?")
    print(openai_agent(prompt))


if __name__ == "__main__":
    main()
