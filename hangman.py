import time
name = input("What is your name? ")
print("")
time.sleep(1)
print("Start guessing...")
time.sleep(0.5)
word = 'mississipi'
guesses = ''
turns = 10
while turns > 0:         
    failed = 0             
    for char in word:      
        if char in guesses:    
            print( char,)    
        else:
            print ("_",)     
            failed += 1    
    if failed == 0:        
        print ("You won")
        if turns == 10:
            print("PERFECT!")
        break              
    print('')
    guess = input("guess a character:") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print ("Wrong")    
        print ("You have", + turns, 'more guesses')
        if turns == 0:           
            print ("You Lose")
