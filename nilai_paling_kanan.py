def cek_digit_kanan(a, b, c):
    digit_a = a % 10
    digit_b = b % 10
    digit_c = c % 10
    if digit_a == digit_b and digit_b == digit_c:
        return True  
    elif digit_a == digit_b or digit_a == digit_c or digit_b == digit_c:
        return True  
    else:
        return False
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))
hasil = cek_digit_kanan(a, b, c)
print(hasil)
