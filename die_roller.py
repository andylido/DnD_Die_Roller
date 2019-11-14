# Prints a message to the user
def print_messages(option):
    if option == 1:
        print("\n   Example Uses:")
        print("   --------------------------------------------------------------")
        print("   4d6             Rolls a 6 SIDED die 4 TIMES.")
        print("   4d6+2 OR 4d6-2  Rolls a 6 SIDED die 4 TIMES +/- the modifier")
        print("   d20             Rolls a 20 SIDED die ONCE")
        print("   d20+2 OR d20-2  Rolls a 20 SIDED die ONCE +/- the modifier\n")
    elif option == 2:
        print("    Input Error. Enter #d# to roll, 'q' to quit, 'h' for help.\n")
    elif option ==3:
        print("   Error in input.\n")
    else:
        pass
    

# Handles the addition of modifications in a roll
def mod_handler(user, mod):
    if mod != 0:
        if len(user.split(mod))<3:
            L = user.split(mod)[0].split('d')
            times = L[0]
            side = L[1]
            m = user.split(mod)[1]
            try:
                times = int(times)
                side = int(side)
                if mod != '+':
                    m = 0-int(m)
                else:
                    m = int(m)
                results = roll_record(side,times)
                result_display(results, side, m, 2)
            except ValueError:
                print_messages(int(3))
    else:
        L = user.split('d')
        times = L[0]
        side = L[1]
        m = 0
        try:
            times = int(times)
            side = int(side)
            results = roll_record(side,times)
            if times == 1: 
                opt = 1
            else: 
                opt = 2
            result_display(results, side, m, opt)
        except ValueError:
            print_messages(int(2))

        

# Stimulates individual die rolls based sides    
# Records the result of each roll in a list
def roll_record(side, times):
    import random as rd
    L = []
    i = 0
    while i < times:
        L.append(rd.randint(1,side))
        i += 1
    return L


# Prints the results of the rolls to the user
def result_display(results, side, mod, option):
    if mod == 1:
        total = sum(results)
        print('         %d sided die,' %(side))
        print('         Your roll is',results)
    else:
        total = sum(results) + mod
        print('         %d sided die, %d time(s), mod %d.' %(side, len(results), mod))
        print('         Your roll(s) are',results,'with mod %d for a total of %d\n' %(mod,total))
        

# Handles user's inputs using string parsing to trigger events       
def user_input():
    terminate = False
    # While Loop for infinite inputs until terminate condition
    while terminate == False:
        user = input('   Roll: ')
        if user == 'q':
            print('\n   Program Terminated.\n')
            return
        elif user =='h':
            print_messages(int(1))
        # user input has 'd' in it, indicating roll call
        elif 'd' in user:
            if user[0] == 'd':
                if '+' in user:
                    mod_handler('1' + user, '+')
                elif '-' in user:
                    mod_handler('1' + user, '-')
                else:
                    mod_handler('1' + user, 0)
            elif '+' in user or '-' in user:
                if '+' in user:
                    mod_handler(user, '+')
                elif '-' in user:
                    mod_handler(user, '-')    
            else:
                mod_handler(user, 0)
        else:
            print_messages(int(2))
            

# The Program's start function            
def program_IO():
    version = "v1.0"
    print("\n   Die Roller (%s)" %(version))
    print("   Directions: Enter 'q' to quit, 'h' for help. \n")
    user_input()
    

def main():
    # Calls on the program function to start
    program_IO()
        
main()