import random
import datetime
import pandas as pd
import names
import xlsxwriter
import string
from random import shuffle
from random import randrange
from datetime import timedelta

class DataGenerator:
    global count

    def __init__ (self,size,count = None):
        self.size = size
        self.count = 1
        

    def gen_money (self):
        self.count = 1
        self.money = []
        while self.count <= self.size:
            value = random.randint(0, 99999) 
            self.money.append(value)
            self.count = self.count + 1
        return self.money

    def gen_date (self,start,end):
        self.count = 1
        self.date = []
        while self.count <= self.size:
            dateValue = str(random.randint(1, 31)) + '/' + str(random.randint(1,12)) +'/' + str(random.randint(start,end))
            self.date.append(dateValue)
            self.count = self.count + 1
        return self.date

    def gen_UserID (self):
        self.count = 1
        self.user = []
        while self.count <= self.size:
            userfullnames = names.get_full_name()
            userId = str(userfullnames[0:random.randint(1, 3)])  + str(userfullnames[(userfullnames.find(' ')+1):len(userfullnames)][0:random.randint(3,len(userfullnames))])
            self.user.append(userId)
            self.count = self.count + 1
        return self.user

    def gen_number (self,digits):
        self.count = 1
        self.number = []
        while self.count <= self.size:
            range_start = 10**(digits-1)
            range_end = (10**digits)-1 
            no = random.randint(range_start,range_end)
            self.number.append(no)
            self.count = self.count + 1
        return self.number

    def gen_string (self,digits):
        self.count = 1
        self.char = []
        while self.count <= self.size:
            characters = ''.join(random.choices(string.ascii_lowercase, k=digits))
            self.char.append(characters)
            self.count = self.count + 1
        return self.char


    def gen_dataCorruption(self,frac,path):
        # null, cases, unicodes, #N/A, random delimeters, type differences, line,random.choice(columns),random.choice(self.cor ))
        self.cor = ['NULL', '#N/A', '"', '|', ',' ,'(']
        return





    #    print("performing the deed" )
    #    for i in range(0,len(columns)):
    #        self.data_corrupt = self.data[columns[i]].sample(frac=frac)
    #        for k in range (0,random.randint(0, len(data_corrupt))):
    #            self.data_corrupt.iloc[k,] = random.choice(self.cor)
    #        self.data.update(self.data_corrupt, join='left', overwrite=True, filter_func=None, errors='ignore')     
    #    print(self.data)
    #    return self.data




class DataExporter:
    
     

    def __init__(self):
        pass

    
    def createfile(self):
        pass

    def compiledata(self,data,columns):
        self.dictionary = dict()
        print("in here")
        for i in range(len(columns)):
            value = data[i]
            key = columns[i]
            self.dictionary[key] = value
            print(i)
        return self.dictionary
        
    def exportdata(self,path):
        df = pd.DataFrame.from_dict(self.dictionary, orient='index')
        print(df)
        with pd.ExcelWriter(path) as writer :
            print(writer)
            df.to_excel(writer)






 #
 #   def datacompiler(self,data,columns):
 #       
#
#
 #   def xlsxWrite(self,path):
 #       df = pd.DataFrame.from_dict(self.dictionary, orient='index')
 #       with pd.ExcelWriter(path) as writer:
 #           df.to_excel(writer)
#
#
#
 #       with pd.ExcelWriter(path) as writercorpt:
 #           self.data.to_excel(writercorpt,sheet_name = 'corrupted')
#

