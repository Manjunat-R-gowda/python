class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  

    def check_password(self, password):
        return self.__password == password

    def change_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.__password = new_password
            print("Password changed successfully")
        else:
            print("Wrong old password")
            
  
user = UserAccount("manju123", "abc@123")

print(user.check_password("abc@123"))
user.change_password("abc@123", "new@456")


class student:
	def __init__ (self,name,marks):
		self.name=name
		self.__marks=marks
	def exam(self):
		return self.__marks
		
	
u=student("manjunath",10)
print(u.name)