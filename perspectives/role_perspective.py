class RolePerspective:
    def __init__(self, role):
        self.role = role
        self.view = self.get_perspective_view()

    def get_perspective_view(self):
        views = {
            "doctor": "You are responsible for patient welfare and informed consent.",
            "patient": "You want the best outcome but feel anxious about the procedure.",
            "bystander": "You are a family member concerned about possible outcomes."
        }
        return views.get(self.role, "Role not defined")

    def display_perspective(self):
        print(f"As a {self.role}: {self.view}")

# Usage Example
doctor_view = RolePerspective("doctor")
doctor_view.display_perspective()

