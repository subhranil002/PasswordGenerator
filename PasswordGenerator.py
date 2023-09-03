import random
import string


def getNewLetter():
    letters = string.ascii_letters
    return random.choice(letters)


def getNewNumber():
    digits = string.digits
    return random.choice(digits)


def getNewSpecialCharacter():
    special_characters = string.punctuation
    return random.choice(special_characters)


def checkPassword(password, number, special_character):
    if number and special_character:
        for char in password:
            if char.isalpha():
                hasLetter = True
            elif char.isdigit():
                hasNumber = True
            else:
                hasSpecialCharacter = True

        if hasLetter and hasNumber and hasSpecialCharacter:
            return True

    elif number:
        for char in password:
            if char.isalpha():
                hasLetter = True
            elif char.isdigit():
                hasNumber = True

        if hasLetter and hasNumber:
            return True

    elif special_character:
        for char in password:
            if char.isalpha():
                hasLetter = True
            elif not char.isalnum():
                hasSpecialCharacter = True

        if hasLetter and hasSpecialCharacter:
            return True


def passwordGenerator(min_length, number, special_character):
    password = ""

    if number and special_character:
        lettersAndNumbersAndSpecialCharacters = [
            getNewLetter(), getNewNumber(), getNewSpecialCharacter()]

        while True:
            while min_length > len(password):
                password += random.choice(lettersAndNumbersAndSpecialCharacters)

            checked = checkPassword(
                password, number, special_character)
            if checked:
                return password

    elif number:
        lettersAndNumbers = [getNewLetter(), getNewNumber()]

        while True:
            while min_length > len(password):
                password += random.choice(lettersAndNumbers)

            checked = checkPassword(
                password, number, special_character)
            if checked:
                return password

    elif special_character:
        lettersAndSpecialCharacters = [
            getNewLetter(), getNewSpecialCharacter()]

        while True:
            while min_length > len(password):
                password += random.choice(lettersAndSpecialCharacters)

            checked = checkPassword(
                password, number, special_character)
            if checked:
                return password

    else:
        while min_length > len(password):
            password += getNewLetter()

        return password


if __name__ == "__main__":
    min_length = int(
        input("Enter the minimum length of the password (6<=?) : "))
    use_number = input(
        "Do you want to have numbers in your password ? (y/n) : ") == "y"
    use_special_character = input(
        "Do you want to have special characters in your password ? (y/n) : ") == "y"

    if min_length < 6:
        print("Error: Minimum password length is 6 or greater.")
    else:
        password = passwordGenerator(
            min_length, use_number, use_special_character)
        print("Password:", password)
