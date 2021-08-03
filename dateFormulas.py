# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:38:20 2021

@author: gerar
"""


from datetime import date
from dateutil.relativedelta import relativedelta


def isholiday(cal, f):
    return f.weekday() in [5, 6] or f in cal.holidays(f, f)


def dtd(cal, bday_cl, f):
    y = f - 1 * bday_cl
    return date(y.year, y.month, y.day)


def movedays(cal, bday_cl, f, days=1):
    # negativos busca hacia atras
    y = f + days * bday_cl
    return date(y.year, y.month, y.day)


def mtd(cal, bday_cl, f, mo=1):
    # "mo" numero de meses que se mueve hacia atras
    if mo<=0:
        raise("mo debe ser distinto de 0 y positivo")
    # negativos busca hacia atras
    f = date(f.year, f.month, 1) + relativedelta(months=-mo+1)
    y = f - 1 * bday_cl
    return date(y.year, y.month, y.day)


def movemonths(cal, bday_cl, f, mo=1):
    # negativos busca hacia atras
    f = f + relativedelta(months=mo) - relativedelta(days=1)

    y = f + 1 * bday_cl
    return date(y.year, y.month, y.day)


def ytd(cal, bday_cl, f, yr=1):
    # negativos busca hacia adelante
    f = date(f.year - (yr - 1), 1, 1)
    y = f - 1 * bday_cl
    return date(y.year, y.month, y.day)



if __name__ == "__main__":
    from datetime import date
    
    import os
    FOLDER = 'D:/python/'
    os.chdir(FOLDER)
    
    import chileanCalendar as ccl
    
    cal = ccl.CLTradingCalendar()
    bday_cl = ccl.CustomBusinessDay(calendar=cal)
    
    fecha = date.today()
    
    isholiday(cal, fecha)
    
    for i in [1,2,3,4,5,6,7,8,9]:
        print(mtd(cal, bday_cl, fecha, mo=i))
        print(ytd(cal, bday_cl, fecha, yr=i))