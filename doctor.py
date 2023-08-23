count=0
fee=0
try:
    for u in range(20):
        a=int(input())
        if a>0 and a<=120:
            if a<17:
                fee+=200
            elif a>=17 and a<=40:
                fee+=400
            elif a>40:
                fee+=300
        else:
            print("Invalid Input")
            exit()
    print(f"Total Income: {fee} INR")
except EOFError:
    print(f"Total Income: {fee} INR")


'''A doctor has a clinic where he serves his patients. The doctor’s consultation fees are different for different groups of patients depending on their age. If the patient’s age is below 17, fees is 200 INR. If the patient’s age is between 17 and 40, fees is 400 INR. If patient’s age is above 40, fees is 300 INR. Write a code to calculate earnings in a day for which one Array/List of values representing age of patients visited on that day is passed as input.
Age should not be zero or less than zero or above 120.
Doctor consults a maximum (max) of 20 patients a day.'''