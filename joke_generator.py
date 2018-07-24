
howmany = input("How many jokes would you like? ")

for i in range(0, howmany):
     base = i + 2
     joke = "There are 10 types of people in this world: "
     joke += "those who understand base {}, ".format(base)
     if base == 2:
        joke += "and those who don't."
     else:
        joke += "those who don't, "
     for n in range(2, base):
        if n == base - 1:
            joke += "and those who thought this was a joke about base {}.".format(n)
        else:
            joke += "those who thought this was a joke about base {}, ".format(n)

     print joke
