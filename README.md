# calendarioChileno
Calendario con feriados chilenos y algunas formulas con fechas

# liberias necesarias
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
