import mysql.connector
myconnect=mysql.connector.connect(host="localhost",user="root",password="root",database="db")
mycur=myconnect.cursor()
mycur.execute("select * from registration")
for i in mycur:
    print(i)


class Register:
    def reg(self):
        email=input("Enter the email: ")
        password=input("Enter the password: ")
        from validate import Validate
        obj=Validate
        obj.checkmail(self,email)
        obj.validpass(self,password)
        data=(email,password)
        query="insert into registration values(%s, %s)"
        mycur.execute(query,data)
        myconnect.commit()

        print("---You have registered successfully---")
        mycur.execute("select * from registration")
        for i in mycur:
            print(i)

        from login import Login
        log=Login()
        log.login()
object1 =Register()



