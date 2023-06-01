def show_numbers(to_number):
    if to_number == 0:
        return
    print(to_number)
    show_numbers(to_number-1)

show_numbers(4)