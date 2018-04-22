#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 19:27:26 2018

@author: AlexKale
"""

import builtins

class DB:
    """
    Класс, описывающий базу данных
    Автор: Калентьев А. А.\n
    """
    def __init__(self, filename, delimiter, schemeFile):
        """
        Конструктор\n
        Параметры:
        \tfilename – имя файла, содержащего записи БД\n
        \tdelimiter – разделитель полей записи, используемый в файле БД\n
        \tschemeFile – имя файла, содержащего схему базы данных
        Автор: Калентьев А. А.\n
        """
        self.db = []
        self.scheme = {}
        self.filename = filename
        self.schemeFile = schemeFile
        self.delim = delimiter
        self.readScheme()
        self.readDB()
        print('Создан объект базы данных')
    
    def writeDB(self):
        """
        Записывает содержимое БД в файл
        Автор: Калентьев А. А.\n
        """
        try:
            with open(self.filename, 'w') as dbFile:
                for entry in self.db:
                    dbFile.write('{0}\n'.format(self.delim.join([str(x) for x in entry])))
        except Exception as e:
            print('Ошибка записи в файл: {0}'.format(e))
            
    def readScheme(self):
        """
        Читает схему БД и загружает ее в память\n
        Автор: Калентьев А. А.\n
        """
        try:
            with open(self.schemeFile) as schemeFile:
                for field in schemeFile:
                    #Формат файла схемы БД:
                    #Имя поля,Тип поля,Индекс поля
                    fieldInfo = field[:-1].split(',')
                    self.scheme[fieldInfo[0]] = { 'index' : fieldInfo[2], 
                                                  'type' : fieldInfo[1] }
        except Exception as e:
            print('Ошибка чтения файла схемы базы данных: {0}'.format(e))
            
    def readDB(self):
        """
        Загружает базу данных из файла в память\n
        Автор: Калентьев А. А.\n
        """
        self.db = []
        try:
            with open(self.filename, 'r') as dbFile:
                for entry in dbFile:
                    self.db.append(entry[:-1].split(self.delim))
        except Exception as e:
            print('Ошибка чтения файла базы данных: {0}'.format(e))
            
    def printScheme(self):
        """
        Печатает в консоль описание схемы БД\n
        Автор: Калентьев А. А.\n
        """
        print('Схема <{0}>'.format(self.schemeFile))
        print('Всего полей: {0}'.format(len(self.scheme)))
        for key, field in self.scheme.items():
            print('Поле {0}:\n\tтип – {1}\n\tиндекс – {2}'.format(key, 
                                                           field['type'],
                                                           field['index']))
            
    def printEntry(self, id):
        #to-do
        pass
    
    def printEntries(self):
        """
        Печатает в консоль все записи БД\n
        Автор: Калентьев А. А.
        """
        print('Записи в БД:')
        for index, entry in enumerate(self.db):
            print('{0}: {1}'.format(index, ' '.join([str(x) for x in entry])))
    
    def addEntry(self, data):
        """
        Добавляет запись в базу данных\n
        Параметры:
        \tdata – список с данными новой записи\n
        Автор: Калентьев А. А.\n
        """
        #TO-DO: обработка ошибок и проверка данных
        self.db.append(data)
        
    def addWithPrompt(self):
        """
        Интерактивное добавление записи (ввод данных через консоль)\n
        Автор: Калентьев А. А.\n
        """
        print('Добавление записи:')
        newEntry = []
        for key, field in self.scheme.items():
            while True:
                inp = input('{0} (тип {1}): '.format(key, field['type']))
                try:
                   val = getattr(builtins,field['type'])(inp)
                except ValueError as e:
                    print('Неверный тип данных')
                else:
                    newEntry.append(val)
                    break
        print('Запись к добавлению: ')
        print(newEntry)
        self.db.append(newEntry)
        
    def delete(self, id):
        """
        Удаляет запись из базы данных\n
        Параметры:
        \tid - ID записи для удаления\n
        Возвращает:
        \t0 при успешном удалении, -1 если запись с указанным ID не существует
        Автор: Калентьев А. А.
        """
        if id < len(self.db):
            del(self.db[id])
            return 0
        return -1



