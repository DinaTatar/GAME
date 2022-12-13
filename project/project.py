from PIL import Image
import random

def readCorrectAnswers(filename='names.txt'):
    ans = {}

    with open(filename, 'r', encoding='utf-8') as f:
        for l in f.readlines():
            if l != "\n":
                words = l.split(';')
                ans[words[0]] = words[1][:-1]

    return ans


def play():
    true_ans = readCorrectAnswers()
    filenames = list(true_ans.keys())

    score = 0

    while True:
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
            break

    print(f'Вы набрали {score} очков')


play()
