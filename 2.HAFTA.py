tamsayi=15
floatsayi=15.5
karakter='efe'
cumle="efemetik"

print(f"int tipindeki değer ataması ={tamsayi}")
print(f"float tipindeki değer ataması ={floatsayi}")
print(f"karakter tipindeki değer ataması ={karakter}")
print(f"cümle tipindeki değer ataması ={cumle}")

sayi1=int(input("Lütfen Bir Tam Sayı Giriniz\n"))
sayi2=int(input("Lütfen Bir Tam Sayı Daha Giriniz\n"))

print(f"iki sayının toplamı = {sayi1+sayi2}")
print(f"iki sayının farkı = {sayi1-sayi2}")
print(f"iki sayının çarpımı = {sayi1*sayi2}")
print(f"iki sayının küsüratlı bölümü = {sayi1/sayi2}")
print(f"iki sayının  bölümü = {sayi1//sayi2}")
print(f"ilk sayının üssü = {sayi1**2}")
print(f"ikinci sayının üssü = {sayi2**2}")
print(f"{sayi1} sayısının 6 ile bölümünden kalan = {sayi1%6}")
print(f"{sayi2} sayısının 6 ile bölümünden kalan = {sayi2%6}")

print(f"sayi 1 isimli değişkenin tipi{type(sayi1)}")
print(f"sayi 2 isimli değişkenin tipi{type(sayi2)}")
print(f"karakter değişkenin tipi{type(karakter)}")

mantıksal1=bool(0)
mantıksal2=bool(1)
print(mantıksal1)
print(mantıksal2)

bool1=int(False)
bool2=int(True)
print(bool1)
print(bool2)

float1=int( 1.6)
int1=float(9)
int2=str(95)
print(float1)
print(int1)
print(int2)

float2=bool(1.5)
float3=bool(0.0)
print(f"floattan boola {float2}")
print(f"floattan boola {float3}")
bool3=float(False)
bool4=float(True)
print(f"booldan floata {bool3}")
print(f"booldan floata {bool4}")
bool5=str(False)
bool6=str(True)
print(f"booldan str e {bool5}")
print(f" booldan str e {bool6}")

#isinstance(int2,int) int mi diye kontrol ediyor 
mahmut="MAHMUTinyo"

print(mahmut.startswith("ma"))

print(mahmut.__contains__("mah"))
print(mahmut.lower())
#\n alt satıra geçer \t tab açar 
print(f"MAHMUTinyo da kaç tane M var ={mahmut.count('M')}")
hasan="hasaninyo"
print(f" mahmut kere hasan {mahmut*hasan.__len__()}")