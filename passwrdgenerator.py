# This program takes input from the user (a number between 4 and 8), then randomly generates a password using letters, numbers, and characters.

import random
import string
size = 1
while size < 4 or size > 8:
  passlen = input("Please choose a length for your password between 4 and 8 characters.")
  size = int(passlen)

x = 1
while x < (size + 1):
  char = string.ascii_letters + string.digits + string.punctuation
# The above took a little research work (Google, Stack Overflow) to discover how to include the different keyboard characters.
#    randpass = random.choice(char)
#    newPassword.append(randpass)
  newPassword = " ".join(random.choice(char))
  x+=1
  print(newPassword,end=' ')