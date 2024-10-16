print("*********************Welcome to kaun banega crorepati***********************")
g = input("Enter yes to play the game - ").lower()
if g != "yes":
    print("invalid input! Try Again!")
    quit()

prizeAmount = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,"1 Crore","7.5 Crore"]
winningAmount = ""
finWinAmt = ""
winSlab = ["10000","3200000","7500000","7.5 Crore"]
qAns = [["Which animal is known as the 'Ship of the Desert'?","B","Horse","Camel","Tiger","Dog"],
             ["How many days are there in a week?","A","7 days","6 days","8 days","10 days"],
             ["What is the capital if india","C","PUNE","KOLKATA","DELHI","MAHARASHTRA"],
             ["How many hours are there in a day?","D","20 HOUR","16 HOUR","12 HOUR","24 HOUR"],
             ["How many letters are there in the English alphabet?","A","26","20","10","36"],
             ["Rainbow consist of how many colours?","C","1","5","7","10"],
             ["How many days are there in a year","C","300","366","365","399"],
             ["How many minutes are there in an hour?","D","10","40","50","60"],
             ["How many seconds are there in a minute?","A","60","40","50","30"],
             ["How many seconds make one hour?","C","3400","3500","3600","3700"],
             ["How many consonants are there in the English alphabet?","B","20","21","22","23"],
             ["Which animal is known as the king of the jungle?","A","Lion","Tiger","Elephant","Snake"],
             ["Name the National bird of India?","B","CROW","PEACOCK","DOVE","SQUIRREL"],
             ["Name the National animal of India?","A","TIGER","LION","WOLF","CHEETAH"],
             ["What is the National Anthem of India?","a","jana gana mana","amar sonar bangla","hookah bar","tum mile"],
             ["Name the national flower of India?","a","LOTUS","ROSE","LILY","SUNFLOWER"],
             ["Name the national Fruit of India?","A","MANGO","JACKFRUIT","PAPAYA","BANANA"]]
             
try:
    for i in range(15,len(qAns)):
        print("___________________________________________________________________________________")
        print(f"******************Question for Rs - {prizeAmount[i]}*****************************")
        print(qAns[i][0])
        print(f"A. {qAns[i][2]} | B. {qAns[i][3]}")
        print(f"C. {qAns[i][4]} | D. {qAns[i][5]}")
        ans = input("CHOOSE OPTION - ").upper()
        if ans == qAns[i][1].upper():
            winningAmount = str(prizeAmount[i])
            print(f"Correct Ans, You won Rs. {prizeAmount[i]}")
            if winningAmount == winSlab[0]:
                finWinAmt = winningAmount
            elif winningAmount == winSlab[1]:
                finWinAmt = winningAmount
            elif winningAmount == winSlab[2]:
                finWinAmt = winningAmount
            elif winningAmount == winSlab[3]:
                finWinAmt = winningAmount
        else:
            print("Wrong Answer !")
            break

    print(f"Congratulations Your Rs - {finWinAmt} will be transferred to your account after 20 leap year")
    print("Thanks for playing kaun banega crorepati, Have a Good Day")
except Exception as e:
    print(f"Encountered an error, please try again or contact the developer{e}")
