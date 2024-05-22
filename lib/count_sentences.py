#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self._value = value


    @property
    def value(self):
        return self._value
    

    @value.setter
    def value(self, the_value):
        if (type(the_value) == str):
          self._value = the_value
        else:
          print("The value must be a string.")

   
    def is_punctuation(self, char):
       return self._value.endswith(char)
    def is_sentence(self):
        return self.is_punctuation(".")
    
    def is_question(self):
        return self.is_punctuation("?")
    
    def is_exclamation(self):
        return self.is_punctuation("!")
    
    def count_sentences(self):
        value = self.value
        for punctuation in ['!','?']:
          value = value.replace(punctuation, '.')
    
        sentences = [sentence for sentence in value.split('.') if sentence]
    
        return len(sentences)
