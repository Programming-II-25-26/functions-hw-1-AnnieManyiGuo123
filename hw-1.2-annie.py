# create a machine can generate the student's score and give messages
# version: Sep 9th
# author: Annie

def calculate_grade():
    # make sure score is in 0-100 and integer
    while True:
        score = int(input("My score is (0-100): "))
        if 0 <= score <= 100:
            break
        else:
            print("Invalid score! Enter a number between 0 and 100")

    bonus = int(input("My bonus is: "))

    final_score = score + bonus

    print("Final score:", final_score)

    # check
    if final_score >= 60:
        print("You pass!")
    else:
        print("You failed!")

    return final_score

calculate_grade()