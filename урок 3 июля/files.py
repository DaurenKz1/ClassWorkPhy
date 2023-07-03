book = open("./book.txt", encoding="utf-8")
text = book.readlines()
print(text)

word_to_replace = input("Введите слово, которое нужно заменить: ")
replacement_word = input("Введите слово, на которое нужно заменить: ")


for i in text:
    if word_to_replace.lower() in i:
     new_text = i.replace(word_to_replace.lower(),replacement_word.lower())


    elif word_to_replace.capitalize() in i:
     new_text = i.replace(word_to_replace.capitalize(),replacement_word.capitalize())

    elif word_to_replace.upper() in i:
     new_text = i.replace(word_to_replace.upper(),replacement_word.upper())

    print(new_text)


book.close()
