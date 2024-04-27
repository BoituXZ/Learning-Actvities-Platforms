# So Day 1 of getting out of TUTORIAL HELL,  a simple calculator Sunday, 14 April

def Calculate():
    ctype = input("Would you like to add, subtract, multiply, divide, square or root a number?\n Enter (a) for add, (-) for subtraction, (x) for multiplication, (/) for division, (*) power and (r) for root\n")
    
# this part adds, which is pretty simple. Yayy :)
    if ctype == "+":
        Num_1 = int(input("Enter first number: "))
        Num_2 = int(input("Enter second number: "))
        Answer = Num_1 + Num_2
    
# this part is the subtraction  
    if ctype == "-":
        Num_1 = int(input("Enter first number: "))
        Num_2 = int(input("Enter second number: "))
        Answer = Num_1 - Num_2
        
        
# this part is the multiplication
    if ctype == "x":
        Num_1 = int(input("Enter first number: "))
        Num_2 = int(input("Enter second number: "))
        Answer = Num_1 * Num_2
        
        
# this part is the division
    if ctype == "/":
        Num_1 = int(input("Enter first number: "))
        Num_2 = int(input("Enter second number: "))
        Answer = Num_1 / Num_2
        
        
# this part is the squaring
    if ctype == "*":
        Num_1 = int(input("Enter number: "))
        Answer = Num_1 * Num_1
        
        
# this part is finding the root
    if ctype == "r":
        Num_1 = int(input("Enter number: "))
        temp = int(Num_1 / 2)
        Num_2 = 0
        Answer = "There is no exact root for this number!"
        while Num_2 in range(0, temp):
            if (Num_2 * Num_2) == Num_1:
                 Answer = Num_2
                 Num_2 += 1
            else:
                Num_2 += 1
    
    
    print("The answer is: ",Answer)
        
        
    
    
Calculate()