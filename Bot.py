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
    x1=float(input("������ x1: "))
    y1=float(input("������ y1: "))
    z1=float(input("������ z1: "))
    x2=float(input("������ x2: "))
    y2=float(input("������ y2: "))
    z2=float(input("������ z2: "))
    return("��������� d="+str(math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)))

def arc():
    r=float(input("������ ����� ����: "))
    teta=float(input("������ ��� �� ����� ������� �� ���: "))
    return("��������� L="+str(r*teta))

def point2d():
    x1=float(input("������ x1: "))
    y1=float(input("������ y1: "))
    x2=float(input("������ x2: "))
    y2=float(input("������ y2: "))
    return("��������� d="+str(math.sqrt((x2-x1)**2+(y2-y1)**2)))

def square():
    r=float(input("������ ����� ����: "))
    return("��������� S="+str(r*math.pi*math.pi))

def pi():
    return("����� �="+str(math.pi))

def point():
    x1=float(input("������ ���������� ������� x1: "))
    y1=float(input("������ ���������� ������� y1: "))
    x2=float(input("������ ���������� ������� x2: "))
    y2=float(input("������ ���������� ������� y2: "))
    t = ((x1 - x2) * (y2 - y1)) / ((y2 - y1) ** 2 + (x2 - x1) ** 2)
    x = x1 + t * (x2 - x1)
    y = y1 + t * (y2 - y1)
    return ('���������� ����� ��������: ('+str(x)+','+str(y)+')')

def kulon():
    k=8.9875*(10**9)
    q1=float(input("������ q1: "))
    q2=float(input("������ q2: "))
    r=float(input("������ r: "))
    return ('��������� F='+str(k*q1*q2*r))

def boil():
    v1=float(input("������ q1: "))
    v2=float(input("������ q2: "))
    p2=float(input("������ r: "))
    return ('��������� P1='+str(p2*v2/v1))

def stala():
    return ("���������� ����� k=8.9875*10^9")

def ocean():
    return ("��������� �� ������ ����� - ����� �����")

def area():
    return ("��������� �� ������ ������� - ������")

def country():
    return ("�����, � ��� ����������� �������� ������� ���� ������ - ��������")

def space():
    input_filename = input("������ ��'� �������� �����: ")
    output_filename = input("������ ��'� ��������� �����: ")

    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        processed_content = ' '.join(content.split())

        with open(output_filename, 'w') as output_file:
            output_file.write(processed_content)

        return("��������� ��� ��������� � ���� "+output_filename)
    except FileNotFoundError:
        return("�������: ���� �� ��������.")
    except:
        return("�������: ������� ������� ��� ������� �����.")

def sentence():
    input_filename = input("������ ��'� �������� �����: ")

    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        sentences = re.split(r'[.!?]+', content)

        sentences = [sentence for sentence in sentences if sentence.strip()]

        sentence_count = len(sentences)
        return("ʳ������ ������ � �����: "+str(sentence_count))
    except FileNotFoundError:
        return("�������: ���� �� ��������.")
    except:
        return("�������: ������� ������� ��� ������� �����.")

def vowel():
    input_filename = input("������ ��'� �������� �����: ")

    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        words = re.findall(r'\b[AEIOUaeiou]\w+\b', content)

        if not words:
            return("� ����� ���� ���, �� ����������� � ������� �����.")
        else:
            longest_words = []
            max_length = max(len(word) for word in words)

            for word in words:
                if len(word) == max_length:
                    longest_words.append(word)

            return("�������� �����, �� ����������� � ������� �����: "+str(longest_words))
    except FileNotFoundError:
        return("�������: ���� �� ��������.")
    except:
        return("�������: ������� ������� ��� ������� �����.")

def digit():
    input_filename = input("������ ��'� �������� �����: ")
    output_filename = input("������ ��'� ��������� �����: ")

    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        processed_content = re.sub(r'\b\w*\d\w*\b', '', content)

        with open(output_filename, 'w') as output_file:
            output_file.write(processed_content)

        return("��������� ��� ��������� � ����"+output_filename)
    except FileNotFoundError:
        return("�������: ���� �� ��������.")
    except:
        return("�������: ������� ������� ��� ������� �����.")

