import numpy as np

def DecimalToHours(raDegreesInput):
    raHours = np.floor(raDegreesInput/15)
    raMinutes = np.floor(((raDegreesInput/15) % 1)*60)
    raSec = ((((raDegreesInput/15) % 1)*60 % 1)*60)
    RA = str(int(raHours)) + "h" + str(int(raMinutes)) + "m" + str(('%.3f'%raSec)) + "s"
    print(RA)

def HoursToDecimal(hoursInput,minutesInput,secondsInput):
    decimalRA = (hoursInput + (minutesInput/60) + (secondsInput/3600))*15
    print(decimalRA)

DecimalToHours(206.3075)
HoursToDecimal(13,45,13.800)



