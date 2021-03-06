# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 22:34:15 2021

@author: gerar
"""
import datetime as dt
from datetime import date
from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday,\
                                    sunday_to_monday, GoodFriday
from pandas.tseries.offsets import CustomBusinessDay
from dateutil.relativedelta import relativedelta

def native_land_holidays(day):
    '''
    Feriados locales
    '''
    if day.day == 17:
        if (day.weekday() == 4) or (day.weekday() == 0):
            return day
        else:
            return day + dt.timedelta(1)
    elif day.day == 20:
        if day.weekday() == 4:
            return day
        else:
            return day - dt.timedelta(1)


def offset_holidays(day):
    '''
    Feriados mundiales
    '''
    if day.weekday() <= 3:
        return day - dt.timedelta(day.weekday())
    elif day.weekday() == 4:
        return day + dt.timedelta(3)
    return day


class CLTradingCalendar(AbstractHolidayCalendar):
    # fechas chilenas
    rules = [
        Holiday('NewYearsDay', month=1, day=1, observance=sunday_to_monday),
        GoodFriday,
        Holiday('LabourDay', month=5, day=1),
        Holiday('NavalGlories', month=5, day=21),
        Holiday('SaintsPeterandPaul', month=6, day=29,
                observance=offset_holidays),
        Holiday('OurLadyofMountCarmel', month=7, day=16),
        Holiday('AssumptionOfMary', month=8, day=15),
        Holiday('SandwichIndependenceDay1', month=9, day=17,
                observance=native_land_holidays),
        Holiday('PseudoIndependenceDay', month=9, day=18),
        Holiday('ArmyGlories', month=9, day=19),
        Holiday('SandwichIndependenceDay2', month=9, day=20,
                observance=native_land_holidays),
        Holiday('ColumbusDay', month=10, day=12,
                observance=offset_holidays),
        Holiday('AllSaintsDay', month=11, day=1),
        Holiday('ImmaculateConception', month=12, day=8),
        Holiday('Christmas', month=12, day=25),

        # ESPECIFIC HOLIDAYS CHILE
        Holiday('PapaFranciscoinChile', year=2018, month=1, day=16),
    ]
    



if __name__ == "__main__":
    f = date(2021,5, 21)
    f = date.today()

    isholiday(f)
    dtd(f)
    mtd(f)
    ytd(f)
  