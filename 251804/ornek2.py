hava_sicaklik=int(input("hava sıcaklıgını giriniz"))
if hava_sicaklik<=5:
    print("soguk")
elif hava_sicaklik>=6 and hava_sicaklik<=14:
    print("ılık")
else:
    print("yanlış bilgi girdiniz")
    