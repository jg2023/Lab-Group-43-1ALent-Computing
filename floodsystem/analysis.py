from sqlite3 import DateFromTicks
import matplotlib
import matplotlib.dates
from matplotlib.dates import date2num
import numpy
def polyfit(dates,levels,p):
    dateFloat = []
    d0 = date2num(dates[0])
    for date in dates:
        dateFloat.append(date2num(date)-d0)
    polyCoeff = numpy.polyfit(dateFloat,levels,p)
    poly = numpy.poly1d(polyCoeff)
    return poly,d0