def greet(lang):
    if lang == "en":
        return"HI"
    elif lang == "es":
        return"Hello"
    else:
        return"Finish"
print(greet("en"), "Tarak")
print(greet("es"), "Leela")
print(greet("do"), "Code")
