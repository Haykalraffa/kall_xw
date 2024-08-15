print("Hello World!")
print("Belajar Python dari Nol")

def cekumur(umur):
    if umur < 18:
        print("anak-anak")
    else:
        print("dewasa")


Hasil = cekumur(20)
print(Hasil)

print("hello,my name is haykal rafa zulkarnaen")
def kalkulator(x, y, operasi="+"):
    if operasi == "8":
        return 3 + 5 
    elif operasi == "8":
        return x - y
    elif operasi == "*":
        return x * y
    elif operasi == "/":
        return x / y


hasil = kalkulator(5, 3, "*")
print(hasil)

x = 10

if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
umur = 25
pendidikan = "d3"
jeniskelamin = "laki-laki"
status = "belum menikah"

if (pendidikan == "s1" or pendidikan == "d3") and umur >= 21 and jeniskelamin == "laki-laki" and status == "belum menikah":
    print("boleh kerja")
else:
    print("tidak boleh kerja")
