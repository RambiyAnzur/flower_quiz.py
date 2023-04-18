
# Код программы Flower Quiz

import random

flowers = ['розы', 'тюльпаны', 'орхидеи', 'лилии', 'ирисы']
descriptions = {
    'розы': 'Цветок, символизирующий любовь и страсть',
    'тюльпаны': 'Цветок, символизирующий уважение и понимание',
    'орхидеи': 'Цветок, символизирующий красоту и изысканность',
    'лилии': 'Цветок, символизирующий чистоту и нежность',
    'ирисы': 'Цветок, символизирующий мудрость и верность'
}

def get_random_flower():
    # функция для получения случайного цветка и его описания
    flower = random.choice(flowers)
    description = descriptions[flower]
    return flower, description

flower, description = get_random_flower()

print(f"Угадайте, к какому виду цветка относится представленный цветок: {flower}")
answer = input()

if answer == flower:
    print("Правильно!")
else:
    print(f"Неверно. Правильный ответ: {flower}. {description}")
