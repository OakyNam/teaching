"""Reference solution scaffold for a LangGraph-style workflow."""

from __future__ import annotations


def research(state: dict) -> dict:
    state.setdefault("notes", []).append("researched")
    return state


def analyze(state: dict) -> dict:
    state["analysis"] = "enough evidence"
    return state


def respond(state: dict) -> dict:
    state["response"] = "final answer"
    return state
