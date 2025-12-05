def obliczBMI():
    try:
        masa = float(input('Podaj masę (w kg): '))
        wzrost = float(input('Podaj wzrost (w cm): ')) / 100

        bmi = masa / wzrost**2
        print(f'Twoje BMI: {round(bmi, 2)}')
        porownajWynik(bmi)
    except ValueError:
        print('Podaj poprawne dane!')

def porownajWynik(bmi:float):
    match bmi:
        case x if x < 18.5:
            print("Masz niedowagę")
        case x if x > 18.5 and x < 24.9:
            print('Masz idealną masę ciała')
        case x if x > 25 and x < 29.9:
            print('Masz nadwagę')
        case x if x > 30 and x < 34.9:
            print('Masz otyłość I stopnia')
        case x if x > 35 and x < 39.9:
            print('Masz otyłość II stopnia')
        case _:
            print('Masz otyłość III stopnia')



obliczBMI()