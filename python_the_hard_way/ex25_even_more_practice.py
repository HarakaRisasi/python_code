#_*_coding:utf-8_*_
''' Для запуска этой программы необходимо:
    1.В консоли ввести 'Python'
    2.Далее ввести >>> import name_of_prog
        !Имя программы не должно начинаться с цифры
'''
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words
#split - метод, который разбивает строку в список
#word = "Hello world !!"
#words = word.split(' ')
#
#'Hello' 'world' '!!'

def sort_words(words):
    """Sorts the words."""
    return sorted(words)
#sorted() - строки отсортированы по алфавиту, 
#           а числа отсортированы по номерам.

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word
    
#pop() - метод удаляет элемент в указанной позиции.

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and return the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

