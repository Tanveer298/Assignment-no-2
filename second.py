# Define the questions and answers
quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Great White Shark"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. J.K. Rowling", "C. Ernest Hemingway", "D. Mark Twain"],
        "answer": "A"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A. Gold", "B. Oxygen", "C. Silver", "D. Hydrogen"],
        "answer": "B"
    }
]

# Function to run the quiz
def run_quiz(quiz):
    score = 0
    print("Welcome to the Quiz!\n")

    for q in quiz:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A, B, C, or D): ").strip().upper()
        
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer was {q['answer']}.\n")

    print(f"Your final score is {score} out of {len(quiz)}.")

# Run the quiz
run_quiz(quiz)