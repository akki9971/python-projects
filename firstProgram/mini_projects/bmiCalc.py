height = int(input("your height in cms "))
weight = int(input("your weight in kgs "))

bmiRatio = round(weight/pow(height/100,2),1)
# print(bmiRatio)
if bmiRatio >= 18.5:
    if bmiRatio>24.9:
        if bmiRatio > 30:
            if bmiRatio > 35:
                if bmiRatio > 40:
                    print(str(bmiRatio)+" kya h ye , itta sara bmi ratio gende phatt jayega weight kam kr")
                else:
                    print("your bmi ratio is " + str(bmiRatio) +" you are overweight at level 3")
            else:
                print("your bmi ratio is " + str(bmiRatio) +" you are overweight at level 2")
        else:
            print("your bmi ratio is " + str(bmiRatio) +" you are overweight at level 1")
    else:
        print("your bmi ratio is " + str(bmiRatio) +" you are absolutely fit n fine ")
else:
    print("your bmi ratio is " + str(bmiRatio) +"   you are underweight")