from enum import Enum
from typing import List, Any


class Process(Enum):
    SEQUENTIAL = "sequential"
    PARALLEL = "parallel"


class Agent:
    def __init__(self, **kwargs):
        self.config = kwargs


class Task:
    def __init__(self, **kwargs):
        self.config = kwargs


class Crew:
    def __init__(self, agents: List[Agent], tasks: List[Task], process: Process = Process.SEQUENTIAL, **kwargs):
        self.agents = agents
        self.tasks = tasks
        self.process = process
        self.config = kwargs

    def kickoff(self, inputs: dict) -> Any:
        # Minimal deterministic simulation of task processing for local testing
        outputs = {"inputs": inputs, "results": []}
        for task in self.tasks:
            desc = task.config.get("description") or task.config.get("description", "")
            agent = task.config.get("agent") or None
            outputs["results"].append({"task": desc, "agent": getattr(agent, 'config', str(agent))})
        return outputs
