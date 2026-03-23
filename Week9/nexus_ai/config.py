from config.llm_client import get_model_client


class NexusConfig:

    def __init__(self):

        self.model_client = get_model_client()

        self.max_iterations = 3
        self.enable_memory = True
        self.enable_logging = True

        self.agents = {
            "planner": "Planner Agent",
            "researcher": "Research Agent",
            "coder": "Code Agent",
            "analyst": "Analysis Agent",
            "critic": "Critic Agent",
            "optimizer": "Optimizer Agent",
            "validator": "Validator Agent",
            "reporter": "Reporter Agent"
        }

    def get_model(self):
        return self.model_client


def create_config():
    return NexusConfig()