# pris = 89
# lunch = "ärtsoppa"

# if not(pris != 100 and lunch != "ärtsoppa"):
#     print("Sant")
# else:
#     print("Falskt")

# Övning 1

# # Example 1
# print("ex 1 --------")
# input()
# x = 0.0
# flag = True
# while x != 1.0:
#     print(x)
#     x += 0.1
#     flag= False
#     if x > 2:
#         break

# # Example 2
# print("ex 2 --------")
# input()
# x = 0.0
# while x - 1.0 > 0.0001:
#     print(x)
#     x += 0.1
#     if x > 2:
#         break

# # Example 3
# print("ex 3 --------")
# input()
# x = 0.0
# while abs(1.0 - x) > 0.0001:
#     print(x)
#     x += 0.1
#     if x > 2:
#         break

# print(x)
# # a = 20


# def instruktioner():
#     #Rovkvalser används för att bekämpa spinn      
#     #Skriver ut instruktioner för rovkvalster.
#     a = 10
#     print(a)
#     input()
#     return a, b, ertyu, b



# b, h, o, p = instruktioner()
# print(a)
# print(b)


# def elliot(a, b, c):
#     b *= c      # 4 * 6 = 24
#     a **= b     # 2 ** 24 = 
#     return a



# def main():
#     redsultat = elliot(2,4,6)
#     print(redsultat)
#     g = 1+2
#     print(g)

# main()


# Övning 2

# s = ""
# a = "1112031584"
# for i in range(1, len(a)):
#     if int(a[i]) % 2 == int(a[i - 1]) % 2:
#         s += max(a[i], a[i - 1])
# print("www.multisoft.se/" + s)


# s = ""
# a = [3, 8, 5, 1, 8, 5, 3, 2, 7]
# i = 0

# while i < len(a):
#     if a[i] % 2 != 0:
#         s += str(a[i]) + str(a[a[i]])
#         i += 2
#     else:
#         i -= 1

# print("www.multisoft.se/" + s)



# def rekursiv(x):
#     x = x+1
#     if x == 10:
#         return x
#     else:
# #         return rekursiv(x)
    

# # tal = rekursiv(0)
# # print(tal)

# # listA = [1,2,3]
# # listA.extend()


# # s = "   Hejsan Är Du Snäll Idag?   "
# # print(s.islower())
# # print(s.lower())
# # print(s.split(" "))
# # print(s.strip("a"))
# # print(s.replace("a",''))

# # listA = [1,2,3,2,2,2,2,2,2,2,2,2]
# # listA.clear()
# # print(listA)
# # listb =[]

# # dictb ={}


# # listyuio = [1,2,3,4,5,6]
# # listrätt = []

# # for num in listyuio:
# #     if num % 2 == 1:
# #         listrätt.append(num)
# # for num in listyuio:
# #     if num % 2 == 0:
# #         listrätt.append(num)

# # print(listyuio)
# # print(listrätt)


# # Övning 3

# class Konto:
#     def __init__(self, namn, pengar, kontonummer):
#         self.namn = namn
#         self.pengar = pengar
#         self.kontonummer = kontonummer
#         self.pin = "1234"

#     def __str__(self):
#         return self.namn + " har " + str(self.pengar) + " på sitt konto"
    
#     def uttag(self, uttag):
#         kod = input("Ge pin")
#         if kod != self.pin:
#             print("aja baja")
#         else:
#             if self.pengar >= uttag:
#                 self.pengar = self.pengar-uttag
#             else:
#                 print("du saknar cash")



# mittKonto = Konto("Linda", 100000, 23456789)
# print(mittKonto)
# dittKonto = Konto("alBrekt", 14, 567890)
# print(dittKonto)
# dittKonto.uttag(2000)
# print(dittKonto)


class Aklass:
    def __init__(self):
        self.b = 84.194567890
        self.c = 0.067
    
    def __str__(self):
        return "b är " + str(self.b) + " och c är " + str(self.c)

objekt = Aklass()
print(objekt)
print(objekt.b)