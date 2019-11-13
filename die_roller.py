
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


def result_display(results, side, mod):
    if mod == 0:
        total = sum(results)
        print('         %d sided die, %d time(s)' %(side, len(results)))
        print('         Your row(s) are',results,'for a total of %d\n' %(total))
    else:
        total = sum(results) + mod
        print('         %d sided die, %d time(s), mod %d.' %(side, len(results), mod))
        print('         Your row(s) are',results,'with mod %d for a total of %d\n' %(mod,total))

        
def user_input():
    valid_input = False
    while valid_input == False:
        user = input('   Roll: ')
        if user == 'q':
            print('\n   Program Terminated.\n')
            return
        elif 'd' in user:
            if '+' in user or '-' in user:
                if '+' in user:
                    if len(user.split('+'))<3:
                        mod_split = user.split('+')
                        L = mod_split[0].split('d')
                        times = L[0]
                        side = L[1]
                        M = user.split('+')
                        mod = M[1]
                        try:
                            times = int(times)
                            side = int(side)
                            mod = int(mod)
                            results = roll_record(side,times) #number of intervals, digits per interval
                            result_display(results, side, mod)
                        except ValueError:
                            print("   Error in input.")
                    else:
                        print("   Error in input")
                elif '-' in user:
                    if len(user.split('-'))<3:
                        mod_split = user.split('-')
                        L = mod_split[0].split('d')
                        times = L[0]
                        side = L[1]
                        M = user.split('-')
                        mod = M[1]
                        try:
                            times = int(times)
                            side = int(side)
                            mod = 0-int(mod)
                            results = roll_record(side,times) #number of intervals, digits per interval
                            result_display(results, side, mod)
                        except ValueError:
                            print("   Error in input")
                    else:
                        print("   Error in input")
                else:
                    print("   Error in input")
                
            else:
                L = user.split('d')
                times = L[0]
                side = L[1]
                mod = 0
                try:
                    times = int(times)
                    side = int(side)
                    results = roll_record(side,times) #number of intervals, digits per interval
                    result_display(results, side, mod)
                except ValueError:
                    print("    Please input (#of times rolled)d(#of dice sides) or 'q' to quit.")
        else:
            print("     Please input (#of times rolled)d(#of dice sides) or 'q' to quit.")
            valid_input == False

            
def program_IO():
    print("\n   Die Roller (v1.0)")
    print("   Directions: Enter #d# to roll.\n   EXAMPLE: 4d6 Rolls a 6 SIDED die 4 TIMES.\n")
    user_input()
    

def main():
    program_IO()
        
main()