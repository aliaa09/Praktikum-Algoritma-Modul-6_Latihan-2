def cek_tahun_kabisat(tahun):
    # Fungsi untuk mengecek apakah suatu tahun adalah kabisat atau tidak
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

def jumlah_hari_dalam_bulan(bulan, tahun):
    # Fungsi untuk menentukan jumlah hari dalam suatu bulan
    hari_dalam_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if bulan == 2:
        return 29 if cek_tahun_kabisat(tahun) else 28
    else:
        return hari_dalam_bulan[bulan - 1]

def main():
    print("Program ini akan menentukan jumlah hari dalam bulan tertentu")
    print("Masukkan 0 untuk menghentikan program")

    while True:
        bulan = int(input("Masukkan bulan (1-12): "))
        if bulan == 0:
            print("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.")
            break
        elif bulan < 1 or bulan > 12:
            print("Bulan tidak valid. Masukkan bulan antara 1 dan 12.")
            continue
        
        if bulan == 2:
            tahun = int(input("Masukkan tahun (misalnya, 2021): "))
            hari = jumlah_hari_dalam_bulan(bulan, tahun)
        else:
            hari = jumlah_hari_dalam_bulan(bulan, 0)  # Tidak perlu tahun untuk bulan selain Februari

        print(f"{hari} hari dalam sebulan\n")

main()
