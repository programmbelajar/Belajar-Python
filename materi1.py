# CARA KERJA PROGRAM DAN BYTECODE
import time
start_time = time.time()
print('Hello')
print('World')
print('Hellp World')

# Ini namanya Comment, comment ini tidak akan muncul di outputnya

a = 10 #ini namanya assignment, assigment ini akan muncul di outputnya
print(a)

"""
ini namanya comment mulitiline
contoh comment multiline ini bisa digunakan 
untuk menulis banyak baris komentar
"""

"""
di python, output yang dikeluarkan itu berdasarkan
urutan print di dalam program ini
jadi, jika kita menulis print('Hello') di baris pertama
maka outputnya akan muncul di baris pertama juga
"""

print(time.time() - start_time, 'detik')
# ini namanya comment inline, comment inline ini akan muncul di outputnya
# kita bisa mengcompile python ke yang namanya bytecode, bytecode ini bisa dijalankan di komputer manapun
# cara mengcompile, buka terminal dan tuliskan python -m py_compile day-one.py
# mengcompile akan lebih cepta dibandingkan menjalankan python langsung, karena python tidak perlu mengcompile ulang setiap kali dijalankan
