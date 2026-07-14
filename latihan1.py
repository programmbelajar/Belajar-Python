# LATIHAN KONVERSI SATUAN TEMPERATURE

# Program ini akan mengkonversi suhu dari Celcius ke Reamur, Fahrenheit, dan Kelvin
celcius = float(input("Masukkan suhu dalam Celcius: "))
print("suhu adalah", celcius, "Celcius\n")

# reamur
reamur = (4/5) * celcius
print("suhu dalam Reamur adalah", reamur, "Reamur")

# fahrenheit
fahrenheit = (9/5) * celcius + 32
print("suhu dalam Fahrenheit adalah", fahrenheit, "Fahrenheit")

# kelvin
kelvin = celcius + 273
print("suhu dalam Kelvin adalah", kelvin, "Kelvin")

# Fahrenheit ke Kelvin
fahrenheit = float(input("\nMasukkan suhu dalam Fahrenheit: "))
celcius = (5/9) * (fahrenheit - 32)
kelvin = celcius + 273
print("suhu dalam Kelvin adalah", kelvin, "Kelvin")

# Kelvin ke Fahrenheit
kelvin = float(input("\nMasukkan suhu dalam Kelvin: "))
celcius = kelvin - 273
fahrenheit = (9/5) * celcius + 32
print("suhu dalam Fahrenheit adalah", fahrenheit, "Fahrenheit")