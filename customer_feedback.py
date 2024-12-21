def calculate_positive_feedback_percentage(ratings):
    if not ratings:
        return 0.0
    
    positive_feedback = [rating for rating in ratings if rating == 4 or rating == 5]
    percentage = (len(positive_feedback) / len(ratings)) * 100
    return round(percentage, 2)
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
positive_feedback_percentage = calculate_positive_feedback_percentage(ratings)
print(f"Positive Feedback: {positive_feedback_percentage}%")