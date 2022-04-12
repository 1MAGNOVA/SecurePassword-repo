""" this program, generates 3 sets of random alphanumeric characters and  verify if human"""


from ast import Break
import random
from re import X
from captcha.image import ImageCaptcha
import string
import time



Name = input("please enter your name here:")
print ("Welcome, " ,(Name))
time.sleep(2.0)
print("=======")
print("Please wait...")
time.sleep(2.0)
print("===========================")
print("Hi,", (Name),"Please type the letters as seen in the Captcha")


image = ImageCaptcha(width = 280, height = 90)
captcha_textChars = string.hexdigits
x = ( ''.join(random.choice(captcha_textChars) for i in range(8)) )
captcha_text = x

data = image.generate(captcha_text) 
image.write(captcha_text, 'CAPTCHA.png')
print("===========================")
print("===========================")
print("===========================")
P = input("Please type the letters as seen in the Captcha:")
if x == P:
    print("Nice to know you're human", (Name))
else:
    print("i'mn sorry, bots are not allowed, goodbye!")    
Break
print("===========================")
print("===========================")
print("===========================")
        
        

if x == P:
    def randPass():
            
        """"generate the three sets of passwords and concatenate them"""
        firstPartpass = string.ascii_lowercase
        p = (''.join(random.choice(firstPartpass) for i in range(8)) )

        secondPartpass = string.ascii_uppercase
        q = ( ''.join(random.choice(secondPartpass) for i in range(8)) )

        thirdPartpass = string.digits
        Partpass = string.ascii_uppercase
        r = ( ''.join(random.choice(thirdPartpass) for i in range(8)) )

        sumPass =  (p +'-'+ r +'-'+ q)
        return(sumPass)
    randPass()
print("your Safe password is", randPass())