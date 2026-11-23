import json
import random
import subprocess

# file = open("questions.json", "r")
# questions = json.load(file)
# file.close()

with open("questions.json", "r") as file:
    questions = json.load(file)

def run_quiz():
    name = input("Enter your Name: ").title().strip()
    print("\n========================")
    print("   \033[1mPYTHON QUIZ GAME\033[0m")
    print("========================\n")
    print(f"Welcome {name}!\n")
    print("The Quiz is based on Simple Python code.")
    print("The Quiz has 10 Questions Available.\n")

    while True:
        try:
            num = int(input("Choose how many questions you want to answer (1-10): "))
            if num < 1 or num > 10:
                print("Invalid number. Please choose number from 1 to 10.")
            else:
                break
        except ValueError:
            print("Please enter a whole number, not a word.")
     
    print(f"You have chosen to answer {num} questions")


    print("Choose an answer using A, B, C, or D.")
    print("You can also type the answer itself.\n")
    print(f"Good Luck {name}!\n")
    input("Press Enter to start....")
    subprocess.run(["clear"])

    score = 0
    letters = ["A", "B", "C", "D"]
    user_answers = []
    answered_questions = []

    random.shuffle(questions)

    for number, item in enumerate(questions[:num], 1):

        print("\nQuestion", number)
        print(item["question"])

        for i, option in enumerate(item["options"]):
            print(letters[i] + ".", option)

        while True:
            answer = input("What is the answer? ").lower()
            user_input = answer

            if answer.upper() in letters:
                answer = item["options"][letters.index(answer.upper())].lower()
                break

            if answer in [option.lower() for option in item["options"]]:
                break

            print("Invalid answer. Please enter A, B, C, D, or the answer itself.")

        correct_answer = item["answer"].lower()

        user_answers.append(user_input)
        answered_questions.append(item)

        if answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect")
        subprocess.run(["clear"])

    print("\nYour score:", score, "/", num)

    while True:
        review = input("Do you want to review your answers? (yes/no): ").lower()

        if review == "yes" or review == "y" or review == "no" or review == "n":
            break

        print("Invalid input. Please enter yes or no.")

    if review == "yes" or review == "y":

        print("\n===== CORRECT ANSWERS =====\n")

        for i in range(len(answered_questions)):

            if user_answers[i].upper() in letters:
                answer_number = letters.index(user_answers[i].upper())
                selected_answer = answered_questions[i]["options"][answer_number]
            else:
                selected_answer = user_answers[i]

            if selected_answer.lower() == answered_questions[i]["answer"].lower():
                print(answered_questions[i]["question"])
                print("Your answer:", selected_answer)
                print()

        print("\n===== WRONG ANSWERS =====\n")

        for i in range(len(answered_questions)):

            if user_answers[i].upper() in letters:
                answer_number = letters.index(user_answers[i].upper())
                selected_answer = answered_questions[i]["options"][answer_number]
                selected_letter = user_answers[i].upper()

                if selected_answer.lower() != answered_questions[i]["answer"].lower():
                    print(answered_questions[i]["question"])
                    print("Your answer:", selected_letter + ".", selected_answer)
                    print("Correct answer:", answered_questions[i]["answer"])
                    print()
            else:
                if user_answers[i] != answered_questions[i]["answer"].lower():
                    print(answered_questions[i]["question"])
                    print("Your answer:", user_answers[i])
                    print("Correct answer:", answered_questions[i]["answer"])
                    print()


run_quiz()
