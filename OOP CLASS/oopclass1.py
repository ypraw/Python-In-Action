
class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def render_view(self):
        print("Warna Mobil : ", self.warna)
        print("Merk Mobil : ", self.merk)


""" panggil kelas """
# Buat Objek pertama dengan variabel saya
saya = Mobil("merah", "toyota")
saya.render_view()
