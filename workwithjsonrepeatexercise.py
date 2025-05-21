import random
import json
import requests
import html
import pprint
score_correct = 0
score_incorrect = 0
endgame = ""
while endgame != "quit":
    r = requests.get("https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple")
    if r.status_code != 200:
        endgame = input("There was an error retrieving the question, press enter to continue or type 'quit' to quit.")
    else:
        answer_indicators = ["A", "B", "C", "D"]
        data = json.loads(r.text)
        question = data["results"][0]["question"]
        answers = data["results"][0]["incorrect_answers"]
        correct_answer = data["results"][0]["correct_answer"]
        answers.append(correct_answer)
        random.shuffle(answers)
        correct_index = answers.index(correct_answer)
        print(html.unescape(question) + "\n")
        for i, answer in enumerate(answers):
            print(f"{answer_indicators[i]} - {html.unescape(answer)}")
        user_answer = input("\nWhat is your answer?:").upper()
        if user_answer in answer_indicators:
            if user_answer == answer_indicators[correct_index]:
                print(f"Your answer is correct!, the correct answer is: {answer_indicators[correct_index]} - {html.unescape(correct_answer)}")
                score_correct += 1
            else:
                print(f"Sorry, {html.unescape(user_answer)} is incorrect. The correct answer is {answer_indicators[correct_index]} - {html.unescape(correct_answer)}")
                score_incorrect += 1
        else:
            print("Your entry isn't in the options. Please select A, B, C, or D.")

        print("\n##################")
        print(f"Your score is:\nCorrect answers: {str(score_correct)} \nIncorrect answers: {str(score_incorrect)}")
        print("##################")
    endgame = input("\nPress enter to play again or type 'quit' to quit the game: ").lower()
print("\nThanks for playing!")
