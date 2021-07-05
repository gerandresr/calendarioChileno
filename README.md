# calendarioChileno
Calendario con feriados chilenos y algunas formulas con fechas

# liberias necesarias
import datetime as dt
from datetime import date
from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday,\
                                    sunday_to_monday, GoodFriday
from pandas.tseries.offsets import CustomBusinessDay
from dateutil.relativedelta import relativedelta
