import DataGeneration

path = '/media/beast/beast1/DeLoiTte!/randomdata.xlsx'




def data_gen():
    columns = ['Journal_number','amount','username','type','description','date_effective','date_entered' ]
    Jno = DataGeneration.DataGenerator(2).gen_number(6)
    Amt = DataGeneration.DataGenerator(2).gen_money()
    Uname = DataGeneration.DataGenerator(2).gen_UserID()
    Typ = DataGeneration.DataGenerator(2).gen_string(2)
    Desc = DataGeneration.DataGenerator(2).gen_string(12)
    DateEff = DataGeneration.DataGenerator(2).gen_date(2000, 2012)
    DateEnt =DataGeneration.DataGenerator(2).gen_date(1990, 2058)   
    data = [Jno,Amt,Uname,Typ,Desc,DateEff,DateEnt]

    data_cor = DataGeneration.DataGenerator(2).gen_dataCorruption(0.25, path=path)

    p = DataGeneration.DataExporter()
    p.compiledata(data= data, columns= columns)
    p.exportdata(path=path)
    print(data,columns)

    return 





if __name__ == '__main__':
    data_gen()