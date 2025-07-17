"""
 ¡De Fahrenheit a Celsius!: Diseña un programa que indicando los grados Fahrenheit los transforme el Celsius.

 Fórmula de conversión: (F-32) * 5/9 = C
"""

print("=========  Fahrenheit to Celsius convertor  ==========")
fahr = float(input("\nEnter degrees in Fahrenheit: "))
cel = (fahr - 32) * 5 / 9

print("\n{} Fahrenheit = {} Celsius".format(fahr, cel))
