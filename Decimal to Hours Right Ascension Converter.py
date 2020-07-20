import numpy as np
import math

def DecimalToHours(raDegreesInput):
    raHours = np.floor(raDegreesInput/15)
    raMinutes = np.floor(((raDegreesInput/15) % 1)*60)
    raSec = ((((raDegreesInput/15) % 1)*60 % 1)*60)
    RA = str(int(raHours)) + "h" + str(int(raMinutes)) + "m" + str(('%.3f'%raSec)) + "s"
    print(RA)

def HoursToDecimal(hoursInput,minutesInput,secondsInput):
    decimalRA = (hoursInput + (minutesInput/60) + (secondsInput/3600))*15
    print(decimalRA)
    
def ArcminArcsecToDegrees(deg,arcmin,arcsec):
    output = deg + math.copysign(1,deg)*(arcmin/60) + math.copysign(1,deg)*(arcsec/3600)
    print(output)

def DegreesToArcminArcsec(deg):
    degreePart = math.copysign(1,deg)*np.floor(abs(deg))
    minutePart = np.floor((abs(deg) % 1)*60)
    secondPart = (((abs(deg) % 1)*60) % 1)*60
    print(degreePart,minutePart,secondPart)

DecimalToHours(206.3075)
HoursToDecimal(13,45,13.800)



