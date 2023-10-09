#problem1
def HelpMenu():
       choice = input("type p to pause, q to quit, s to summon")
       if choice == "p":
            print("pausing...")
       elif choice == "q":
             print("quiting..")
       else:
             print("summon...")
           
HelpMenu()

#problem2
def CountToTen(a, b, c, d, e, f, g, h, i, j):
    print(a, "+", b, "+", c, "+", d, "+", e, "+", f, "+", g, "+", h, "+", i, "+", j )
CountToTen(1,2,3,4,5,6,7,8,9,10)

num1 = 11
num2 = 15
num3 = 19
#problem3
avarage = (num1 + num2 + num3) /3
print ("The avarage of 11, 15 and 19 is: " , avarage)

