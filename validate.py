import re
class Validate:
    def checkmail(self,email):
        regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex,email)):
            print("Valid mail")
        else:
            print("Invalid mail")
            from registration import Register
            obj=Register()
            obj.reg()

    def validpass(self,password):
        sys=['#','@','&','$']
        if len(password)<6:
            print("Password should be atleast 6 in length")
            from registration import Register
            obj=Register()
            obj.reg()
            
        elif len(password)>18:
            print("Password should be maximum of 18 in length")
            from registration import Register
            obj=Register()
            obj.reg()
            
        elif not any(char.isdigit() for char in password):
            print("Password should have atleast one numerals")
            from registration import Register
            obj=Register()
            obj.reg()
            
        elif not any(char.isupper() for char in password):
            print("Password should have atleast one uppercase letter")
            from registration import Register
            obj=Register()
            obj.reg()
            
        elif not any(char.islower() for char in password):
            print("Password should have atleast one lowercase letter")
            from registration import Register
            obj=Register()
            obj.reg()
            
        elif not any(char in sys for char in password):
            print("Password should have atleast one special case letter")
            from registration import Register
            obj=Register()
            obj.reg()
    
        else:
            print("Valid password")

val=Validate()


