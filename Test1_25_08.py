
# coding: utf-8

# In[ ]:


class Cipher:
    S = input("Please enter the text to be encrypted:") #ask for user for a str & store it
    from random import randint
    key =randint(1,50)
    def encrypt (S,key):
        ciphertext = S+str(key)
        yield (ciphertext) #Concatenate Str & random integer
    
    def decrypt():
        d = list(ciphertext)
        for i in d:
            try:
                a=int(i)
            except ValueError:
                print(i,end="")
                continue
            print(a,end="")

