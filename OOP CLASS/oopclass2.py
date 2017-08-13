

class Mobil:

    def __init__(this, merk, warna, kecepatan=0):
        this.merk = merk
        this.warna = warna
        this.kecepatan = kecepatan

    def render_view(this):
        print("Warna Mobil : ", this.warna)
        print("Merk Mobil : ", this.merk)

    def TambahKecepatan(this, increment=0):
        this.increment = increment
        this.kecepatan += increment
        return this.kecepatan


""" panggil kelas """
# Buat Objek pertama
saya = Mobil("merah", "toyota", 0)
saya.render_view()
speed = 50
print("kecepatan saat ini", saya.kecepatan, "ditambah sebesar", speed,
      "sehingga kecepatan saat ini menjadi ", saya.TambahKecepatan(speed))

print()
# Objek Kedua
kamu = Mobil("biru", "honda", 10)
kamu.render_view()
speed = 30
print("kecepatan saat ini", kamu.kecepatan, "ditambah sebesar",
      speed, "sehingga kecepatan saat ini menjadi ", kamu.TambahKecepatan(speed))
