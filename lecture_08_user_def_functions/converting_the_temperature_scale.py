import random

def convert_temperature(temp, from_unit, to_unit):
    temp = float(temp)
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()
    
    if from_unit == to_unit:
        return temp
    elif from_unit == "C" and to_unit == "F":
        return (temp * 9/5) + 32
    elif from_unit == "F" and to_unit == "C":#
        return (temp - 32) * 5/9
    elif from_unit == "C" and to_unit == "K":
        return (temp +273.15)
    elif from_unit == "K" and to_unit == "C":
        return (temp - 273.15)
    elif from_unit =="F" and to_unit == "K":
        return (temp -32) *5/9 +273.15
    elif from_unit == "K" and to_unit == "F":
        return (temp -273.15) *9/5 +32
    else: 
        raise ValueError ("Invalid units, Please use the standard units i.e: C, F or K")
    
temperature = random.uniform(-30, 100)
fr = random.choice(["c", "f", "k"])
to = random.choice(["c", "f", "k"])

result = convert_temperature(temperature, fr , to)
print(f" Today's temperature is: {temperature}{fr.upper()}")
print(f" Converted temperature scale is: {to.upper()}")
print(f" Converted result is: {result}{to.upper()}")

