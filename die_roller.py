import random as rd

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
    

# Handles the addition of modifications to a roll
def mod_handler(user, mod):
    # Roll die with modifiers
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
    # Roll die with no modifiers
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

        

# Stimulate individual die rolls and record in list
def roll_record(side, times):
    L = []
    i = 0
    while i < times:
        L.append(rd.randint(1,side))
        i += 1
    return L


# Prints roll results
def result_display(results, side, mod, option):
    from datetime import datetime as dt
    print('   %s'%dt.now().strftime('%H:%M:%S'))
    if option == 1:
        print('         Roll a %d sided die' %(side))
        print('         Got: %d\n'% (results[0]))
    elif option == 2 and len(results)==1:
        print('         Roll a %d sided die mod %d' %(side,mod))
        print('             Got:', results[0])
        print('             Mod:', mod)
        print('         Total: %d\n' % (sum(results) + mod))
    else:
        if mod != 0:
            print('         Roll a %d sided die, %d times, mod %d' %(side, len(results), mod))
        else:
            print('         Roll a %d sided die, %d times' %(side, len(results)))
        print('             Got: ', end='')
        for item in results:
            print('%d ' %(item), end='')
        print("")
        if mod != 0:
            print('             Mod:', mod)
        else:
            pass
        print('         Total: %d\n' % (sum(results) + mod))
        

def mutiple_rolls(user):
    rolls = user.split(' ')
    for item in rolls:
        if item == '':
            rolls.remove(item)
    return rolls

def individual_roll(user):
    if user[0] == 'd':
        if '+' in user:
            mod_handler('1' + user, '+')
        elif '-' in user:
            mod_handler('1' + user, '-')
        else:
             mod_handler('1' + user, 0)
    elif '+' in user or '-' in user:
        if '+' in user and 'd' in user:
            mod_handler(user, '+')
        elif '-' in user and 'd' in user:
            mod_handler(user, '-')
        else:
            print_messages(int(2))
    else:
        mod_handler(user, 0)

# Handle user inputs using string parsing to trigger events     
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
            if ' ' in user:
                rolls = mutiple_rolls(user)
                for die in rolls:
                    individual_roll(die)
                print("   -------------------------")
            else:
                individual_roll(user)
                print("   -------------------------")
        elif 'c' in user:
            for i in range(50):
                print("")
        else:
            print_messages(int(2))
            

# Program's start function            
def program_IO():
    version = "v1.1"
    print("\n   Die Roller (%s)" %(version))
    print("   Directions: Enter 'q' to quit, 'h' for help. \n")
    user_input()
    

def main():
    # Calls on the program function to start
    program_IO()
        
main()