def year():
    current_year = datetime.datetime.now().year
    return ("�������� �� - "+str(current_year))

def yeardays():
    year = int(input("������ ��: "))

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days = 366 
    else:
        days = 365  

    return("ʳ������ ��� � ����"+str(year)+"���������"+str(days)+"���.")

def guess_number_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    printBot("��� '������ ����� �� 1 �� 10'")
    printBot("� ������� �����. ��������� �������!")

    while True:
        guess = int(input("������ ���� �������: "))
        attempts += 1

        if guess == number_to_guess:
            return("³���! �� ������� �����"+ str(number_to_guess)+"��"+ str(attempts)+ "�����!")
        else:
            return("�� ����, �� �� �������. �������� ����� - "+str(number_to_guess))


def songs():
    favorite_songs = [
        "����� ��������, � �������� � ������\n"
        "������ ��� ��� ������� ������\n"
        "�� ������� �� �������� �������\n"
        "�����, � �� ������\n"
        "� �� ����� � ������, �� �����\n"
        "���� �� � ��� ������ ���� ������ ����\n"
        "�� ��� �����, ���� �� ����� �������\n"
        "�����, � �� ������",

        "�� ����� ��������\n"
        "�� ����� ������\n"
        "�� ���-�� ������\n"
        "� ������� ���� �����.\n"
        "�� �����, �����?\n"
        "�� �����, �� �����\n"
        "�������� ��� ����������\n"
        "�� �� ������ �� ����.",

        "�������, �������, �������\n"
        "� ������ �� �������� �����\n"
        "� ���� ����, ����� ������, ������ � ������\n"
        "� ��� �� ������� � �� �������� �� ����.",

        "� ��� ��� ������ �����.\n"
        "� ������ �� ������,\n"
        "� ������ ���� ������� ����:\n"
        "���� �� �������� �������!?\n"
        "���� � ���� ���� ���� ������ �����,\n"
        "���� � �� ������,\n"
        "���� � �� �������� ���,\n"
        "�� �� ��� ���� �����,\n"
        "���� �� ���� �����.",

        "���� � ���� ���� ������ �� ���\n"
        "� ������� �� ����.\n"
        "�������� �� ���, �������� �� �����\n"
        "� ��� ���� �� ���!"
    ]
    song_chorus = random.choice(favorite_songs)
    return ("������ ���� � ��������� �����:\n"+song_chorus)


def joke():
    jokes = [
        "����� �������� � ���������?\n� ���.\n� ������� ��� �����.",
        "���� ������� �� ��� ��������� ����� �����. ������� ����� ������ ���� � ������� � ���� ���������:\n� ����� ��� �� ����� �����, ���� �� �����.",
        "�� �������\n���� ����� � ���� ����� ����� ������ �� ����� ����������� �����������???",
        "����:\n� ���� � ������. � ���� �� ������\n³�:\n� � ���� � ������ ����� ������� ������!",
        "������ ����� �� �������� �� ��������. ����� � �� �� ���. ������� ���� �� �����������. ����� � �� �� ����. ������ �������� �� �����-��������. � �� ���."
    ]
    joke = random.choice(jokes)
    return ("�������: \n"+joke)

def colors():
    return ("������� ������� ������ - ���� �� ������.")

def mountain():
    return ("�������� ���� ���� - �������.")

def lake():
    return ("�������� ����� ���� - ��������� ����.")

def teror():
    return ("���� - ������� ��������.")

