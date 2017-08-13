
__author__ = "Yunindyo Prabowo"
__date__ = "$Apr 5, 2017 2:55:21 AM$"


board = []


def print_matrix(matrix):
    for baris in matrix:
        new_baris = str(baris)
        new_baris = new_baris.replace(',', '')
        new_baris = new_baris.replace('[', '')
        new_baris = new_baris.replace(']', '')
        print new_baris


# inisialisasi matrik versi1
initMatrix = [["Y"] * 5 for i in range(5)]

# inisialisasi matrik versi2
for x in range(0, 5):
    board.append(["0"] * 5)


# versi jelek dipandang mata
print " versi gak enak dipandang mata"
print board

# versi kerenan dikit
print "versi kerenan dikit"
print_matrix(board)
