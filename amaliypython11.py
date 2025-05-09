# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
########1-topshiriq#######
#son=float(input("Juft son kiriting: ",))
#if son%2: # % qoldiqni bildiradi ya'ni son o'zgaruvchini 2 ga bo'lgandagi
#    print("Bu son juft emas")
#else:
#    print("Rahmat!")
#########2-topshiriq#######
#yosh=float(input("Yoshingizni kiriting: ",))
#if yosh<=4 or yosh>=60:
#    print("Siz uchun bepul!")
#elif yosh<18:
#    print("Siz 10000 so'm to'lashingiz kerak!")
#elif yosh>=18:
#    print("Siz 20000 so'm to'lashingiz kerak!")

#if yosh<=4 or yosh>=60:
#    narx=0
#elif yosh<18:
#    narx=10000    
#elif yosh>=18:
#    narx=20000   
#if narx==0:
#    print("Siz uchun kirish bepul!")
#else:
#    print(f"Siz {narx} so'm to'lashingiz kerak!") # "" bilan matn kiritilganda {} o'zgaruvchini qabul qilmas ekan
##########3-topshiriq##########
#x=float(input("1-sonni kiriting: ",))
#y=float(input("2-sonni kiriting: ",))
#if x==y:
#    print("sonlar bir-biriga teng ekan!")
#elif x>y:
#    print("1-son 2-sondan katta ekan!")
#elif x<y:
#    print("2-son 1-sondan katta ekan!")
#########4-topshiriq###########
#mahsulotlar=['tuxum','un','yog\'','guruch','sabzi','karam','yong\'oq','olma','nok','kartoshka']
#savat=[]
#for n in range(1,6,1):
#    savat.append(input(f"savatga {n}-mahsulotni kiriting."))
#for mahsulot in savat: # takrorlanuvchi buyruq for orqali kiritiladi.
#    if mahsulot in mahsulotlar:
#        print(f"{mahsulot} do'konimizda bor!")
#    else:
#        print(f"{mahsulot} do'konimizda yo'q. Noqulaylik uchun uzur so'raymiz!")
############5-topshiriq##############
#mahsulotlar=['tuxum','un','yog\'','guruch','sabzi','karam','yong\'oq','olma','nok','kartoshka']
#savat=[]
#dokonda_bor=[]
#dokonda_yoq=[]
#for n in range(1,6,1):
#    savat.append(input(f"savatga {n}-mahsulotni kiriting."))
#for mahsulot in savat: # takrorlanuvchi buyruq for orqali kiritiladi.
#    if mahsulot in mahsulotlar:
#        dokonda_bor.append(mahsulot)
#    else:
#        dokonda_yoq.append(mahsulot)
#if dokonda_yoq==[]: # agar list bo'sh bo'lsa [] bilan ko'rsatish yetarli
#    print('Siz so\'ragan barcha mahsulotlar do\'konimizda bor')
#else:
#    print(f"quyidagi mahsulotlar do'konimizda yo'q:\n{dokonda_yoq}")
#############6-topshiriq#########
#foydalanuvchilar=['anvar','olim','hasan','husan','abbos']
#user=input('Login tanlang: ',)
#if user in foydalanuvchilar:
#    print("Login band, yangi login tanlang!")
#else:
#    print('Xush kelibsiz!')
##############7-topshiriq#########
butun_son_kiriting=float(input("Butun son kiriting: ",))
for n in range(2,11):
    if not (butun_son_kiriting%n):
        print(f"Kiritilgan son {n} ga qoldiqsiz bo'linadi")       