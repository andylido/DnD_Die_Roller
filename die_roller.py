def roll_die(side):
    import random
    return random.randint(1,side)

def roll_record(side, times):
    L = []
    i = 0
    while i < times:
        L.append(roll_die(side))
        i += 1
    return L


def user_input():
    cont = False
    while cont == False:
        y = input("Number of rolls: ")
        x = input("Number of sides: ")

        try:
            x = int(x)
            y = int(y)
            cont = True
        except ValueError:
            print("Error. Input must be integers.\n")
            
    results = roll_record(x,y) #number of intervals, digits per interval
    print(results)

def program_IO():
    user_input()
    

def main():
    print("\nDie Roller v1.0\n")
    
    program_IO()
        
    
    
main()