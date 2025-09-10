dict = {"Alice":20 , "Aayushi":100 , "Madhur":99}
name=input("Enter student name: ")
try:
    print(f"{name}'s marks: {dict[name]}")
except KeyError:
    print("Student not found")

    