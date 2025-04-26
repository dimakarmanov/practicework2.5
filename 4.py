string = input("Введите строку: ")
if string.startswith("abc"):
    string = string.replace("abc", "www")
else:
    string = string + "zzz"
print(string)