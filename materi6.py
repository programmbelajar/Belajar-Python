# OPERASI ARITMATIKA

a = 15
b = 2

# Pengurangan
hasil = a - b
print(a, '-', b, '=', hasil)

# Penjumlahan
hasil = a + b
print(a, '+', b, '=', hasil)

# Perkalian
hasil = a * b
print(a, 'x', b, '=', hasil)

# Pembagian 
hasil = a/b
print(a, '/', b, '=', hasil)

# Pangkat
hasil = a ** b
print(a, '**', b, '=', hasil)

# Operasi floor division --> pembagian hasil dibulatkan ke bawah
hasil = a // b
print(a, '//', b, '=', hasil)

# Modulus --> sisa hasil bagi
hasil = a % b
print(a, '%', b, '=', hasil)

# Prioritas Operasi Aritmatika
"""
1. ()
2. exponen ** 
3. *, /, //, %
4. +, -
"""
print('')
x = 3
y = 2
z = 4

hasil = x ** y * z + x /y - y % z // y
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',y, '=', hasil)

hasil = x + y * z
print(x,'+',y,'*',z, '=', hasil)

hasil = (x + y) * z
print('(',x,'+',y,')','*',z, '=', hasil)