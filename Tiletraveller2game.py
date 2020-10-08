#def north(x, y)
#def south(x, y)
#def west(x, y)
    # Check if error?
#def east(x, y)

# Set x and y equal to 1 (start)
# Check which direction is available
    # If y > x you can move east?
    # If x is 1 then west is unavailable
    # If x is 3 then east is unavailable
    # If y is 1 then south is unavailable
    # If y is 3 then north is anavailable
# Prompt for a direction
# Error if wrong direction is called
# Call a function based on the input

# If you are in 3, 1 then print Victory
def north(x, y):
    if y==3:
        return False
    elif x == 2 and y == 2:
        return False
    else:
        return True 

def east(x, y):
    if y>x:
        return True
    else:
        return False

def south(x, y):
    if y == 1:
        return False
    elif x == 2 and y == 3:
        return False
    else: 
        return True

def west(x, y):
    if x != 1 and y >= x:
        return True
    else:
        return False 

def leaver_puller_one(tempo):
    if tempo == 0:
        pull_leaver = input("Pull a lever (y/n): ")
        if pull_leaver == "y" or "Y":
            return pull_leaver
        else:
            return pull_leaver


x = 1
y = 1
temp1 = 0
temp2 = 0 
temp3 = 0 
temp4 = 0
coin = 0

while True:
    print('You can travel: ', end='')
    n = north(x, y)
    e = east(x, y)
    s = south(x, y)
    w = west(x, y)
    
    if n == True and e == False and s == False and w == False:
        print('(N)orth', end='')
    if n == True and e == True and s == True and w == False:
        print('(N)orth or (E)ast or (S)outh', end='')
    if e == True and s == True and n == False and w == False:
        print('(E)ast or (S)outh', end='')
    if e == True and w == True and n == False and s == False:
        print('(E)ast or (W)est', end='')
    if s == True and w == True and n == False and e == False:
        print('(S)outh or (W)est', end='')
    if n == True and s == True and w == False and e == False:
        print('(N)orth or (S)outh', end='')   
     
    print('.', end='')
    print()
    direction = input('Direction: ')
    direction = direction.lower()
    if direction == 'n' or direction == 'e' or direction == 's' or direction == 'w':
        if direction == 'n' and n == True:
             y += 1
        elif direction == 'e' and e == True:
             x += 1 
        elif direction == 's' and s == True:
             y -= 1
        elif direction == 'w' and w == True:
             x -= 1
        else: 
            print('Not a valid direction!')

    else:
        print('Not a valid direction!')

    if x == 1 and y == 2:
        if temp1 == 0:
            asdfaq = leaver_puller_one(temp1) 
            if asdfaq == "y" or "Y":
                temp1 += 1
                coin += 1
                print(f"You recieved 1 coin, your total is now {coin}")
            else:
                temp += 1


    if x == 2 and y == 2:
        if temp2 == 0:
            asdfaq = leaver_puller_one(temp2) 
            if asdfaq == "y" or "Y":
                temp2 += 1
                coin += 1
                print(f"You recieved 1 coin, your total is now {coin}")
            else:
                temp2 += 1


    if x == 2 and y == 3:
        if temp3 == 0:
            asdfaq = leaver_puller_one(temp3) 
            if asdfaq == "y" or "Y":
                temp3 += 1
                coin += 1
                print(f"You recieved 1 coin, your total is now {coin}")
            else:
                temp3 += 1


    if x == 3 and y == 2:
        if temp4 == 0:
            asdfaq = leaver_puller_one(temp4) 
            if asdfaq == "y" or "Y":
                temp4 += 1
                coin += 1
                print(f"You recieved 1 coin, your total is now {coin}")
            else:
                temp4 += 1


                
    if x == 3 and y == 1:
        print(f"Victory! Total coins {coin}.")
        break
