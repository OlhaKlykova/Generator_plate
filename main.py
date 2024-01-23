from random import randrange

def random_plate():
    # Генерация случайной длины номера от 6 до 8 символов
    plate_length = randrange(6, 8)
    plate = ""

    if plate_length == 6:
        # Генерация буквенных символов для первых трех позиций
        for i in range(min(plate_length, 3)):
            char_plate = chr(randrange(65, 91))
            plate += char_plate

        # Генерация цифровых символов для последних трех позиций
        for _ in range(plate_length - 3, plate_length):
            char_plate_num = str(randrange(0, 10))
            plate += char_plate_num

    elif plate_length == 7:
        # Генерация цифровых символов для первых четырех позиций
        for _ in range(min(plate_length, 4)):
            char_plate_num = str(randrange(0, 10))
            plate += char_plate_num

        # Генерация буквенных символов для последних трех позиций
        for _ in range(plate_length - 3, plate_length):
                char_plate = chr(randrange(65, 91))
                plate += char_plate

    return plate


def main():
    generated_plate = random_plate()
    print(generated_plate)


if __name__ == '__main__':
    main()