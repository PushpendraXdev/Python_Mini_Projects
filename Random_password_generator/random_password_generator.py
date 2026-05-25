import random
import string

def generate_password():
    length=int(input("Enter thedesire password length: ").strip())
    print("answer in y/n\n")
    include_uppercase=input("Include upper case?: ").lower().strip()
    special_characters=input("Include special characters? ").lower().strip()
    include_digits=input("Include digit? ").lower().strip()


    if length<4:
        print("password must be grater than 4 characters")
        return
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase if include_uppercase =="y" else ""
    special=string.punctuation if special_characters =="y" else ""
    digits=string.digits if include_digits =="y" else ""

    all_characters=lower+upper+special+digits
    

    required_characters=[]
    if include_uppercase=="y":
        required_characters.append(random.choice(upper))
    if special_characters=="y":
        required_characters.append(random.choice(special))
    if include_digits=="y":
        required_characters.append(random.choice(digits))
    reamining_length=length-len(required_characters)
    password=required_characters

    for _ in range(reamining_length):
        character=random.choice(all_characters)
        password.append(character)
    random.shuffle(password)
    str_password="".join(password)
    print(str_password)


generate_password()
