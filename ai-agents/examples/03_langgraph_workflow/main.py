"""LangGraph-style workflow demo with a fallback executor."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

try:
    from langgraph.graph import END, StateGraph  # type: ignore
except ImportError:  # pragma: no cover - optional dependency
    END = "END"
    StateGraph = None


@dataclass
class WorkflowState:
    question: str
    research_notes: List[str] = field(default_factory=list)
    analysis: str = ""
    answer: str = ""
    needs_more_research: bool = False


def research(state: WorkflowState) -> WorkflowState:
    state.research_notes.append(f"Collected notes for: {state.question}")
    state.needs_more_research = "deep" in state.question.lower()
    return state


def analyze(state: WorkflowState) -> WorkflowState:
    state.analysis = f"We have {len(state.research_notes)} research note(s)."
    return state


def respond(state: WorkflowState) -> WorkflowState:
    state.answer = f"Answer: {state.analysis} Final recommendation for '{state.question}'."
    return state


def route(state: WorkflowState) -> str:
    return "research" if state.needs_more_research and len(state.research_notes) < 2 else "respond"


def run_fallback(question: str) -> WorkflowState:
    state = WorkflowState(question=question)
    state = research(state)
    state = analyze(state)
    if route(state) == "research":
        state.needs_more_research = False
        state = research(state)
        state = analyze(state)
    return respond(state)


def mermaid_graph() -> str:
    return "graph TD\n  research --> analyze\n  analyze -->|more research| research\n  analyze -->|enough info| respond"


def main() -> None:
    question = "Check service health and do a deep investigation"
    state = run_fallback(question)
    print(mermaid_graph())
    print(state.answer)
    if StateGraph is not None:
        graph = StateGraph(WorkflowState)
        graph.add_node("research", research)
        graph.add_node("analyze", analyze)
        graph.add_node("respond", respond)
        graph.set_entry_point("research")
        graph.add_edge("research", "analyze")
        graph.add_conditional_edges("analyze", route, {"research": "research", "respond": "respond"})
        graph.add_edge("respond", END)
        print("LangGraph objects were created successfully.")


if __name__ == "__main__":
    main()
