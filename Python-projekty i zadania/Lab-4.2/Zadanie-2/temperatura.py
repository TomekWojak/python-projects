def c_to_f(celsius):
    stopnie_f = celsius * 9/5 + 32
    return round(stopnie_f,2)

def f_to_c(fahrenheit):
    stopnie_c = (fahrenheit - 32) * 5/9
    return round(stopnie_c,2)

def c_to_k(celsius):
    stopnie_k = celsius + 273.15
    return round(stopnie_k,2)
