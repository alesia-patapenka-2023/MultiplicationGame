from random import seed, randint


seed(100)
if __name__=="__main__":
    count = 0
    test_passed = 7
    rezume = []
    example = ""
    for i in range(10):
        first = randint(1, 10)
        second = randint(1, 10)
        result = first * second
        example = f"{first} x {second} = ?"
        print(f"Question: {example}", end= "")
        try:
            answer = int(input())
        except ValueError:
            answer = None
        if (answer == result):
            print("Right")
            correct_answer = f"Q{i+1}: {example}; Student Answer: {answer}; Answer: {result}; Status: CORRECT"
            rezume.append(correct_answer)
            count = count + 1
        else:
            print(f"Wrong! The right answer is: {result}")
            wrong_answer = f"Q{i+1}: {example}; Student Answer: {answer}; Answer: {result}; Status: WRONG"
            rezume.append(wrong_answer)
    print(f"Number of correct answers is: {count}")
    if (count >= test_passed):
        print("Congratulations!!!")
    else:
        print("try again!")
    print("*** SUMMARY ***")
    for i in range(10):
        print(rezume[i])



