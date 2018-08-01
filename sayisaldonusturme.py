print("""
        Dönüştürmek istediğiniz sayı 16'lık sistemdeki
        bir sayı ise x, değilse y yazınız!

        Çıkmak için --> q yazınız!""")

xyorq = input('[x/y/q] : ')
if(xyorq=='x'):
    girilen_deger = input("Lütfen bir değer giriniz : ")
    girilen_donusturme = int(input("Dönüştürülen sayı sistemi - [2/8/10] : "))
    if(girilen_donusturme==10):
        print("Sonuç : ", int(girilen_deger,16))
    elif(girilen_donusturme==8):
        a = int(girilen_deger,16)
        print("Sonuç : ", '{:o}'.format(a))
    elif(girilen_donusturme==2):
        b = int(girilen_deger,16)
        print("Sonuç : ", '{:b}'.format(b))
    else:
        print("Lütfen 2,8 veya 10 dışında birşey girmeyiniz!")
elif(xyorq=='y'):
    girilen_deger = int(input("Lütfen harf veya özel karakter içermeyen bir değer giriniz : "))
    girilen_donusturme = int(input("Dönüştürülen sayı sistemi - [2/8/16] : "))
    def ikili():
        print('{:b}'.format(girilen_deger))
    def sekizli():
        print('{:o}'.format(girilen_deger))
    def onaltili():
        print('{:x}'.format(girilen_deger))
    if(girilen_donusturme==2):
        ikili()
    elif(girilen_donusturme==8):
        sekizli()
    elif(girilen_donusturme==16):
        onaltili()
    else:
        print("Lütfen 2,8 veya 16 dışında birşey girmeyiniz!")
elif(xyorq=='q'):
    exit()
else:
    print("Lütfen x, y veya q dışında birşey girmeyiniz!")
