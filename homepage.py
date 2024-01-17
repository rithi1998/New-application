'''
Title              : Insurance Management System
Author             : Rithika S M
Created on         : 06/02/2023
Last Modified Date : 20/06/2023
Revised by         : Silpa M
Reviewed on        : 25/02/2023
'''
class home():
    def main(self):
        print("--------Welcome--------")
        print("1.New user 2.Registered user")
        x=int(input("Enter the number for navigation: "))
        if x==1:
            print("You will be directed to registration page")
            from registration import Register
            obj=Register
            obj.reg(self)
        elif x==2:
            print("You will be directed to login page...")
            from login import Login
            log=Login()
            log.login()
        else:
            print("Enter valid credentials")
r=home()
r.main()
from logout import Logout
out=Logout()
out.outside()
