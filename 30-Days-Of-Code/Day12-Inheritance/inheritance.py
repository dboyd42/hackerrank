#!/usr/bin/python3

class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        # Call the base class's __init__ method and pass the required *args
        Person.__init__(self, firstName, lastName, idNumber)
        # Initialize the __scores attribute
        self.__scores = scores

    def getScores(self):
        return self.__scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        average = int(sum(self.getScores())/len(self.getScores()))
        if 90 <= average <= 100:
            return 'O'
        elif 80 <= average < 90:
            return 'E'
        elif 70 <= average < 80:
            return 'A'
        elif 55 <= average < 70:
            return 'P'
        elif 40 <= average < 55:
            return 'D'
        else:
            return 'T'

