class Grade:
    def __init__(self, subject, score):
        self.subject = subject
        self.score = score

    def __str__(self):
        return f"Subject: {self.subject}, Score: {self.score}"

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.__password = None  # Private attribute for storing the user's password
        self.grades = []  # List to store grade objects

    def set_password(self, password):
        # TODO: Validation
        # Step 1: Create a requirement to set password length > 8
        # Print a warning if shorter

    def get_password(self):
        return "********" if self.__password else "Password not set"  # Get a masked password

    def login(self):
        print(f"{self.username} logged in")  # Simulate a user login action

    def view_grades(self):
        print(f"Grades for {self.username}:")
        for grade in self.grades:
            print(grade)  # Display user's grades

    def __str__(self):
        return f"User: {self.username}, Email: {self.email}"  # Represent the user as a string

class Admin(User):
    def __init__(self, username, email):
        super().__init__(username, email)
        self.is_admin = True  # Admins are marked as admins

    def change_grade(self, user, subject, new_score):
        if user in self.grades:  # Check if the admin is allowed to change grades for this user
            for grade in user.grades:
                if grade.subject == subject:
                    grade.score = new_score  # Update the grade
                    print(f"Admin {self.username} changed {user.username}'s grade in {subject} to {new_score}")
                    return
            print(f"Subject {subject} not found in {user.username}'s grades.")
        else:
            print(f"Admins cannot change grades for {user.username}.")

    def delete_user(self, user):
        # TODO
        # Step 1: Check if user is admin
        # Only allow admins to delete users (not other admins)
        

    def admin_function(self):
        print(f"Admin {self.username} performed an admin-only function.")

# Creating objects
user1 = User("alice", "alice@example.com")
user2 = User("bob", "bob@example.com")

admin1 = Admin("teacher1", "teacher@example.com")
admin2 = Admin("teacher2", "teacher2@example.com")

# Setting passwords
user1.set_password("password123")
user2.set_password("securepass")

# Creating grade objects for users
user1.grades.append(Grade("Math", 90))
user1.grades.append(Grade("Science", 85))
user2.grades.append(Grade("Math", 78))
user2.grades.append(Grade("Science", 92))

# Logging in
user1.login()
admin1.login()

# Accessing attributes and methods
print(f"{user1.username}'s password: {user1.get_password()}")
print(f"{user2.username}'s password: {user2.get_password()}")

# Abstraction
print(user1)
print(admin1)

# Viewing grades
user1.view_grades()
user2.view_grades()

# Admin changes a grade
admin1.change_grade(user1, "Math", 95)
user1.view_grades()  # Verify the grade change

admin1.change_grade(user2, "History", 88)  # Attempt to change a non-existing subject

admin1.change_grade(user2, "Math", 85)  # Attempt to change a grade for a non-admin user

# Admin deletes a user
admin1.delete_user(user2)

# Admin-only function
admin1.admin_function()

# Admins cannot delete other admins
admin1.delete_user(admin2)
