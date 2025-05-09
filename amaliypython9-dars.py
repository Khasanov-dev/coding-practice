#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  4 21:14:10 2025

@author: xasanov
"""
###################################
#ismlar=['ali','vali','hasan','husan','olim']
#for mehmon in ismlar:
    #print(f"Hurmatli", mehmon.capitalize(), f"sizni konferensiyaga taklif qilamiz!\nhurmat bilan \"Nazariy fizika\" kafedrasi")
    #print('kod', len(ismlar), 'marta takrorlandi')
#toq_sonlar_10dan100gacha=list(range(11,101,2)) # 11 dan 99 gacha toq sonlarni chiqaradi
#for n in toq_sonlar_10dan100gacha: # n o'zgaruvchi list elementidan olinadi
   # print(f'{n} ning kubi', n**3, 'ga teng.') # agar list 0 dan boshqa tartibdan boshlansa {n+1} yozilmaydi
###################################
#kinolar=[]
#for n in range(1,6,1): # n 1 dan 5 gacha qiymatlarni qabul qiladi
 #   kinolar.append(input(f"{n}-yaxshi ko\'rgan filmlaringiz nomini kiriting:"))
#print(kinolar)
###################################
tanishgan_odamlarim_soni=int(input('Bugun siz tanishgan odamlar soni:>>>'))
bugun_tanishgan_odamlarim=[]
for n in range(1,tanishgan_odamlarim_soni+1,1): #range(boshlang'ich son,oxirgidan bitta avvalgi qadamdagi son, qadam o'lchami)
    bugun_tanishgan_odamlarim.append(input(f"Siz tanishgan {n}-odamning ismi: ").capitalize()) # metodlar faqat elementlarga qo'llanadi listga emas
print(bugun_tanishgan_odamlarim)