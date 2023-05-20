# -*- coding: cp1251 -*-
import re
from colorama import init, Fore
import math
import datetime
import random
init(autoreset=True)

def printBot(text):
    print(Fore.RED + text)

def writetofile(text,filename):
    with open(filename, 'a') as file:
        file.write(text+"\n")

def point3d(f):
    x1=float(input("Введіть x1: "))
    y1=float(input("Введіть y1: "))
    z1=float(input("Введіть z1: "))
    x2=float(input("Введіть x2: "))
    y2=float(input("Введіть y2: "))
    z2=float(input("Введіть z2: "))
    return("Результат d="+str(math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)))

def arc():
    r=float(input("Введіть радіус кола: "))
    teta=float(input("Введіть кут між двома точками на колі: "))
    return("Результат L="+str(r*teta))

def point2d():
    x1=float(input("Введіть x1: "))
    y1=float(input("Введіть y1: "))
    x2=float(input("Введіть x2: "))
    y2=float(input("Введіть y2: "))
    return("Результат d="+str(math.sqrt((x2-x1)**2+(y2-y1)**2)))

def square():
    r=float(input("Введіть радіус кола: "))
    return("Результат S="+str(r*math.pi*math.pi))

def pi():
    return("Число П="+str(math.pi))

def point():
    x1=float(input("Введіть координату вектора x1: "))
    y1=float(input("Введіть координату вектора y1: "))
    x2=float(input("Введіть координату вектора x2: "))
    y2=float(input("Введіть координату вектора y2: "))
    t = ((x1 - x2) * (y2 - y1)) / ((y2 - y1) ** 2 + (x2 - x1) ** 2)
    x = x1 + t * (x2 - x1)
    y = y1 + t * (y2 - y1)
    return ('Координати точки перетину: ('+str(x)+','+str(y)+')')

def kulon():
    k=8.9875*(10**9)
    q1=float(input("Введіть q1: "))
    q2=float(input("Введіть q2: "))
    r=float(input("Введіть r: "))
    return ('Результат F='+str(k*q1*q2*r))

def boil():
    v1=float(input("Введіть q1: "))
    v2=float(input("Введіть q2: "))
    p2=float(input("Введіть r: "))
    return ('Результат P1='+str(p2*v2/v1))

def stala():
    return ("Кулонівська стала k=8.9875*10^9")

def ocean():
    return ("Найбільший за площею океан - тихий океан")

def area():
    return ("Найбільший за площею материк - Євразія")

def country():
    return ("Країна, в якій знаходиться найбільша пустеля після Сахари - Австралія")

def space():
    input_filename = input("Введіть ім'я вхідного файлу: ")
    output_filename = input("Введіть ім'я вихідного файлу: ")

    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        processed_content = ' '.join(content.split())

        with open(output_filename, 'w') as output_file:
            output_file.write(processed_content)

        return("Результат був записаний у файл "+output_filename)
    except FileNotFoundError:
        return("Помилка: Файл не знайдено.")
    except:
        return("Помилка: Виникла помилка при обробці файлу.")

def sentence():
    input_filename = input("Введіть ім'я вхідного файлу: ")

    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        sentences = re.split(r'[.!?]+', content)

        sentences = [sentence for sentence in sentences if sentence.strip()]

        sentence_count = len(sentences)
        return("Кількість речень у тексті: "+str(sentence_count))
    except FileNotFoundError:
        return("Помилка: Файл не знайдено.")
    except:
        return("Помилка: Виникла помилка при обробці файлу.")

def vowel():
    input_filename = input("Введіть ім'я вхідного файлу: ")

    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        words = re.findall(r'\b[AEIOUaeiou]\w+\b', content)

        if not words:
            return("У тексті немає слів, які починаються з голосної літери.")
        else:
            longest_words = []
            max_length = max(len(word) for word in words)

            for word in words:
                if len(word) == max_length:
                    longest_words.append(word)

            return("Найдовші слова, що починаються з голосної літери: "+str(longest_words))
    except FileNotFoundError:
        return("Помилка: Файл не знайдено.")
    except:
        return("Помилка: Виникла помилка при обробці файлу.")

