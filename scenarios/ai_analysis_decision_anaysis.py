from transformers import pipeline

class DecisionAnalyzer:
    def __init__(self):
        self.sentiment_analyzer = pipeline("sentiment-analysis")

    def analyze_decision(self, decision_text):
        # Analyze sentiment for empathy or ethical reasoning
        result = self.sentiment_analyzer(decision_text)
        sentiment = result[0]['label']
        print(f"Decision analysis: {sentiment}")
        if sentiment == "NEGATIVE":
            return "Consider the implications for all involved."
        elif sentiment == "POSITIVE":
            return "Good ethical reasoning!"
        else:
            return "Neutral response detected."

# Example Usage
analyzer = DecisionAnalyzer()
feedback = analyzer.analyze_decision("I will tell the patient about all the risks involved.")
print("AI Feedback:", feedback)

