import datetime

from array_solution import create_field, choice_bombs,\
    setup_bombs, make_attack, find_neighbours, make_calculations


def play():
    name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    size = int(input("Enter Field Size (10 for a 10*10 field): "))
    num_of_bombs = int(input("Enter Number Of Bombs: "))

    field = create_field(size)
    bombs = choice_bombs(num_of_bombs, field.shape)
    field = setup_bombs(field, bombs)

    count_of_attacks = 0

    with open(f'{name}.txt', 'w') as file:
        file.write('\n')
        file.write(f'Game Time: {datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")}' + '\n')
        file.write(f'Field Size = {size} * {size}' + '\n')
        file.write(f'Number of Bombs = {num_of_bombs}')
        file.write('\n')
        file.write('\n')
        file.write('First Field Setup: ')
        file.writelines(str(field))

        while 'B' in field:
            attack = make_attack(field.shape, bombs)
            neighbours = find_neighbours(field.shape, attack)
            field = make_calculations(attack, neighbours, field)
            count_of_attacks += 1

            file.write('\n')
            file.write('-==-' * 10 + '\n')
            file.write('\n')
            file.write(f'Field After Attack Number {count_of_attacks}, Attack Position: {attack}')
            file.write('\n')
            file.writelines(str(field))

        file.write('\n')
        file.write('###' * 10 + '\n')
        file.write('\n')
        file.write('Final Result \n')
        file.writelines(str(field))
        file.write('\n')
        file.write('\n')
        file.write(f'Field Is Cleared After {count_of_attacks} Attacks')

        file.close()

    print(f'Field Is Cleared After {count_of_attacks} Attacks. To see the process open the file: {name}.txt')


if __name__ == "__main__":
    play()
