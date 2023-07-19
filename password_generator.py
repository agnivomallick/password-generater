import random as rand
import string as st

print("""
      [Tool Made By Agnivo Mallick[v1.0.0]]
      Hello!

      Welcome to Password Generator!

      This tool helps you to generate passwords.
      They are CRACKER-PROOF!
      You can use these passwords in your logins or signups.

      I hope you like the passwords!
    """)

word_list = {
    "adjectives": [
        "blue", "smelly", "sleepy", "tired", "sad", "fluffy",
        "purple", "proud", "orange", "fat", "thin", "unhappy",
        "wet", "dry", "brave", "hardworking", "irritating"
    ],
    "nouns": [
        "goat", "panda", "duck", "rat", "human", "hacker", "cracker", "mixer", "toaster",
        "frock", "dress", "mule", "donkey", "computer", "keyboard", "book", "cobbler",
        "table", "chair"
    ],
    "colors": [
        "red", "orange", "yellow", "blue", "green", "black", "grey", "brown",
        "blue"
    ],
} # all the words from which the password will be generated.

while True:
    adjective = rand.choice(word_list["adjectives"]) # one adjective
    noun = rand.choice(word_list["nouns"]) # one noun
    color = rand.choice(word_list["colors"]) #one color
    number = rand.randrange(0, 200) # any number between 0 and 200
    special_char = rand.choice(st.punctuation) # one special character

    finalPassword = adjective + noun + color + str(number) + special_char
    print("Here is your new password! %s" %finalPassword)

    isQuit = input("Do you want another password? Y or N:")

    if isQuit.lower() == "n":
        break