print("Enter the number between 10 to 40 and you have 5 chances to guess the correct number")
print("Hint: This is a two digit Number multiple of 3 and sum of digits also 3")
chances = 0
maxChances: int = 5

while True:
    n = 30
    userInput = input("enter your number \n")
    if userInput.isnumeric():
        yourNum = int(userInput)
        if 10 <= yourNum <= 40:
            chances += 1
            if yourNum < n:
                if chances == maxChances:
                    print("maximum try limit exceeds, Game loss")
                    confirm: str = input("want to play again? type 'Y' for yes and 'N' for no ")
                    if (confirm == 'y') or (confirm == 'Y'):
                        chances = 0
                        choice = True
                        continue
                    if (confirm == 'n') or (confirm == 'N'):
                        print("thank you for playing")
                        break
                else:
                    print("your guessed number is smaller then actual one")
                    print("try again with larger number")
                    print("your remaining chances are " + str(maxChances - chances))
                    continue
            if yourNum > n:
                if chances == maxChances:
                    print("maximum try limit exceeds, Game loss")
                    confirm: str = input("want to play again? type 'Y' for yes and 'N' for no ")
                    if (confirm == 'y') or (confirm == 'Y'):
                        chances = 0
                        continue
                    if (confirm == 'n') or (confirm == 'N'):
                        print("thank you for playing")
                        break
                else:
                    print("your guessed number is greater then actual one")
                    print("try again with smaller number")
                    print("your remaining chances are " + str(maxChances - chances))
                    continue
            if yourNum == n:
                print("yeah 🎉🎉, You guessed it right 😍")
                print("You have won the game in " + str(chances) + " chance's")
                break
        else:
            print("please try to enter the number between 10 to 40")
    else:
        print("there must be some error occurred or you enters something else, please enter number only")