def reverse_string(string):
     words = string.split(' ') 
     reverse_sentence = ' '.join(reversed(words)) 
     return reverse_sentence 
if __name__ == "__main__": 
     input = 'Teja is Name My'
     print (reverse_string(input)) 