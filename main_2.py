from random import randrange


def generator_letters(num_letters):
    return ''.join(chr(randrange(65, 91)) for _ in range(num_letters))


def generator_numbers(num_numbers):
    return ''.join(str(randrange(0, 10)) for _ in range(num_numbers))


def random_plate():
    # Генерация случайной длины номера от 6 до 7 символов
    plate_length = randrange(6, 8)
    plate = ""

    if plate_length == 6:
        plate += generator_letters(3)
        plate += generator_numbers(plate_length - 3)
    elif plate_length == 7:
        plate += generator_numbers(4)
        plate += generator_letters(plate_length -3)

    return plate


def main():
    generated_plate = random_plate()
    print(generated_plate)


if __name__ == '__main__':
    main()