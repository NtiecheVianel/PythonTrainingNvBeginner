print("Simple Quiz Game".center(50))
print("The rules are simple, You have three attempts for each question. If you fail, the question is cancelled and you won't get any marks.")
ready = input("Are you ready? (Yes/No): ").strip().lower()
if ready == "yes":
    print("Ok, Great! Let's get the game started!")
    input("Press Enter to continue...")

    marks = 0

    # Question 1
    answer1 = input("What's the capital of France?").strip().lower()
    if answer1 == "paris":
        print("Correct! You get 1 mark.")
        marks = marks + 1
    else:
        print("Incorrect, Two attempts left, Please retry ")
        answer1 = input("What's the capital of France?").strip().lower()
        if answer1 == "paris":
            print("Correct! You get 1 mark.")
            marks = marks + 1
        else:
            print("Incorrect, One attempt left, Please retry ")
            answer1 = input("What's the capital of France?").strip().lower()
            if answer1 == "paris":
                print("Correct! You get 1 mark.")
                marks = marks + 1
            else:
                print("Incorrect, No attempts left, Question cancelled.")
                print("You get 0 marks.")

    # Question 2
    answer2 = input("Who founded Microsoft?").strip().lower()
    if answer2 == "bill gates":
        print("Correct! You get 1 mark.")
        marks = marks + 1
    else:
        print("Incorrect, Two attempts left, Please retry ")
        answer2 = input("Who founded Microsoft?").strip().lower()
        if answer2 == "bill gates":
            print("Correct! You get 1 mark.")
            marks = marks + 1
        else:
            print("Incorrect, One attempt left, Please retry ")
            answer2 = input("Who founded Microsoft?").strip().lower()
            if answer2 == "bill gates":
                print("Correct! You get 1 mark.")
                marks = marks + 1
            else:
                print("Incorrect, No attempts left, Question cancelled.")
                print("You get 0 marks.")

    # Question 3
    answer3 = input("What is the largest ocean on Earth?").strip().lower()
    if answer3 == "pacific":
        print("Correct! You get 1 mark.")
        marks = marks + 1
    else:
        print("Incorrect, Two attempts left, Please retry ")
        answer3 = input("What is the largest ocean on Earth?").strip().lower()
        if answer3 == "pacific":
            print("Correct! You get 1 mark.")
            marks = marks + 1
        else:
            print("Incorrect, One attempt left, Please retry ")
            answer3 = input("What is the largest ocean on Earth?").strip().lower()
            if answer3 == "pacific":
                print("Correct! You get 1 mark.")
                marks = marks + 1
            else:
                print("Incorrect, No attempts left, Question cancelled.")
                print("You get 0 marks.")

    print("\nLet's calculate your marks:")
    print( f"Therefore your mark is {marks} out of 3")
    if marks == 0:
        print("Better luck next time, Buddy, Bye!")
    elif marks == 1:
        print("Hmmm, bad but you can do better!")
    elif marks == 2:
        print("Good job! You're getting the hang of it.")
    elif marks == 3:
        print("Excellent work! You're a quiz master.")
    print("Thanks for playing!")

    continue_game = input("Do you want to play again? (Yes/No): ").strip().lower()
    if continue_game == "yes":
        print("Restart the program to play again.")
    else:
        print("Thanks for playing! Goodbye!")
else:
    print("Maybe next time! Goodbye!")