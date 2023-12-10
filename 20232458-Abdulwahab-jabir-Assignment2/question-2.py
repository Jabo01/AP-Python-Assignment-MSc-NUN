class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"User Information: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")


user1 = User("Jabir", "Abdulwahab", 23, "jabir123@gmail.com")
user2 = User("Alamin", "lateef", 18, "alamin01@gmail.com")


user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Information: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user3 = User("Abubakar", "umar", 21, "abubakar123@gmail.com")


user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()


print(f"Login Attempts: {user3.login_attempts}")


user3.reset_login_attempts()


print(f"Login Attempts after reset: {user3.login_attempts}")

class Admin(User):
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges()

    def show_privileges(self):
        self.privileges.show_privileges()

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin_user = Admin("Steven", "okoroh", 19, "steven.okoroh@gmail.com")


admin_user.show_privileges()