#!/usr/bin/env python
from subprocess import call
import math 
import time
import random 
import string

class Gameboard(object):
    def __init__(self):
        """  Constructor function for gameboard """

        self.hidden_characters = []
        self.game_board_array = [] 
        self.message = ""

        game_board = []
        game_board.append("             __________")
        game_board.append("            |          |")
        game_board.append("            |          |")
        game_board.append("            |          |")
        game_board.append("            |         ( )")
        game_board.append("            |         _|_") 
        game_board.append("            |        / | \\")
        game_board.append("            |          |  ")
        game_board.append("            |         / \\")
        game_board.append("            |       _/   \_")
        game_board.append("            |              ")
        game_board.append("            |             ")
        game_board.append("      ______|______       ")
    
        for line_number,line in enumerate(game_board):
            game_board_line = []
            for character_number,character in enumerate(line):
                game_board_line.append(character)
    
                if character != " ":
                    hidden_character = {}
                    hidden_character["position"] = [line_number,character_number]
                    hidden_character["character"] = character
                    self.hidden_characters.append(hidden_character)
                    game_board_line[character_number] = " "
    
            self.game_board_array.append(game_board_line)
        
        self.hidden_characters.sort(key = lambda character: \
                (math.atan2(-(15-character["position"][1]),(15-character["position"][0]))))


    def update(self,total_characters_to_add):
        """ Updates game board hidden characters based on
            ratio of wrong guesses to allowed guesses """

        for number in range(total_characters_to_add):
            position = self.hidden_characters[number]["position"]
            self.game_board_array[position[0]][position[1]] = \
                    self.hidden_characters[number]["character"]


    def __str__(self):
        """ Prints game board on fresh screen """
        
        call(["clear"])
        string = ""
        for game_board_line in self.game_board_array:
            string += "".join(game_board_line)
            string += "\n"
        string += self.message

        return string

class Word(object):
    def __init__(self, word):
        self.letter_list = []
        self.display_list = []
        
        for letter in word:
            self.letter_list.append(letter)
            self.display_list.append(False)

    
class Game(object):
    def __init__(self):
        """ Constructor function, all attributes empty"""
        
        self.possible_guesses = list(string.ascii_lowercase)
        self.wrong_guesses = []
        self.game_on = True
        self.board = Gameboard()

    
    def start_game(self):
        """ Starts game, establishes desired length and allowed_guesses"""
        
        call(["clear"])
        print("Welcome to hangman!")
        print("How long of a word to you want?")
        self.word_length = input("")
        self.word = Word(self.pick_word())

        print("How many guesses do you want?")
        self.allowed_guesses = input("")
        if self.allowed_guesses >= 26:
            print "There's only 26 letters in the alphabet..."


    def pick_word(self):
        """ Pick word from dictionary file of chosen length."""
        
        dictionary_file = "wordsEn.txt" #TODO: ensure file is in PWD

        with open(dictionary_file) as open_file:
            word_list = open_file.read().splitlines()
        
        if self.word_length > max(word_list):
            print("I don't have one that long...please pick a shorter word!")
            self.word_length = input("")

        possible_words = []
        tries = 0
        while not possible_words:
            starting_letter = random.choice(self.possible_guesses)
            for word in word_list:
                if word.startswith(starting_letter):
                    if len(word) == self.word_length:
                        possible_words.append(word)
            
            if tries > 5:
                print "I had a hard time finding a word, let me try again..."
                print("How long of a word to you want?")
                self.word_length = input("")
            tries += 1
        return random.choice(possible_words)


    def guess_letter(self):
        """ Prompts user to guess letter, 
            modifies the attributes and returns a message 
            based on whether its correct"""
        
        print "Guess a letter!"
        guessed_letter = raw_input("").strip().lower()
        self.possible_guesses = ["X" if letter == guessed_letter else letter for letter in self.possible_guesses]

        if guessed_letter not in self.word.letter_list:
            self.wrong_guesses.append(guessed_letter) 
            message = "You've guessed wrong"
        else:
            indices = [i for i, x in enumerate(self.word.letter_list) if x == guessed_letter] 
            for index in indices:
                self.word.display_list[index] = True
            message = "Great guess!"
        
        total_hidden_characters = len(self.board.hidden_characters)
        ratio = float(len(self.wrong_guesses))/float(self.allowed_guesses)
        total_characters_to_add = int(math.floor(total_hidden_characters*ratio)) 
            
        self.board.update(total_characters_to_add)
        
        return message
     

    def check_state(self):
        """ Checks the attributes to see if the game 
            should go on, returns a message """

        true_count = 0
        message = None
        for index,letter in enumerate(self.word.letter_list):
            if self.word.display_list[index]:
                true_count += 1
        if true_count == len(self.word.display_list):
            message = "Victory is yours!"
            self.game_on = False

        elif len(self.wrong_guesses) >= self.allowed_guesses:
            message = "Game Over."
            self.game_on = False
        return message
     

    def __str__(self):
        """ Prints possible letters and current word status """
        string = "\n Possible Letters: "
        letters_chosen = " "
        for letter in self.possible_guesses:
            letters_chosen += letter+" "
        string += "\n" + letters_chosen
        
        string += "\n Your word: \n"
        print_line = "  "
        for index,item in enumerate(self.word.letter_list):
            if self.word.display_list[index] or not self.game_on:
                print_line += item
            else:
                print_line += "_"
            print_line += " "
        string += print_line

        return string


if __name__ == "__main__":
    print "Would you like to play hangman? (y/n)"
    while True:
        choice = raw_input("")
        if choice.strip().lower() == "y":
            hangman = Game()
            hangman.start_game()
            message = "Let's get started!"
            while hangman.game_on:
                print hangman.board
                print hangman
                message = hangman.guess_letter()
                state_message = hangman.check_state()
                if state_message is not None:
                    hangman.board.message = state_message
                else:
                    hangman.board.message = message
            print hangman.board
            print hangman
            print "\nWould you like to play again? (y/n)"
        else:
            call(["clear"])
            break

