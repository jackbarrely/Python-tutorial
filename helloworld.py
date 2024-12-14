class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(w):
    print("Hello my name is " + w.name)

p1 = Person("John", 36)
p1.myfunc()
