#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 11:31:12 2018

@author: AlexKale
"""

import library.database as database

#убрать, читать имена файлов из консоли
DB_PATH = 'data/db.txt'
SCHEME_PATH = 'data/scheme.txt'

def main():
    """
    Точка входа
    """
    print('Make DBs great again v0.1 ready')
    base = database.DataBase(DB_PATH, ',', DB_PATH)
    base.print_scheme()
    base.print_entries()

if __name__ == '__main__':
    main()
    