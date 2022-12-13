from PIL import Image
import random

def read_correct_answers(filename='names.txt'):
    ans = {}

    with open(filename, 'r', encoding='utf-8') as f:
        for l in f.readlines():
            if l != "\n":
                words = l.split(';')
                ans[words[0]] = words[1][:-1]

    return ans

user_name = input('Добро пожаловать в игру! Как вас зовут? ')
user_name = user_name[0].upper() + user_name[1:]

def play():
    true_ans = read_correct_answers()
    filenames = list(true_ans.keys())

    score = 0

    while True:

        consent = input(f'{user_name}, вы готовы начать? ')
        if consent.lower() == 'да':
            print('Хорошо, начинаем.')
        else:
            input('Вы готовы сейчас? ')
            continue

        filename = random.choice(filenames)
        with Image.open(filename) as im:
            im.show()
        user_ans = input('Как называется эта молекула? ')
        if user_ans.lower() == true_ans[filename]:
            score += 1
            key = input('Поздравляю! Если вам надоело играть, нажмите ноль. Если хотите продолжить игру, нажмите любую другую кнопку: ')
            if key == "0":
                break
        else:
            print(f'Спасибо за небезынтересную попытку ответа. На самом деле это {true_ans[filename]}')
            replay = input('Хотите сыграть еще раз? ')
            if replay.lower() == "да":
                print(f'Вы набрали {score} очков')
                score = 0
                continue
            break

    print(f'Вы набрали {score} очков.')

play()
