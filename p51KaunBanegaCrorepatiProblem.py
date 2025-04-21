ques=["1)WHO IS THE PRIME MINISTER OF INDIA?",
      "2)HOW MANY COLORS ARE IN RAINBOW",
      "3)WHAT IS THE CAPITAL OF INDIA",
      "4)WHICH PLANET IS KNOWN AS RED PLANET",
      "5)WHO IS THE CURRENT PRIME MINISTER OF USA"]

op=["a)NARENDRA MODI\nb)RAHUL GANDHI\nc)INDIRA GANDHI\nd)ABDUL KALAM",
    "a)8  b)2\nc)7  d)10",
    "a)DELHI  b)UP\nc)GOA  d)TAMIL NADU",
    "a)EARTE  b)MARS\nc)JUPITER  d)NONE",
    "a)DONALD TRUMP  b)OBAMA\nc)NARENDRA MODI  d)NONE"]

ans=["a",
     "c",
     "a",
     "b",
     "a"]

money=0
print("Welcome to Kaun Banega Crorepati ")
print("Your game begins:\n")
print("The questions is given in your screen\n\n")
prize=[50000,100000,500000,1000000,1500000]
for i in range(0,5):
    print(ques[i])
    print(op[i])
    answer=input("Please select your option:(a/b/c/d)").lower()
    if answer==ans[i]:
        print("Correct Answer!!✅✅")
        print("You won ",prize[i])
        money=money+prize[i]
    else:
        print("Sorry wrong answer!!❎❎")
        print("The total amount you won is:",money)
        print("Thank you")
        break
print("Congratulations!!🎉🎉🎉\nYou are the Winner of Kon Banega Crorepati")
print("Total Winning:",money)
