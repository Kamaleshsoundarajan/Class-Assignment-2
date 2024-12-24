class multiplefunctions():
    def Subfields():
        print("Sub-fields in AI are:")
        list=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for temp in list:
            print(temp)

    def OddEven():
            num1=int(input("Enter a number:"))
            if((num1%2)==0):
                print(num1, "is Even number")
                message="even"
            else:
                print(num1, "is Odd")
                message="odd"
            return message

    def Elegible():
            Gender=input("Your Gender:")
            Age=int(input("Your Age:"))
            if(Age>=21):
                print("Eligible for marriage")
                message="Eligible"
            elif(Age==18):
                print("Eligible for marriage")
                message="Eligible"
            else:
                print("Not Eligible")
                message="Not Eligible"
            return message
    
    def markpercent():
            Subject1=int(input("Subject1="))
            Subject2=int(input("Subject2="))
            Subject3=int(input("Subject3="))
            Subject4=int(input("Subject4="))
            Subject5=int(input("Subject5="))
            Sum=(Subject1+Subject2+Subject3+Subject4+Subject5)
            print("Total:", Sum)
            percent=(Sum/500)*100
            print("Percentage :",percent)
    
    def triangle():
            Height=float(input("Height:"))
            Breadth=float(input("Breadth:"))
            Formula=(Height*Breadth)/2
            print("Area of Triangle:",Formula)
            Height1=float(input("Height1:"))
            Height2=float(input("Height2:"))
            Breadth1=float(input("Breadth:"))
            Pf=Height1+Height2+Breadth1
            print("Perimeter of Triangle:",Pf)



    