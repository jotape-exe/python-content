from datetime import date, datetime
from datetime import time

def itsthedate():
    data_hj = date.today()
    print(data_hj.strftime('%d/%m/%Y'))

def itsthetime():
    hora = time(hour = 15, minute = 54, second = 30)
    hora.strftime('%H:%M:%S')
    #strftime tranforma o time em string
    print(hora)

def itsdatetime():
    data_hj = datetime.now()
    print(data_hj)

if __name__ == '__main__':
    #itsthedate()
    #itsthetime()
    #itsdatetime()