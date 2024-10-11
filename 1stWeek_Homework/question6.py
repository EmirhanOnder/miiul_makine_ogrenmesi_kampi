ogrenciler = ["Ali", "Veli","Ayşe","Talat","Zeynep","Ece"]

for index, student in enumerate(ogrenciler,1):
    if(index<=3):
        print("Mühendislik Fakültesi",index, ", öğrenci:",student)
    else:
        print("Tıp Fakültesi", index-3,", öğrenci:",student)