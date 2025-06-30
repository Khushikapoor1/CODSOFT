import random
import string
def password_generator(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
     
    all = lower+upper+num+symbols
    password = [random.choice(upper),random.choice(lower),random.choice(num),random.choice(symbols)]
    password += random.choices(all,k=length)
    random.shuffle(password)
    return''.join(password)
length = int(input("Enter the desired password length:"))
print("Generated password:",password_generator(length))
    