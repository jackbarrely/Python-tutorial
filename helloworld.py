# class person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(person):
#   pass
# x = Student("Mike", "Olsen")
# x.printname()


class person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)

class Student(person):
  def __init__(self, fname, lname):
    person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()
