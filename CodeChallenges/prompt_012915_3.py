import string

class Decoder():
    def __init__(self):
        self.alphabet = list(string.ascii_lowercase)
        # z = a, c = a, o = m
        self.scrambled_alphabet = self.scramble(list(string.ascii_lowercase),2)
        self.key = {}
        for index in range(26):
            self.key[self.scrambled_alphabet[index]] = self.alphabet[index]

    def scramble(self, input_list, times):
        for time in range(times):
            input_list.insert(0,input_list.pop())
        return input_list

    def decode(self, coded_message):
        message = ''
        for letter in coded_message:
            if letter in self.alphabet:
                message += self.key[letter]
            else:
                message += letter
        return message

