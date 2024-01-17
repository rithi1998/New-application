import datetime
import mysql.connector
myconnect=mysql.connector.connect(host="localhost",user="root",password="root",database="db")
mycursor=myconnect.cursor()
mycursor.execute("select * from details")
for i in mycursor:
    print(i)

global age,dob,salary

class Profile:
    def calculate_age(self):
        year=int(input("Enter birth year: "))
        month=int(input("Enter birth month: "))
        date=int(input("Enter birth date: "))
        dob = datetime.date(year,month,date)
        today = datetime.date.today()
        age =today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        print("Your age is: ",age)
        print("1.Below 1 lakhs  2. below 2 lakhs 3. Between 5 - 10 lakhs  4. Above 10 lakhs")
        salary=int(input("Enter your income range: "))
        number=(input("Enter your mobile number: "))
        data=[]
        data.append(salary)
        data.append(age)
        data.append(number)
        query="insert into details(salary,age,phone) values(%s,%s,%s)"
        mycursor.execute(query,data)
        myconnect.commit()
        mycursor.execute("select * from details")
        for i in mycursor:
            print(i)
        prof.contact_num(number,salary,age)
        
 
    def contact_num(self,number,salary,age):
        print("1. SMS 2.Call")
        number1=int(input("How would you like to verify your number? ")) 
        if number1==1:
            print("You will get a SMS from our side for verification")
            one_pass=input("Enter OTP: ")
            if len(one_pass)==4:
                print("Your account is verified")
            else:
                print("Your OTP is wrong..Try again")
            
        elif number1==2:
            print("You will get a call from our side for verification")
            print("1.Yes 2.No")
            call=int(input("Did you received the call? "))
            if call==1:
                print("You will be directed to policy plans page")
            else:
                print("Kindly wait for sometime and try again")
        else:
            print("Enter a valid option")

       


        from policy import Policy
        pol=Policy()
        pol.plan()
        pol.suggest()
        

prof=Profile()


    









