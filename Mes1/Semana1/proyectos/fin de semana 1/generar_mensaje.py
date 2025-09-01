name = input("enter a name: ")
interest = input("What are you passionate about?: ")

message = f"Hi, I'm {name} and I am passionate about {interest}"
print(message)
with open("message.txt", "w") as archive:
    archive.write(message)