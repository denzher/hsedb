#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 11:31:12 2018

@author: AlexKale
"""

import library.database as Database

dbPath = 'data/db.txt'
FIELDS = { 'id': 0, 'Name' : 1, 'Lastname' : 2, 'Age' : 2, 'Weight' : 3 }  

def main():
    """
    Main entry point
    """
    print('Make DBs great again v0.1 ready')
    db = Database.DB(dbPath, ',', 'data/scheme.txt')
    db.printEntries()
    db.writeDB()
    
if __name__ == '__main__':
    main()
    