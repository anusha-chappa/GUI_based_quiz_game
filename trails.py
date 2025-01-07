import json
import random

def load_questions():
    try:
        with open('questions.json') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: questions.json not found.")
        exit()
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in questions.json.")
        exit()

def display_question(question_data):
    print(question_data['question'])
    for idx, option in enumerate(question_data['options'], start=1):
        print(f"{idx}. {option}")

def get_answer():
    while True:
        try:
            choice = int(input("Enter the number of your answer: "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Please choose a valid option (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def check_answer(question_data, user_choice):
    correct_answer = question_data['answer']
    user_answer = question_data['options'][user_choice - 1]

    if user_answer == correct_answer:
        print("✅ Correct!")
        return 1
    else:
        print(f"❌ Incorrect! The correct answer was {correct_answer}.")
        return 0

def save_high_score(score):
    with open('high_scores.json', 'w') as file:
        json.dump({"high_score": score}, file)

def load_high_score():
    try:
        with open('high_scores.json') as file:
            data = json.load(file)
            return data.get("high_score", 0)
    except FileNotFoundError:
        return 0

def end_summary(score, total_questions):
    print(f"You answered {score} out of {total_questions} questions correctly!")
    if score == total_questions:
        print("🎉 Perfect score! Amazing job!")
    elif score > total_questions / 2:
        print("👍 Great work! Keep practicing.")
    else:
        print("💪 Keep trying! You'll get better.")

def add_question():
    question = input("Enter the question: ")
    options = [input(f"Option {i+1}: ") for i in range(4)]
    answer = input("Enter the correct answer: ")
    #difficulty = input("Enter difficulty (Easy/Medium/Hard): ")
    #category = input("Enter category: ")

    new_question = {
        "question": question,
        "options": options,
        "answer": answer,
        #"difficulty": difficulty,
        #"category": category
    }

    try:
        with open('questions.json', 'r+') as file:
            questions = json.load(file)
            questions.append(new_question)
            file.seek(0)
            json.dump(questions, file, indent=4)
        print("Question added successfully!")
    except json.JSONDecodeError:
        print("Error: Failed to load questions.json. Ensure it is properly formatted.")


def run_quiz():
    questions = load_questions()
    random.shuffle(questions)
    score = 0

    print("🎮 Welcome to the Quiz Game! 🎉")
    high_score = load_high_score()
    print(f"🥇 Current High Score: {high_score}")

    for question_data in questions:
        display_question(question_data)
        user_choice = get_answer()
        score += check_answer(question_data, user_choice)
        print()

    print(f"Your total score is: {score}/{len(questions)}")
    if score > high_score:
        print("🎉 New High Score! Congratulations!")
        save_high_score(score)
    end_summary(score, len(questions))

if __name__ == "__main__":
    run_quiz()
