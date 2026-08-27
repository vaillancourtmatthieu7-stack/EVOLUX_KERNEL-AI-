class CodeAgent:
    def create_plan(self, objective):
        return {
            "type": "software",
            "objective": objective,
            "sandbox": True
        }
