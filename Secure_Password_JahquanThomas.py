# This program will determine whether a password meets all the requirements for it being secure or not.

# The minimum password length is 8 characters.
min_pass = '01234567'

# The maximum password lenght is 10 characters.
max_pass = '0123456789'

# User will type in a secure password.
password = input('Enter your secure password: ')

# If the password is too short, notify user.
if (len(min_pass)) > (len(password)):
    print('Invalid password entry: Your password is too short. The minimum is 8 characters.')
# If the password is too long, notify user.
elif (len(max_pass)) < (len(password)):
    print('Invalid password entry: Your password is too long. The maximum is 10 characters.')

# Check the password to make sure quan is not used.
elif 'quan' in password.lower():
    print('Invalid password: quan shall not be used in password.')

# Check the password for $ to make sure it is not the first character.
elif password[0] == '$':
    print('Invalid password: $ shall not be used at the beginning of the password.')

# Check the password for $ to make sure it is not the last character.
elif password[-1] == '$':
    print('Invalid password: $ shall not be used at the end of the password.')

# Check the password for $ to make sure it used as any character in the password.
elif '$' not in password[1:-1]:
    print('Invalid password: $ is required to be utilized within password.')

# verify password length meets the minimum and maximum length requirements.
elif (len(min_pass)) <= (len(password)) and (len(max_pass)) >= (len(password)):
    print('Congratulations, you sucessfully entered a valid password.')
