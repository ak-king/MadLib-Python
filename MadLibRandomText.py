__author__ = 'AKing'


import random
import os.path
NUMBER_OF_PROMPTS = 12
class MadLibRandomText:

    def __init__(self):
        self.__rand_txt = random.randint(0, 2)
        # Generate a random int between 0-2 for to choose text file

    def get_random_txt(self, input_words):

        mad_lib_file = "madLib" + str(self.__rand_txt) + ".txt"
        if os.path.isfile(str(mad_lib_file)):
            mad_lib_file = open("madLib" + str(self.__rand_txt) + ".txt", "r")
            mad_lib_text = mad_lib_file.read()
            for i in range(0, NUMBER_OF_PROMPTS):
                mad_lib_text = mad_lib_text.replace("*" + str(i) + " ", input_words[i])

        else:
            mad_lib_text = "Your MadLib text has vanished!"

        return mad_lib_text
