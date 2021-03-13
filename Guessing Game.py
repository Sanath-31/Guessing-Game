#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

num = random.randint(1,100)


# In[2]:


print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")


# In[3]:


guesses = [0]


# In[4]:


while True:
    guess = int(input("I'm thinking of a number between 1 to 100.\nWhat's your guess?"))
    
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
    
    break


# In[5]:


while True:

    guess = int(input("I'm thinking of a number between 1 to 100.\nWhat's your guess?"))
    
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
        
    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IN ONLY {len(guesses)} GUESSEs!')
        break
    
    guesses.append(guess)
    
    if guesses[-2]:  
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
   
    else:
        if abs(num-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')


# In[ ]:




