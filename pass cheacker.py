"""Password strength checker"""
password=input(f"Enter Your Password :-")

score=0

if len(password)>=8:
    score+=1

if any(char.isupper() for char in password):
    score+=1

if any(char.islower() for char in password):
    score+=1

if any(char.isdigit() for char in password):
    score+=1

if any(char in "!@#$%^&*()-+" for char in password):
    score+=1

print("strength of your password is :-",score)


if score <= 2:
    print("Your password is weak.")
elif score == 5:
    print("Your password is medium.")
else:
    print("Your password is strong.")