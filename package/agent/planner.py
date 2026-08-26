class Planner:
    def plan(self, objective):
        return {
            "objective": objective,
            "steps": [
                "Analyser la demande",
                "Construire une solution",
                "Tester",
                "Sauvegarder le projet"
            ]
        }
