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

actionP1 = []
actionP2 = []

power = rd.randint(1,10)

action = ["FireBall",
          "TunderStrike",
          "FrostBall",
          "PowerPunch",
          "FirePunch",
          "Heal",
          "Block",
          "BlackHole",
          "FullRecovery",
          "InstantDead",
          "Atomic"
        ]
persiapan = True
while persiapan == True:
  print("\nOffensive\n"
        "0.FireBall \t= -30\n"
        "1.TunderStrike \t= -20 \n"
        "2.FrostBall \t= -20 \n"
        "3.PowerPunch \t= -10 \n"
        "4.FirePunch \t= -15\n"
        "Defensive\n"
        "5.Heal \t\t= +30\n"
        "6.Block \t= 0\n"
        "exclusive\n"
        "7.BlackHole \t= -500\n"
        "8.FullRecovery \t= +9999\n"
        "9.InstantDead \t= -9999\n"
        "10.Atomic \t= -9999\n")
  
  setup1 = 1
  print("\npemain1: \n")
  while setup1 <= 4:
    pilihan1 = int(input("pilih action: "))
    actionP1.append(action[pilihan1])
    setup1 = setup1 + 1
    
  setup2 = 1
  print("\npemain2: \n")
  while setup2 <= 4:
    pilihan2 = int(input("pilih action: "))
    actionP2.append(action[pilihan2])
    setup2 = setup2 + 1
    persiapan = False
    
print(f"\nPemain1\t:{pemainSatu}\n"
      f"hp\t:{hpSatu}\n"
      f"action\t:{actionP1}\n"
      
      f"\nPemain2\t:{pemainDua}\n"
      f"hp\t:{hpDua}\n"
      f"action\t:{actionP2}\n"
      )
