list = ["qus1 = What is the capital of India?","qus2 = What is the capital of Haryana?", "qus3 = What is the capital of Goa?", "qus4 = What is the capital of Punjab?"]
ans = ["qus1 = New Delhi", "qus2 = Chandigarh", "qus3 = Panaji", "qus4 = Chandigarh"]
price = [1000, 2000, 3000, 4000]
def kbc():
    print("Welcome to kbc")
    print("You have 4 questions to answer")
    print("You can win a maximum of 10000")
    print("Let's start the game!")
    for i in range(len(list)):
        print(list[i])
        user_answer = input("Enter your answer: ")
        if user_answer.lower() == ans[i].split('=')[1].strip().lower():
            print("Correct answer!")
            print(f"You have won {price[i]} rupees")
        else:
            print("Wrong answer!")
            print(f"The correct answer is: {ans[i]}")
            break
    else:
        print("Congratulations! You have answered all questions correctly.")
        print("You have won a total of 10000 rupees.")

kbc()