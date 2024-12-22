tam=int(input("Enter the tamil mark:"))
eng=int(input("Enter the english mark:"))
mat=int(input("Enter the maths mark:"))
sci=int(input("Enter the science mark:"))
soc=int(input("Enter the social mark:"))
total=tam+eng+mat+sci+soc
average=total/5
if tam>=35 and eng>=35 and mat>=35 and sci>=35 and soc>=35:
    print("Result: pass") 
    if average>90 and average<=100:
        print("Grade:A")
        for i in range(5):
            print("very very good")
    elif average>80 and average<=89:
        print("Grade:B")
    elif average>70 and average<=79:
        print("Grade:C")
    elif average>=60 and average>=69:
        print("Grade:D") 
    else:
        print("grade: A")
else:
    print("fail")