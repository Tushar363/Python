# Implement a student Class with introduction such as roll no, name, class. The introduction must be entered by the user.
class Student:
  def getstudentDetails(self):
    self.rollno = int(input("Enter the Roll number: "))
    self.name = input("Enter your name: ")
    self.classofstudent = input("Enter your Class: ")
  def printResults(self):
      print(self.rollno)
      print(self.name)
      print(self.classofstudent)
S1 = Student()
S1.getstudentDetails()

print("Result: ")    
S1.printResults()    