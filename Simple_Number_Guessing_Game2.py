import random

tur = int(input("Welcome to the number guessing game. In this game the first player who guess a random number between 1 and 100 wins. How many rounds would you like to play??"))

puan1 = puan2 = 0

oyuncu1 = input("1st player's name: ")
oyuncu2 = input("2nd player's name: ")

for i in range(tur):
    print("Drawing the lots...")
    y= random.randint(1,2)
    
    if (y == 1):
        x1 = random.randint(1,100)
        print(oyuncu1, " is guessing: ")
        tahmin1 = int(input("Please enter your guess: "))
        sayi1 = 1
        
        while (tahmin1 != x1):
            if (tahmin1 > x1):
                print("Enter a smaller number: ")
                tahmin1 = int(input("Please enter your guess: "))
                sayi1 = sayi1 + 1
            else:
                print("Enter a larger number: ")
                tahmin1 = int(input("Please enter your guess: "))
                sayi1 = sayi1 + 1
                    
        print("Congratulations, correct number= ",tahmin1)
        print(sayi1," th time you got the right result.\n")
    
        
        
        x2 = random.randint(1,100)
        print(oyuncu2, " is guessing: ")
        tahmin2 = int(input("Please enter your guess: "))
        sayi2 = 1
        
        while (tahmin2 != x2):
            if (tahmin2 > x2):
                print("Enter a smaller number: ")
                tahmin2 = int(input("Please enter your guess: "))
                sayi2 = sayi2 + 1
            else:
                print("Enter a larger number: ")
                tahmin2 = int(input("Please enter your guess: "))
                sayi2 = sayi2 + 1
    
        print("Congratulations, correct number= ",tahmin2)
        print(sayi2," th time you got the right result.\n")
        
        
    
    
    else:
        x2 = random.randint(1,100)
        print(oyuncu2, " is guessing: ")
        tahmin2 = int(input("Please enter your guess: "))
        sayi2 = 1
        
        while (tahmin2 != x2):
            if (tahmin2 > x2):
                print("Enter a smaller number: ")
                tahmin2 = int(input("Please enter your guess: "))
                sayi2 = sayi2 + 1
            else:
                print("Enter a larger number: ")
                tahmin2 = int(input("Please enter your guess: "))
                sayi2 = sayi2 + 1
    
        print("Congratulations, correct number= ",tahmin2)
        print(sayi2," th time you got the right result.\n")
        
        
    
        x1 = random.randint(1,100)
        print(oyuncu1, " is guessing: ")
        tahmin1 = int(input("Please enter your guess: "))
        sayi1 = 1
        
        while (tahmin1 != x1):
            if (tahmin1 > x1):
                print("Enter a smaller number: ")
                tahmin1 = int(input("Please enter your guess: "))
                sayi1 = sayi1 + 1
            else:
                print("Enter a larger number: ")
                tahmin1 = int(input("Please enter your guess: "))
                sayi1 = sayi1 + 1
                    
        print("Congratulations, correct number= ",tahmin1)
        print(sayi1," th time you got the right result.\n")
        
        
    print(oyuncu1, sayi1," th time you got the right result.")
    print(oyuncu2, sayi2," th time you got the right result.")
    
    

    if(sayi1 < sayi2):
        print(oyuncu1," won")
        puan1 += 1
        print(oyuncu1, " has", puan1, " points.")
    if(sayi2 < sayi1):
        print(oyuncu2," won")
        puan2 += 1
        print(oyuncu2, " has", puan2, " points.")
    if(sayi1 == sayi2):
        print("Friendship won")
        puan1 += 1
        puan2 += 1
    
if puan1 > puan2:
    print(puan1,"-",puan2," ",oyuncu1," won")    
elif puan2 > puan1:
    print(puan2,"-",puan1," ",oyuncu2," won")    
elif puan1 == puan2:
    print(puan2,"-",puan1," equal scores. Friendship won!")
    