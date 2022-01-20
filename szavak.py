szo1 = input("adj meg egy szót!  ")
szo2 = input("adj meg egy másik szót! ")
szo1_hossz = len(szo1)
szo2_hossz = len(szo2)
if szo1_hossz > szo2_hossz:
    print("Az elso szó hosszabb.")
elif szo1_hossz < szo2_hossz:
    print("A második szó a hosszabb")
else:
    print("A két szó egyforma hosszú")