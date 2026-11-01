def baca_nilai(nama_file):
    try:
        with open(nama_file, "r") as file:
            nilai = []

            for baris in file:
                baris = baris.strip()

                if baris:
                    nilai.append(float(baris))

            return nilai

    except FileNotFoundError:
        print("File tidak ditemukan.")
        return []

    except ValueError:
        print("Data nilai tidak valid.")
        return []


data_nilai = baca_nilai("nilai.txt")

if data_nilai:
    print("Data nilai:", data_nilai)
    print("Rata-rata:", sum(data_nilai) / len(data_nilai))
else:
    print("Tidak ada data nilai.")