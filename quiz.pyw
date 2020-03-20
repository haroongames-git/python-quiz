import time
ts = time.gmtime()

def setTitle(title):
    file = open("\..\quizconsole.log", "a+")
    print("Welcome to the " + title + "!")
    file.write(time.strftime("%Y-%m-%d %H:%M:%S", ts) + " - Title set as " + title + ".\n")
    file.close

def multipleChoice(question, answer1, answer2, answer3, correctanswer):
    file = open("\..\quizconsole.log", "a+")
    print(question + ". Possible answers are: " + answer1 + ", " + answer2 + " and " + answer3 ".")
    answer = input("Enter your answer: ")
    if answer == answer1 or answer == answer2 or answer == answer3:
        if answer == correctanswer:
            print("Correct!")
            file.write(time.strftime("%Y-%m-%d %H:%M:%S", ts) + " - Multiple choice question, answer correct: Question: " + question + ".\nAnswers were " + answer1 + ", " + answer2 + ", " + answer3 + ".\n User put an answer of: " + answer + ".\n")
        else:
            print("You didn't get it right. The answer was: " + correctanswer + ".")
    else:
        print("That answer doesn't exist. I'll ask you one more time.")
        file.write(time.strftime("%Y-%m-%d %H:%M:%S", ts) + " - Multiple choice question, answer incorrect attempt 1/2: Question: " + question + ".\nAnswers were " + answer1 + ", " + answer2 + ", " + answer3 + ".\n User put an answer of: " + answer + ".\n")
        print(question + ". Possible answers are: " + answer1 + ", " + answer2 + " and " + answer3 ".")
    answer = input("Enter your answer: ")
    if answer == answer1 or answer == answer2 or answer == answer3:
        if answer == correctanswer:
            print("Correct!")
            file.write(time.strftime("%Y-%m-%d %H:%M:%S", ts) + " - Multiple choice question, answer correct: Question: " + question + ".\nAnswers were " + answer1 + ", " + answer2 + ", " + answer3 + ".\n User put an answer of: " + answer + ".\n")
            file.close()
        else:
            print("You didn't get it right. The answer was: " + correctanswer + ".")
    else:
        print("That answer doesn't exist. Failed question.")
        file.write(time.strftime("%Y-%m-%d %H:%M:%S", ts) + " - Multiple choice question, answer incorrect attempt 2/2: Question: " + question + ".\nAnswers were " + answer1 + ", " + answer2 + ", " + answer3 + ".\n User put an answer of: " + answer + ".\n")
        file.close()
        
