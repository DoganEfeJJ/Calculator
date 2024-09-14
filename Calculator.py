#Calculator

print("Welcome to Calculator")

num1 = int(input("Please write your first number: "))
num2 = int(input("Please write your second number: "))

islem = input("+,-,*,/: ")

toplam = num1 + num2
cikarma = num1 - num2
carpma = num1 * num2
bolme = num1 / num2

if islem == '+':
          print(f"İşleminizin Sonucu: {toplam}")

elif islem == '-':
        print(f"İşleminizin Sonucu: {cikarma}")

elif islem == '*':
        print(f"İşleminizin Sonucu: {carpma}")

elif islem == '/':
    print(f"İşleminizin Sonucu: {bolme}")

else:
    print("Geçersiz İşlem")
