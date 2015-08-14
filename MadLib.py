__author__ = 'AKing'
# Create MadLibs from user input

from MadLibRandomText import MadLibRandomText

def main():
    randomized_text = MadLibRandomText()
    prompt_words = ["Verb", "Noun", "Pronoun", "Adjective", "Verb", "Noun", "Pronoun", "Adjective", "Adjective", "Verb", "Noun", "Noun"]
    response_words = []
    your_name = input("Enter your name to begin creating fun mad libs otherwise, enter Z to quit. ")
    if your_name.strip().upper() != "Z":
        for i in prompt_words:
            temp = input("Please enter a " + i + ": ")
            response_words.append(temp)

        print(randomized_text.get_random_txt(response_words))
        print("Thanks:", your_name)
        print("We hope you had fun making a unique mad lib!")
        return response_words
    else:
        print("Come back soon!")

main()