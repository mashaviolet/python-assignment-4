# Object Orientated Programming
# It has Classes and Objects

#  syntax
# creating a class:
# a class name start with a capital letter and its singular

# Cohort class
# class Cohort:
# name
#description
#start date
#end date
# add a constructor for the cohort class
# create a function/ add a method to the class that prints the cohort name and the total number of students
# create a new instance/ object of the cohort class 
class Cohort:
    def __init__(self, name, description, start_date, end_date, students):
        # Constructor to initialize the cohort's attributes
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.students = students  # List of students in the cohort

    def print_details(self):
        # Method to print the cohort name and the total number of students
        print(f"Cohort Name: {self.name}")
        print(f"Total number of students: {len(self.students)}")


# Create a new instance (object) of the Cohort class
cohort1 = Cohort(
    name="Data Science Cohort 2024", 
    description="A comprehensive data science program.", 
    start_date="2024-01-10", 
    end_date="2024-12-15", 
    students=["Alice", "Bob", "Charlie", "Diana"]  # List of student names
)

# Call the method to print cohort details
cohort1.print_details()
