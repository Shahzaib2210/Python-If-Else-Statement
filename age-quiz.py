'''
# Pesudo code
1 - Take user_age input from user
2 - Convert user_age input into interger and store in age variable.
3 - Apply check if age is greater than 100 then print "Sorry, you're dead."
4 - Apply check elif age is greater than equal to 40 then print "You're over the hill."
5 - Apply check elif age is equal to 21 then print "Congrats on your 21st!"
6 - Apply check elif age is less than equal to 13 then print "You qualify for the kiddie discount."
7 - else print "Age is but a number"
'''

# Taking age input from user.
user_age = input("Enter your age : ")
age = int(user_age) # converting age into int and storing into age variable.

if age > 100: # checking if age is greater than 100.
    print("Sorry, you're dead.")
elif age >= 65: # checking if age is greater than equal to 65.
    print("Enjoy your retirement!")
elif age >= 40: # checking if age is greater than equal to 40.
    print("You're over the hill.")
elif age == 21: # checking if age is equal to 21.
    print("Congrats on your 21st!")
elif age <= 13: # checking if age is less than equal to 65.
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number.")
          