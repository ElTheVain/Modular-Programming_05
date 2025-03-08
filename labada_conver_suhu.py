def konversi_suhu(input_suhu, jenis_suhu):
    if jenis_suhu == 'Fahrenheit':
        konversi = lambda C: (9/5) * C + 32
        hasil = konversi(input_suhu)
        print(f"Input C = {input_suhu}. Output F = {hasil}.")
    elif jenis_suhu == 'Reamur':
        konversi = lambda C: 0.8 * C
        hasil = konversi(input_suhu)
        print(f"Input C = {input_suhu}. Output R = {hasil}.")
    else:
        print("Jenis suhu tidak valid. Pilih 'Fahrenheit' atau 'Reamur'.")

konversi_suhu(100, 'Fahrenheit')   
konversi_suhu(80, 'Reamur')     
konversi_suhu(0, 'Fahrenheit')  
