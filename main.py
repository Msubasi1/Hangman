import sys

inLetters = []
outLetters = []
solution = []
myanswer = []
final = []
heal = 5
index = 0
found=0


def inMode(letter, index, heal, found):
    if index==len(myanswer):
        exit(1)

    if letter not in solution:

        heal -= 1
        remainingheal(heal)
        index += 1

        if index > len(myanswer):
            exit(1)
        else:
            print("Guessed Word : " + letter + " The game turned into OUT mode")
            print("You have " + str(heal) + " guesses left")
            print(final)
            print("--------------------------------------------")
            if index == len(myanswer):
                print("You finished all letters")
                print("You lost the game")
                exit(1)
            outMode(myanswer[index], index, heal,found)
    else:
        # check inletters list
        # check final list
        # if ok append both list

        if letter not in inLetters:

            inLetters.append(letter)

            # replace final list
            for e in range(0, len(solution)):
                if solution[e] == letter:
                    final[e] = letter

            index += 1
            if index > len(myanswer):
                exit(1)
            else:
                print("Guessed Word : " + letter + " You are in IN mode")
                print("You have " + str(heal) + " guesses left")
                print(final)
                print("--------------------------------------------")
                found +=1
                if found==len(solution):
                    print("You won the game")
                    exit(0)

                inMode(myanswer[index], index, heal,found)

        else:
            heal -= 1
            remainingheal(heal)
            index += 1
            if index > len(myanswer):
                exit(1)
            else:
                print("Guessed Word : " + letter + " The game turned into OUT mode")
                print("You have " + str(heal) + " guesses left")
                print(final)
                print("--------------------------------------------")
                if index == len(myanswer):
                    print("You finished all letters")
                    print("You lost the game")
                    exit(1)
                outMode(myanswer[index], index, heal,found)


def outMode(letter, index, heal,found):
    if index==len(myanswer):
        exit(1)

    if letter in solution:
        heal -= 1
        remainingheal(heal)
        index += 1

        if index > len(myanswer):
            exit(1)
        else:
            print("Guessed Word : " + letter + " You are in OUT mode")
            print("You have " + str(heal) + " guesses left")
            print(final)
            print("--------------------------------------------")
            if index == len(myanswer):
                print("You finished all letters")
                print("You lost the game")
                exit(1)
            outMode(myanswer[index], index, heal,found)
    else:
        # check outletters list
        # check final list
        # if ok append both list

        if letter not in outLetters:
            index += 1

            if index > len(myanswer):
                exit(1)
            else:
                print("Guessed Word : " + letter + " The game turned into IN mode")
                print("You have " + str(heal) + " guesses left")
                print(final)
                print("--------------------------------------------")
                inMode(myanswer[index], index, heal,found)

        else:
            heal -= 1
            remainingheal(heal)
            index += 1

            if index > len(myanswer):
                exit(1)
            else:
                print("Guessed Word : " + letter + " You are in OUT mode")
                print("You have " + str(heal) + " guesses left")
                print(final)
                print("--------------------------------------------")
                if index == len(myanswer):
                    print("You finished all letters")
                    print("You lost the game")
                    exit(1)
                outMode(myanswer[index], index, heal,found)


def remainingheal(heal):
    if heal == 0:
        print("You lost the game")
        exit(1)


print('Hello, world!')

for e in str(sys.argv[1]):
    solution.append(str(e))

for e in str(sys.argv[2]).split(','):
    myanswer.append(str(e))

print("You have 5 guesses left")
# print(solution)
for e in range(0, len(solution)):
    final.append('-')
print(final)
print("--------------------------------------------")

# START
if myanswer[index] in solution:
    inMode(myanswer[index], index, heal,found)
else:
    outMode(myanswer[index], index, heal,found)
