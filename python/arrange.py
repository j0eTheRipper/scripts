#!/usr/bin/env python3

from os import rename as mv
from os import listdir, mkdir
from os.path import isdir
from json import dump, load
from sys import argv


class DIR:
    def __init__(self, path, extensions):
        self.path = path
        self.extensions = extensions

    def extensions_setup(self):
        try:
            with open('.extensions.json') as file:
                info = load(file)
        except FileNotFoundError:
            info = dict()

        info[self.path] = tuple(self.extensions)

        with open('.extensions.json', 'w') as file:
            dump(info, file)

    def dir_setup(self):
        self.extensions_setup()

        if not isdir(self.path):
            mkdir(self.path)


class File:
    def __init__(self, path):
        self.path = path
        self.name = self.path.split('/')[-1]
        self.extension = self.path.split('.')[-1]
        self.destination = ''

    def determine(self):
        with open('.extensions.json', 'r') as file:
            dir_ext = load(file)

        for directory, extensions in dir_ext.items():
            if self.extension in extensions:
                self.destination = directory
                break

    def move(self):
        mv(self.path, f'{self.destination}/{self.name}')

    def main(self):
        self.determine()

        if self.destination != '':
            self.move()


# User commands

while True:
    user_cmd = input('Select a mode for the list below:\n1) Setup a folder\n2) clean the downloads\n0) exit\n> ')
    if user_cmd == '1':
        dir_ = input('Please enter the path of the dir (eg: ~/xxx)\n> ')
        if isdir(dir_):
            ext = input('Please enter the extensions that go in the directories')
            ext = tuple(ext.split())
            dir_ = DIR(dir_, ext)
            DIR.dir_setup(dir_)
        else:
            create_ = input('The directory you entered already exists. Do you want to create it? y / n: ')
            if create_ == 'y':
                mkdir(dir_)
    elif user_cmd == '2':
        dir_contents = listdir(f'Downloads')
        for i in dir_contents:
            new = File(f'Downloads/{i}')
            new.main()
    elif user_cmd == '0':
        quit()
