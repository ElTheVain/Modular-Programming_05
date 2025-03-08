def konversi_suhu(input_suhu, jenis_suhu):
    if jenis_suhu == 'Fahrenheit':
        Celcius_to_Fahrenheit = lambda C: (9/5) * C + 32
        hasil = Celcius_to_Fahrenheit(input_suhu)
        print(f"Suhu awal = {input_suhu} to Fahrenheit = {hasil}.")
    elif jenis_suhu == 'Reamur':
        Celcius_to_Reamur = lambda C: 0.8 * C
        hasil = Celcius_to_Reamur(input_suhu)
        print(f"Suhu awal = {input_suhu} to Reamur = {hasil}.")
    else:
        print("Jenis suhu tidak valid. Pilih 'Fahrenheit' atau 'Reamur'.")
konversi_suhu(100, 'Fahrenheit') 
konversi_suhu(80, 'Reamur')      
konversi_suhu(0, 'Fahrenheit')    
