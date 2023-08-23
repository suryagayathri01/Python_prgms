tv={1:10000,2:7000,3:6000}
try:
    n=int(input())
    assert n in tv
    exch=int(input())
    assert exch in [1,2]
    if exch==1:
        wc=int(input())
        assert wc in [1,2]
        if wc==1:
            print(f"{float(tv[n])-(float(tv[n])*0.2):.2f} INR")
        else:
            print(f"{float(tv[n])-(float(tv[n])*0.02):.2f} INR")
    else:
        print(f"{float(tv[n]):.2f} INR")
except:
    print("Invalid Input")


''' A customer has a choice to buy TV from set of 3 company models provided by the store.
If customer takes an exchange offer,then customer will get a discount of 2%, if the old TV is not working else he will get a discount of 20%.
If the customer do not opt for exchange offer then, he has to pay MRP of the TV and display that amount.
Menu for TV condition should be displayed only if customer choose for exchange offer. Whenever the user enters an invalid option, then the code should stop with message "Invalid Input" and it should be displayed in the same format as it is case sensitive.
Assume the following list is already seen by the customer. There should be 3 inputs for each customer, whose answer should be a number given with that choice.
FIRST INPUT CHOICE:
Display List(Select TV Model)
1. Samsung 10000 RS
2. Onida 7000 RS
3. HDLC 6000 RS
SECOND INPUT CHOICE:
Want To Take Exchange Offer?
1. Yes
2. No
THIRD INPUT CHOICE:
Current Condition Of Customer's Old TV
1. Working
2. Not Working'''