def digit():
    input_filename = input("Введіть ім'я вхідного файлу: ")
    output_filename = input("Введіть ім'я вихідного файлу: ")

    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        processed_content = re.sub(r'\b\w*\d\w*\b', '', content)

        with open(output_filename, 'w') as output_file:
            output_file.write(processed_content)

        return("Результат був записаний у файл"+output_filename)
    except FileNotFoundError:
        return("Помилка: Файл не знайдено.")
    except:
        return("Помилка: Виникла помилка при обробці файлу.")

def year():
    current_year = datetime.datetime.now().year
    return ("Поточний рік - "+str(current_year))

def yeardays():
    year = int(input("Введіть рік: "))

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days = 366 
    else:
        days = 365  

    return("Кількість днів у році"+str(year)+"становить"+str(days)+"днів.")

def guess_number_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    printBot("Гра 'Вгадай число від 1 до 10'")
    printBot("Я загадав число. Спробуйте вгадати!")

    while True:
        guess = int(input("Введіть вашу догадку: "))
        attempts += 1

        if guess == number_to_guess:
            return("Вітаю! Ви вгадали число"+ str(number_to_guess)+"за"+ str(attempts)+ "спроб!")
        else:
            return("На жаль, ви не вгадали. Загадане число - "+str(number_to_guess))


def songs():
    favorite_songs = [
        "Буваю страшний, а насправді ж дитина\n"
        "Мабуть усе іще первісна людина\n"
        "Та головне ти зрозуміти повинна\n"
        "Поліна, я на колінах\n"
        "Я не люблю ні галасу, ані крику\n"
        "Коли не в свої справи люди пхнуть пику\n"
        "Це все пусте, одне ти знати повинна\n"
        "Поліна, я на колінах",

        "Не обіцяй назавжди\n"
        "Не обіцяй навічно\n"
        "Де твоє-моє завтра\n"
        "У скронях вітер свище.\n"
        "Не обіцяй, навіщо?\n"
        "Не обіцяй, не треба\n"
        "Залежить час найближчий\n"
        "Та не завжди від тебе.",

        "Зцапала, злапала, спутала\n"
        "Я взагалі не виступаю вдома\n"
        "Я сижу вяжу, хаваю бутери, граюся в шутери\n"
        "Я дівіді не вимикаю і за навастямі не слєжу.",

        "У тобі так багато сторін.\n"
        "Я просто не розумію,\n"
        "я просто хочу спитати тебе:\n"
        "чому ти настільки красива!?\n"
        "Чому в мене ціла купа дивних речей,\n"
        "яких я не розумію,\n"
        "яких я не відкриваю тобі,\n"
        "бо це все може вбити,\n"
        "Тебе це може вбити.",

        "Небо в твоїх очах вириває мій дах\n"
        "І кружляє по світу.\n"
        "Забивати на час, забивати на страх\n"
        "Я без тебе не вмію!"
    ]
    song_chorus = random.choice(favorite_songs)
    return ("Приспів однієї з улюблених пісень:\n"+song_chorus)


def joke():
    jokes = [
        "Боїшся стрибати з парашутом?\n– Так.\n– Стрибай без нього.",
        "Один хлопчик не вмів вимовляти слово шість. Прийшов якось одного разу в магазин і каже продавцеві:\n— Дайте мені сім пачок масла, одну не треба.",
        "Не розумію…\nЧому штани в яких краще вього лежати на дивані називаються спортивними???",
        "Вона:\n– Була в туалеті. У мене дві поділки…\nВін:\n– У мене в туалеті також поганий сигнал!",
        "Їздили вчора на екскурсію на хлібзавод. Тепер я не їм хліб. Сьогодні були на м’ясокомбінаті. Тепер я не їм м’ясо. Завтра екскурсія на лікеро-водочний. Я не їду."
    ]
    joke = random.choice(jokes)
    return ("Анекдот: \n"+joke)

def colors():
    return ("Кольори прапора України - синій та жовтий.")

def mountain():
    return ("Найбільша гора світу - Еверест.")

def lake():
    return ("Найбільше озеро світу - Каспійське море.")

def teror():
    return ("росія - держава терорист.")

