name = input("enter a name: ")
interest = input("What are you passionate about?: ")

message = f"Hi, I'm {name} and I am passionate about {interest}"
print(message)

file_path = r"G:\Mi unidad\Python\100DaysOfCode\Mes1\Semana1\proyectos\fin de semana 1\message.txt"
with open(file_path, "w", encoding="utf-8") as archive:
    archive.write(message)