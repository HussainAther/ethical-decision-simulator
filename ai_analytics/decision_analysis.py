from sentiment_analysis import SentimentAnalyzer
from empathy_detector import EmpathyDetector

class DecisionAnalyzer:
    def __init__(self):
        self.sentiment_analyzer = SentimentAnalyzer()
        self.empathy_detector = EmpathyDetector()

    def analyze_decision(self, decision_text):
        # Perform sentiment analysis
        sentiment = self.sentiment_analyzer.analyze_sentiment(decision_text)

        # Detect empathy level
        empathy_score = self.empathy_detector.detect_empathy(decision_text)

        # Generate feedback based on sentiment and empathy
        if sentiment == "negative" and empathy_score < 0.5:
            feedback = "Consider the ethical implications for everyone involved."
        elif sentiment == "positive" and empathy_score >= 0.5:
            feedback = "Good empathy and ethical reasoning!"
        else:
            feedback = "Reflect on your decision and consider others' perspectives."

        return {
            "sentiment": sentiment,
            "empathy_score": empathy_score,
            "feedback": feedback
        }

# Example Usage
analyzer = DecisionAnalyzer()
decision_text = "I think telling the truth is the best approach, even if it’s difficult."
result = analyzer.analyze_decision(decision_text)
print("Analysis Result:", result)

