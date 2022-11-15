import time
import DataGeneration

path = r'./data.xlsx'




def data_gen(n):
    columns = ['Journal_number','amount','username','type','description','date_effective','date_entered' ]
    Jno = DataGeneration.DataGenerator(n).gen_number(6)
    Amt = DataGeneration.DataGenerator(n).gen_money()
    Uname = DataGeneration.DataGenerator(n).gen_UserID()
    Typ = DataGeneration.DataGenerator(n).gen_string(2)
    Desc = DataGeneration.DataGenerator(n).gen_string(12)
    DateEff = DataGeneration.DataGenerator(n).gen_date(2000, 2012)
    DateEnt =DataGeneration.DataGenerator(n).gen_date(1990, 2058)   
    data = [Jno,Amt,Uname,Typ,Desc,DateEff,DateEnt]

    data_cor = DataGeneration.DataGenerator(n).gen_dataCorruption(0.25, path=path)

    p = DataGeneration.DataExporter()
    p.compiledata(data= data, columns= columns)
    p.clearop(path=path)
    time.sleep(1)
    p.exportdata(path=path)
    print(data,columns)

    return 





if __name__ == '__main__':
    data_gen(n=100)