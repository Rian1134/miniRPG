import random as rd
import os

print("Selamat Datang\n")

print("Peraturan:\n"
      "\n- = dmg, + = heal, 0 = block\n"
      "\nAction = apa yang akan dilakukan pemain\n"
      "\nBlock = hanya bisa dilakukan jika power pemain yang diserang lebih dari lawan\n"
      "\nPower = memperkuat action secara acak (1/10)\n"
      "\nExclusive = action yang hanya bisa dilakukan bila mendapat power 10 dan tidak bisa di block\n"
      "\nsetiap pemain hanya 4 action\n")

pemainSatu = input("masukan nama(pamain 1): ")
pemainDua = input("masukan nama (pemain 2): ")
hpSatu = 1000
hpDua = 1000

giliran1 = True
giliran2 = False


actionP1 = []
actionP2 = []

power = rd.randint(1,10)


def FireBall():
    dmg = 30 * power
    if giliran1:
      hpSatu - dmg
    if giliran2:
      hpDua - dmg

def TunderStrike():
  dmg = 20 * power
  if giliran1:
      hpSatu - dmg
  if giliran2:
      hpDua - dmg
  
  