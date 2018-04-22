#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 11:31:12 2018

@author: AlexKale
"""

import library.database as Database

dbPath = 'data/db.txt'
schemePath = 'data/scheme.txt' 

def main():
    """
    Main entry point
    """
    print('Make DBs great again v0.1 ready')
    db = Database.DB(dbPath, ',', schemePath)
    db.printEntries()
    
if __name__ == '__main__':
    main()
    