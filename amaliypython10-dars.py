#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  5 21:13:49 2025

@author: xasanov
"""
#######1-topshiriq#########
#cars=['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
#    if car=='gm':
#        print(car.upper())
#    else:
#        print(car.title())
######2-topshiriq#########
#cars=['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
 #   if car != 'gm':
  #      print(car.title())
  #  else:
  #      print(car.upper())
#######3-topshiriq#########
#foydalanuvchi_ismi=input("Foydalanuvchi ismini kiriting!>>>")
#if foydalanuvchi_ismi.upper()=='ADMIN':
#    print('Xush kelibsiz!\nFoydalanuvchilar ro\'yxatini ko\'rishni hoxlaysizmi?')
#else:
#    print('Foydalanuvchi ismini kiriting!')
########################################
#ism=input("ism kiriting:>>>",)
#print(ism.upper()) # .upper metodi shartlar yoki qandaydir funksiyalar bilan qo'llanadi alohida qo'llanmaydi
########################################
#################4-topshiriq#################
#sonlar=[input("1-sonni kiriting:",),input("2-sonni kiriting:")]
#if sonlar[0]==sonlar[1]:
#    print("Sonlar bir-biriga teng ekan!")
#else:
#    print("Sonlar bir-biriga teng emas ekan!")
################5-topshiriq#################
#son_kiriting=int(input("ixtiyoriy son kiriting:",))
#if son_kiriting==0:
#    print("0 musbat ham manfiy ham emas")
#if son_kiriting<0:
#    print("Manfiy son ekan")
#elif son_kiriting>0:
#    print("Musbat son ekan") # else: shart qabul qilmaydi agar shart kiritish kerak bo'lsa, elif shart: dan foydalanish kerak
#################6-topshiriq################3
#ildiz_olish_uchun_son_kiriting=float(input("Ixtiyoriy butun sonni kiriting: "),)
#if ildiz_olish_uchun_son_kiriting>=0:
#    print("Javob: ",ildiz_olish_uchun_son_kiriting**0.5)
#else:
#    print("Manfiy sondan ildiz olib bo'lmaydi!")
#############################################
ildiz_olish_uchun_son_kiriting=float(input("Ixtiyoriy butun sonni kiriting: "),)
n=ildiz_olish_uchun_son_kiriting
print("Javob: ",**0.5) if ildiz_olish_uchun_son_kiriting>=0 else print("Manfiy sondan ildiz olib bo'lmaydi!")