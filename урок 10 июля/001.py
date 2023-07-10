myfile = open('book.txt', 'w+', encoding='utf-8')
text = myfile.read(50)
myfile.write("Шерлок жив")
myfile.close()

print(text)