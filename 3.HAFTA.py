"""sayi_1=int(input("Lütfen Bir Tam Sayı Giriniz\n"))
sayi_2=int(input("Lütfen Bir Tam Sayı Daha Giriniz\n"))
print(f"işlem=sayi_1<sayi_2 \t sonuç= {not(sayi_1<sayi_2)}")
print(f"işlem=sayi_1<=sayi_2 \t sonuç= {not(sayi_1<=sayi_2)}")
print(f"işlem=sayi_1>sayi_2 \t sonuç= {not(sayi_1>sayi_2)}")
print(f"işlem=sayi_1>=sayi_2 \t sonuç= {not(sayi_1>=sayi_2)}")
print(f"işlem=sayi_1==sayi_2 \t sonuç= {not(sayi_1==sayi_2)}")
print(f"işlem=sayi_1!=sayi_2 \t sonuç= {not(sayi_1!=sayi_2)}")
print(f"işlem=sayi_1!=sayi_2 \t sonuç= {not(not(not(not(sayi_1!=sayi_2))))}")"""
#--------------------------------------------------------------------------------------------------------------------
#pythonda is, not , in kelimeleri ingilizcede taşıdıkları anlamlarıyla programlamada kullanılır özellikle mantıksal sorgularda!
#not kelimesi bir işlemi tersine çevirir
#is kelimesi bir işlemi kontrol eder
#in kelimesi bir işlemin içinde olup olmadığını kontrol eder
#örnek olarak not(sayi_1<sayi_2) sayi_1 sayi_2 den küçükse False döndürür ve not ile True yapar
#is kelimesi ise bir işlemi kontrol eder örneğin sayi_1<sayi_2 işlemi doğruysa True döndürür
#in kelimesi ise bir işlemin içinde olup olmadığını kontrol eder örneğin sayi_1 sayi_2 nin içinde varsa True döndürür
#--------------------------------------------------------------------------------------------------------------------
"""ogrnot=int(input("Lütfen Notunuzu Giriniz\n"))


if ogrnot>0 and ogrnot<=45:
    print("Notunuz FD")
elif ogrnot>=45 and ogrnot<=50:
    print("Notunuz DC")
elif ogrnot>=50 and ogrnot<=60:
    print("Notunuz CC")
elif ogrnot>=61 and ogrnot<=70:
    print("Notunuz CB")
elif ogrnot>=71 and ogrnot<=80:
    print("Notunuz BB")
elif ogrnot>=81 and ogrnot<=90:
    print("Notunuz BA")
elif ogrnot>=91 and ogrnot<=100:
    print("Notunuz AA")
else :
    print("Geçerli bir not giriniz")"""
#--------------------------------------------------------------------------------------------------------------------

"""sayi=int(input("Lütfen Bir Sayı Giriniz\n")) 
if sayi>0 and sayi%2==1:
    print(f"{sayi} sayısının karesi= {sayi**2}")
elif sayi>0 and sayi%2==0:
    print(f"{sayi} sayısının küpü= {sayi**3}")
elif sayi<0 and sayi%2==1:
    print(f"{sayi} sayısının pozitif halinin üç katı= {(sayi*-1)*3}")
elif sayi<0 and sayi%2==0:
    print(f"{sayi} sayısının pozitif halinin iki katının 4 fazlası= {(sayi*-1)*2+4} sayının mutlak değeri ={abs(sayi)}")
else:
    print("tam sayı girmediniz")"""

#-----------------------------------------------------------------------------------------------------------------------

"""for i in range(10):
    pass
print(i)"""
#tab koyarsak içine girdiği için 0 dan 10 a kadar yazar tab koymazsak sadece 9 yazar
#pass ifadesi bir bloğun içinde hiçbir işlem yapmadan geçmesini sağlar
"""for i in range(5,11):
    print(i)"""
#5 den 10 a kadar yazar
#for anahtar_kelime in range(başlangıç,bitiş,artış):
"""for i in range(1,11,2):
    print(i)"""
#1 den 10 a kadar 2 şer artar
#1 3 5 7 9
#if kullanmadan 1 ile 200 arasındaki 6'ya tam bölünen tüm sayıları yazdırın (for kullanarak)
"""for i in range(6,200,6):

    print(i)"""
#1 ile 300 arasında
#3 e ve 7 ye tam bölünen ama 2 ye tam bölünmeyen ilk 6 sayıyı yazdıran kod
#(sayaç mantığı da devreye girecek)
#if ile break kullanımı 
#if ile bir sorgudan bir şart arandıktan sonra break komutu yazılırsa
#döngü kırılır ve döngüden çıkılır
"""sayac=0
for i in range(1,300):
    if i%3==0 and i%7==0 and i%2!=0:
        print(f" sayi {sayac+1}= {i}")
        sayac+=1
    if sayac==6:
        break
print(f"toplamda {sayac} tane sayı bulundu")"""
#break komutu döngüyü kırar ve döngüden çıkar
#---------------------------------------------------------------------------------   
#iç içe for kullanımı
"""for i in range(1,6):
    for j in range(6,11):
        print(f"{i}x{j}={i*j}")"""
#iç içe for kullanımı ile 1 den 5 e kadar olan sayıların 6 dan 10 a kadar olan sayılarla çarpımını yazar
#dış döngü 1 den 10 (dahil) a kadar 
#iç döngü 11 den 20 (dahil) ye kadar olmak üzere
#tüm sayılırın çarpım sonuçlarından tek olanları yazdırın
#sonucu 11 den büyük 70 den küçük olanları yazdırın
#kaç tane sonuç olduğunu yazdırın 
"""sayac=0
for i in range(1,11):
    for j in range(11,21):
        sonuc=i*j
        if (sonuc)%2==1 and sonuc>11 and sonuc<70:
            sayac+=1
            print(f"{sayac} kadar sonuç vardır {i}x{j}={sonuc}")"""

    




   


    

    