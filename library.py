class multiplefuction():
    def oddeven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            print("52452 is even number")
            msg="52452 is even number"
        else:
            print("52452 is odd number")
            msg="52452 is odd number"
            return msg
    
    def subfields():
        print("subfields in ai are:")
        lists=["Machine learning","Neural Networks","Vision","Robotics","Speech Processing","Natural language process"]
        for field in lists:
            print(field)
    
    def mrgeligibility():
        sex=input("your sex:")
        age=int(input("your age:"))
        if(sex=="male"):
            if(age>=21):
                print("eligible")
            else:
                print("not eligible")
        elif(sex=="female"):
            if(age>=18):
                print("eligible")
            else:
                print("not eligible")
        else:
            print("invalid")
            return

    def percentage():
        sub1=98
        sub2=99
        sub3=100
        sub4=91
        sub5=95
        total=(sub1+sub2+sub3+sub4+sub5)
        totalsub=5
        print("total:",total)
        percentage=(total/(totalsub*100))*100
        print("percentage:",percentage)
        return

    def triangle():
        height=int(input("height:"))
        breadh=int(input("breadh:"))
        area=(height*breadh)/2
        print("area of triangle:",area)
        height1=int(input("height1:"))
        height2=int(input("height2:"))
        breadh1=int(input("breadh1:"))
        perimeter=height1+height2+breadh1
        print("perimeter of triangle:",perimeter)


