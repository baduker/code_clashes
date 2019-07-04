def bmi(weight, height):
    b = round(weight / height ** 2, 1)
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]