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

def result_display(results, side):
    total = sum(results)
    print('   Roll a %d sided die, %d times.' %(side, len(results)))
    print('\n   Your rows are',results,'for a total of %d\n' %(total))
    

def user_input():
    valid_input = False
    while valid_input == False:
        user = input('\n   Roll: ')
        if 'd' in user:
            L = user.split('d')
            times = L[0]
            side = L[1]

            if '+' in user or '-' in user:
                if '+' in user:
                    M = user.split('+')
                elif '-' in user:
                    M = user.split('-')
                else:
                    print('Error Detected.\n')
                
            else:
                try:
                    times = int(times)
                    side = int(side)
                    valid_input = True
                except ValueError:
                    print("   Error. Input must be integers.\n")
        else:
            print('\n   Please input (#of times rolled)d(#of dice sides). \n')
            valid_input == False
            
    results = roll_record(side,times) #number of intervals, digits per interval
    result_display(results, side)

def program_IO():
    print("\n   Die Roller (v1.0)")
    print("   Directions: Enter #d# to roll.\n   EXAMPLE: 4d6 Rolls a 6 SIDED die 4 TIMES.\n")
    user_input()
    

def main():
    program_IO()
        
main()