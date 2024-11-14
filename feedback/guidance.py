class FeedbackGenerator:
    def __init__(self):
        pass

    def generate_feedback(self, emotion, decision_quality):
        if emotion == "frustration":
            feedback = "This is a tough decision. Try to consider all perspectives."
        elif decision_quality == "poor":
            feedback = "Consider the ethical implications more carefully."
        elif decision_quality == "good":
            feedback = "Great ethical reasoning! You've considered all factors."
        else:
            feedback = "Reflect on the choice before making a final decision."
        
        print("Generated Feedback:", feedback)
        return feedback

# Example Usage
feedback_gen = FeedbackGenerator()
feedback_gen.generate_feedback("neutral", "good")