class Bot:
    def __init__(self):
        self.f=''
        self.branch=''
        self.branches={
            '����������': {'���������� ������ �� ����� ������� � �������':point3d,
                           '���������� ������� ���� ����':arc,
                           '���������� ������� ������ �� ����� ������� �� ������':point2d,
                           '���������� ����� ����':square,
                           '����� �':pi,
                           '���������� ����� �������� ���� ������':point},
            '������': {'����� ������':kulon,
                       '����� �����-�������':boil,
                       '���������� �����':stala},
            '���������': {'��������� �� ������ �����':ocean,
                          '��������� �� ������ �������':area,
                          '�����, � ��� ����������� �������� ������� ���� ������':country},
            '������ � �������': {'������� ����� ��� ������ ������':space,
                                 'ϳ��������� ������� ������ � �����':sentence,
                                 '������ �������� �����, �� ����������� � ������� �����':vowel,
                                 '�������� � ������ �� �����, �� ������ �����':digit},
            '��������': {'���� ����� ��?':year,
                         '���������� ��� � ����':yeardays,
                         '������ ����� �� 1 �� 10':guess_number_game,
                         '�������� ����':songs,
                         '�������':joke,
                         '������� ������� ������':colors,
                         '��� ������� ���� � ���?':mountain,
                         '��� �������� ����� � ���?':lake,
                         '��� ������� ������������ ����� � ���?':teror}
        } 
    def start(self):
        while(1):
            printBot("�� ������ ������ ��� ������� � ��������� �������: ����������, ������, ���������, ������ � �������, ��������.")
            writetofile("�� ������ ������ ��� ������� � ��������� �������: ����������, ������, ���������, ������ � �������, ��������.",self.f)
            theme=input().lower()
            writetofile(theme,self.f)
            if theme.lower() == '�����':
                printBot("�� ���������")
                writetofile("�� ���������",self.f)
                exit()
            elif theme.lower() == '��������':
                printBot("�� ��������� ���� �����. ��� ������� ������ �� �� �������� ��������� �����������. ���������!\n")
                writetofile("�� ��������� ���� �����. ��� ������� ������ �� �� �������� ��������� �����������. ���������!\n",self.f)
            elif theme.lower() == '�����':
                printBot("ͳ���� �����������. �� �������� ����. ��� ������ �������� �����\n")
                writetofile("ͳ���� �����������. �� �������� ����. ��� ������ �������� �����\n",self.f)
            else:         
                if theme in self.branches.keys():
                    self.branch=theme
                    break
                else:
                    printBot("�������, � �� ���� ���� �����! ��������� �� ��� �� ������.")
                    writetofile("�������, � �� ���� ���� �����! ��������� �� ��� �� ������.",self.f)
        self.themes()
    def hi(self):
        printBot("�����, ���� ����� ������.")
        writetofile("�����, ���� ����� ������.",self.f)
        self.start()
    def themes(self):
        while(1):
            printBot("\n�� ������ ������ <"+self.branch+">. �� ������ ������ ��� ������� � ��������� ���:")
            writetofile("\n�� ������ ������ <"+self.branch+">. �� ������ ������ ��� ������� � ��������� ���:",self.f)
            for text in self.branches[self.branch].keys():
                printBot("\t"+text)
                writetofile("\t"+text,self.f)
            theme=input()
            writetofile(theme,self.f)
            if theme.lower() == "�����":
                printBot("�� ���������\n")
                writetofile("�� ���������\n",self.f)
                exit()
            elif theme.lower() == "��������":
                printBot("�� ������ ������ <"+self.branch+">. ��� ������� ������ ���� �� �������� ��������� �����������. ������� ���� �����!\n")
                writetofile("�� ������ ������ <"+self.branch+">. ��� ������� ������ ���� �� �������� ��������� �����������. ������� ���� �����!\n",self.f)
            elif theme.lower() == "�����":
                self.start()
            else:         
                if theme in self.branches[self.branch].keys():
                    temp=self.branches[self.branch][theme]()
                    printBot(temp)
                    writetofile(temp,self.f)
                else:
                    printBot("�������, � �� ���� ���� ����! ��������� �� ��� �� ������.")
                    writetofile("�������, � �� ���� ���� ����! ��������� �� ��� �� ������.",self.f)


def main():
    b = datetime.datetime.now()
    date=b.strftime("%d-%m-%Y %H-%M-%S")

    bot=Bot() 
    bot.f='dialog-'+date+'.txt'
    bot.hi()

if __name__ == '__main__':
    main()


