course = "Python Kursu: Robotik Kodlama eğitmenliği dersleri (45 saat)"
website = "https://www.morsakademi.com"


# 1 - "course" karakter sayısını alın.
print(len(course))


# 2 - "website" içinden www karakterlerini alın.
print(website[8:11])


# 3 -  "website" içinden com karakterlerini alın.
print(website[-3:])


# 4 - "course" içinden ilk 15 ve son 15 karakterlerini alın.
print(course[0:15])
print(course[-15:])


# 5 - "course" ifadesindeki karakterleri tersten yazdırın.
print(course[::-1])


name = "Burak"
surname = "Üstün"
age = 25
job = "Eğitimci"

# 6 - Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    "Benim adım Burak Üstün, Yaşım 25 ve mesleğim Eğitimci" (3 farklı yöntemler) 

# 1. Yöntem
print("Benim adım " + name + " " + surname + "," + " " + "Yaşım " + str(age) + " " + "ve mesleğim " + job)

# 2. Yöntem
print("Benim adım {} {}, Yaşım {} ve mesleğim {}".format(name, surname, age, job))

# 3. Yöntem
print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}")

# 7 - "Hello world" ifadesindeki "w" harfini "W" ile değiştirin.
cumle = "Hello world"
print(cumle.replace("w", "W"))


# 8 - "abc" ifadesini yan yana 3 defa yazdırın.
print("abc"*3)

# veya

kelime = "abc"
print(kelime*3)