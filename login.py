import mysql.connector
myconnect=mysql.connector.connect(host="localhost",user="root",password="root",database="db")
mycur=myconnect.cursor()
mycur.execute("select * from registration")
for i in mycur:
    print(i)

class Login:
    def login(self):
        em=input("Enter your mail id: ")
        passwd=input("Enter your password: ")
        query= "select * from registration where (Email=%s and Password=%s)"
        data=(em,passwd)
        mycur.execute(query,data)
        result=mycur.fetchone()

        
        if(result):
            print("---Log in successfully---")
            from profile1 import Profile
            prof=Profile()
            prof.calculate_age()
            
        else:
            print("Invalid login..Try again")
        

log=Login()






