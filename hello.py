print("Hello World!")
print(2+4)
print(6/2)
age=25
hobby="dancing"
description = "Her age is {} and she likes {}.".format(age,hobby)
print(description)
#Amy
count_description = description.count("is")
print(count_description)
print("The quick brown fox jumps over the lazy dog.".lower().count("the"))

# A comment, this is so you can read the program later.
# Anything after the # is ignored by Python.
print("I could have code like this.") # and the comment after is ignored.

# You can also use a comment to "disable" or comment out code:
# print("This won't run.")
print("This will run!")

print("What is your name?")
myname= raw_input()
print(myname)
print("Hello {}!".format(myname))