class Bot:
    def __init__(self):
        self.f=''
        self.branch=''
        self.branches={
            'математика': {'Обчислення відстані між двома точками в просторі':point3d,
                           'Обчислення довжини дуги кола':arc,
                           'Обчислення довжини відрізка між двома точками на площині':point2d,
                           'Обчислення площі кола':square,
                           'Число П':pi,
                           'Обчислення точки перетину двох прямих':point},
            'фізика': {'Закон Кулона':kulon,
                       'Закон Бойля-Маріотта':boil,
                       'Кулонівська стала':stala},
            'географія': {'Найбільший за площею океан':ocean,
                          'Найбільший за площею материк':area,
                          'Країна, в якій знаходиться найбільша пустеля після Сахари':country},
            'робота з текстом': {'Вивести текст без зайвих пробілів':space,
                                 'Підрахувати кількість речень у тексті':sentence,
                                 'Знайти найдовші слова, які починаються з голосної літери':vowel,
                                 'Видалити з тексту всі слова, які містять цифри':digit},
            'загальна': {'Який зараз рік?':year,
                         'Обчислення днів у році':yeardays,
                         'Вгадай число між 1 та 10':guess_number_game,
                         'Улюблена пісня':songs,
                         'Анекдот':joke,
                         'Кольори прапора України':colors,
                         'Яка найвища гора у світі?':mountain,
                         'Яке найбільше озеро у світі?':lake,
                         'Яка найбільш терористична країна у світі?':teror}
        } 
    def start(self):
        while(1):
            printBot("Ви можете задати мені питання з наступних галузей: математика, фізика, географія, робота з текстом, загальна.")
            writetofile("Ви можете задати мені питання з наступних галузей: математика, фізика, географія, робота з текстом, загальна.",self.f)
            theme=input().lower()
            writetofile(theme,self.f)
            if theme.lower() == 'вихід':
                printBot("До побачення")
                writetofile("До побачення",self.f)
                exit()
            elif theme.lower() == 'допомога':
                printBot("Ви розпочали вибір галузі. Вам потрібно обрати її та слідувати наступним інструкціям. Спробуйте!\n")
                writetofile("Ви розпочали вибір галузі. Вам потрібно обрати її та слідувати наступним інструкціям. Спробуйте!\n",self.f)
            elif theme.lower() == 'назад':
                printBot("Нікуди повертатись. Це стартове меню. Для виходу напишіть вихід\n")
                writetofile("Нікуди повертатись. Це стартове меню. Для виходу напишіть вихід\n",self.f)
            else:         
                if theme in self.branches.keys():
                    self.branch=theme
                    break
                else:
                    printBot("Помилка, я не знаю цієї галузі! Спробуйте ще раз її ввести.")
                    writetofile("Помилка, я не знаю цієї галузі! Спробуйте ще раз її ввести.",self.f)
        self.themes()
    def hi(self):
        printBot("Привіт, мене звати Євгенія.")
        writetofile("Привіт, мене звати Євгенія.",self.f)
        self.start()
    def themes(self):
        while(1):
            printBot("\nВи обрали галузь <"+self.branch+">. Ви можете задати мені питання з наступних тем:")
            writetofile("\nВи обрали галузь <"+self.branch+">. Ви можете задати мені питання з наступних тем:",self.f)
            for text in self.branches[self.branch].keys():
                printBot("\t"+text)
                writetofile("\t"+text,self.f)
            theme=input()
            writetofile(theme,self.f)
            if theme.lower() == "вихід":
                printBot("До побачення\n")
                writetofile("До побачення\n",self.f)
                exit()
            elif theme.lower() == "допомога":
                printBot("Ви обрали галузь <"+self.branch+">. Вам потрібно обрати тему та слідувати наступним інструкціям. Вводьте тему чітко!\n")
                writetofile("Ви обрали галузь <"+self.branch+">. Вам потрібно обрати тему та слідувати наступним інструкціям. Вводьте тему чітко!\n",self.f)
            elif theme.lower() == "назад":
                self.start()
            else:         
                if theme in self.branches[self.branch].keys():
                    temp=self.branches[self.branch][theme]()
                    printBot(temp)
                    writetofile(temp,self.f)
                else:
                    printBot("Помилка, я не знаю цієї теми! Спробуйте ще раз її ввести.")
                    writetofile("Помилка, я не знаю цієї теми! Спробуйте ще раз її ввести.",self.f)


def main():
    b = datetime.datetime.now()
    date=b.strftime("%d-%m-%Y %H-%M-%S")

    bot=Bot() 
    bot.f='dialog-'+date+'.txt'
    bot.hi()

if __name__ == '__main__':
    main()


