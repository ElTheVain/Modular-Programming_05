def cek_angka(a, b , c):
    if a + b == c or a + c == b or b + c == a:
        return True
        
    elif a == b or b == c or a == c:
        return False
        
    else:
        return False
    print(cek_angka(50, 20, 70))
    print(cek_angka(50, 20, 70))
    print(cek_angka(50, 20, 70))
