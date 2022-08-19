website = "https://morsakademi.com"
course = "Python Kursu: Robotik Kodlama eğitmenliği dersleri (45 saat)"

print(len(course))

print(website[8:])

print(website[:19])

print(course[15:45])

print(course[::-1])

name, surname, age, job= "Burak", "Üstün", "25", "Eğitimci"

print("Benim adım " + name + " " + surname + "," + " Yaşım " + age + " ve mesleğim " + job)

print("Benim adım {} {}, Yaşım {} ve mesleğim {}" .format(name, surname, age, job))

print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}")

x = "Hello world"

print(x[:6] + "W" + x[7:])
#replace kullanarak yapılabilir

y = "abc"

print(f"{y}{y}{y}")