from random import seed, randint


seed(100)
if __name__=="__main__":
    count = 0
    test_passed = 7
    for i in range(10):
        first = randint(1, 10)
        second = randint(1, 10)
        result = first * second
        print(f"Question: {first} x {second} = ?", end=" ")
        try:
            answer = int(input())
        except ValueError:
            answer = None
            print("No")

        if (answer == result):
            print("yes")
            count = count + 1
        else:
            print("no")
    print(f"Right is {count}")
    if (count >= test_passed):
        print("Congratulations!!!")
    else:
        print("try again!")


