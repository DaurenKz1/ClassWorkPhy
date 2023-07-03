book = open("./book.txt", encoding="utf-8")
text = book.read()
text_list = text.split("\n")
print(text_list)

word_to_replace = input("Введите слово, которое нужно заменить: ")
replacement_word = input("Введите слово, на которое нужно заменить: ")

new_text_list = []
for i in text_list:
    if word_to_replace.lower() in i:
     new_text = i.replace(word_to_replace.lower(),replacement_word.lower())


    if word_to_replace.title() in i:
     new_text = i.replace(word_to_replace.title(),replacement_word.title())

    if word_to_replace.upper() in i:
     new_text = i.replace(word_to_replace.upper(),replacement_word.upper())

    new_text_list.append(new_text)

final_text = "\n".join(new_text_list)

print(final_text)


book.close()
