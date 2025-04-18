otopark=int(input("kaldıgınız süreyi giriniz"))
if otopark == 1 :
    print("ödeyeceginiz miktar:,5TL")
elif otopark >1 and otopark <5:
    print("ödeyeceginiz miktar:,otopark*4")
elif otopark>=5:
    print("ödeyeceginiz miktar:,otopark *5")
else:
    print("yanlış bilgi girdiniz")