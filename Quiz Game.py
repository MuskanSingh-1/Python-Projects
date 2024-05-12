#To build a python program to create a Basic QUiz Game

#Function for displaying the question and options
def display_question(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

#Function to take the user input and get the answer entered by user
def take_user_answer():
    while True:
        try:
            user_input = int(input("Enter your answer: "))
            if 1 <= user_input <= 4:
                return user_input
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#Function to check if the answer entered by user is correct or not and increment the score for correct answer and display coorect answer if wrong answer is entered
def evaluate_answer(user_answer, correct_answer,ans):
    if user_answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print("Incorrect. The correct answer is ", correct_answer,ans)
        return 0

#Function to run the quiz and display all questions one after the other
def run_quiz(questions):
    score = 0
    for q in questions:
        display_question(q["question"], q["options"])
        user_answer = take_user_answer()
        score += evaluate_answer(user_answer, q["correct_answer"], q["ans"])
    return score

#Function where all questions are present
def main():
    questions = [
        {
            "question": "What is the capital of Chhattisgarh?",
            "options": ["Jagdalpur", "Bhilai", "Bilaspur", "Raipur"],
            "correct_answer": 4,
            "ans":"Raipur"
        },
        {
            "question": "What is the samllest planet in our solar system?",
            "options": ["Mars", "Mercury", "Venus", "Saturn"],
            "correct_answer": 2,
            "ans":"Mercury"
        },
        {
            "question": "Where was G20 summit 2023 held?",
            "options": ["Greece", "Egypt", "India", "China"],
            "correct_answer": 3,
            "ans":"India"
        },
        {
            "question": "Ottawa is the capital of which country?",
            "options": ["Canada", "Italy", "Brazil", "Australia"],
            "correct_answer": 1,
            "ans":"Canada"
        },
        {
            "question": "Which of the following is called the blue city of India?",
            "options": ["Jodhpur", "Patiala", "Ludhiana", "Jaipur"],
            "correct_answer": 1,
            "ans":"Jodhpur"
        }
    ]

#First line to be displayed on the screen and asking the user to start the quiz
    print("Welcome to the Quiz Game!")
    input("Press Enter to start...")

#Obtaining the final score
    score = run_quiz(questions)

#Displaying the final score of user
    print("Quiz completed!")
    print("Your final score is: ", score, "\nOut of: 5")

#Calling the main function in order to run the quiz
if __name__ == "__main__":
    main()