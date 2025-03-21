import random as rd
import os

print("Selamat Datang\n")

pamainSatu = input("masukan nama(pamain 1): ")
pamainDua = input("masukan nama (pemain 2): ")
hpSatu = 1000
hpDua = 1000

actionP1 = []
actionP2 = []

power = rd.randint(1,10)

action = ["FireBall",
          "TunderStrike",
          "FrostBall",
          "PowerPunch",
          "Heal",
          "BlackHole",
          "FirePunch",
          "FullRecovery",
          "InstantDead",
          "Block",
          "Atomic"
        ]
   