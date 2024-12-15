#lesson2 #string #problem12
words_input = input("Введите слова, разделенные пробелами: ")
    
words_list = words_input.split()
    
separator = input("Введите разделитель: ")
    

def join_words(words, separator):
    return separator.join(words)

result = join_words(words_list, separator)
print("Результат:", result)