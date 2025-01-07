#  GUI based quiz Game:

## About the Project:
 
A simple Python-based GUI Quiz Game using `tkinter` and `ttkbootstrap`. This project displays questions with multiple-choice answers and tracks the user's score. It's a fun way to test your knowledge on various topics!
## Requirements
Before you begin, make sure you have the following installed:
-   Python (version 3.6 or above)
-   `ttkbootstrap` library
-   `tkinter` (comes pre-installed with Python)
## Libraries:
-   **ttkbootstrap**: Used to enhance the appearance of tkinter widgets with modern themes. To install this, use:
 `pip install ttkbootstrap`
-   **json**: A built-in Python module to load and manage questions in JSON format.
-   **random**: A Python built-in module to randomize the questions.

## Features:

-   **Multiple Choice Questions**: Each question has four answer options. You select your answer by clicking a button. 
-   **Score Tracking**: Your score is tracked throughout the quiz and displayed at the end. 
-   **Random Question Order**: Questions are shuffled to ensure a different experience each time you play.
-   **Feedback**: After answering a question, you receive immediate feedback on whether your answer was correct or incorrect.   
-   **Modern Interface**: Using `ttkbootstrap` for enhanced visual appeal with a modern theme.
-   **Next Question Button**: After each question, you can move to the next question once you select an answer.
  ## How the Game Works
-   The game starts with a welcome screen and displays the first question.
-   You will be presented with four options for each question.
-   After selecting an option, the game will show whether your answer is correct or incorrect.
-   The score will update accordingly.
-   After you complete all questions, the game will show your total score.
 ## How to Run
- Open a terminal or command prompt.
-  Navigate to the directory containing `quiz_game.py`.
-  Execute the script using the command:
    
    python quiz_game.py
    
The game window will open, displaying the first question.

## Code Explanation

### 1. **Initialization**

The `QuizApp` class initializes the game:
-   Loads questions from the `questions.json` file.
-   Sets up the GUI using `ttkbootstrap` components such as labels, buttons, and frames.

### 2. **Loading Questions**

The `load_questions` method reads the `questions.json` file:

-   Ensures the file exists and is in the correct format.
-   Loads the questions into the application.

### 3. **Displaying Questions**

The `display_question` method:
-   Displays the current question and its options on the GUI.
-   Enables buttons for answer selection.
    
### 4. **Answer Checking**
The `check_answer` method:
-   Compares the user's selected answer with the correct answer.
-   Updates the score and displays feedback.
    

### 5. **Navigation**

-   **Next Question:** The `next_question` method progresses to the     next question or ends the quiz if all questions are answered.
-   **End Quiz:** Displays the final score and closes the game window.

## Example Questions File (`questions.json`)
[
  {
    "question": "What is the capital of France?",
    "options": ["Berlin", "Madrid", "Paris", "Rome"],
    "answer": "Paris"
  },
]
           

