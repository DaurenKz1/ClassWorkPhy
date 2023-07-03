book = open("./book.txt", encoding="utf-8")
text = book.readlines()

def format_text(filename,max_lenght):
    with open(filename,encoding='utf-8') as myfile:
        lines = myfile.readlines()
    for line in lines:
        line = line.strip()
        words = line.split()
