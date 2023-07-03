
def format_text(filename, max_line_length):
    # Открываем файл и читаем его содержимое
    with open(filename, 'r') as my_file:
        lines = my_file.readlines()

    formatted_lines = []
    for line in lines:

        line = line.strip()


        words = line.split()


        formatted_words = []
        current_line_length = 0

        for word in words:

            if current_line_length + len(word) + len(formatted_words) <= max_line_length:
                formatted_words.append(word)
                current_line_length += len(word)
            else:

                formatted_lines.append(' '.join(formatted_words))
                formatted_words = [word]
                current_line_length = len(word)


        formatted_lines.append(' '.join(formatted_words))


    formatted_text = ' '.join(formatted_lines)
    formatted_text = formatted_text.capitalize()

    return formatted_text


max_length = int(input("Введите максимальную длину строк: "))

formatted_text = format_text('task_2.txt', max_length)
