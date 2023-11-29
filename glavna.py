import pom
pojam = pom.odaberi_pojam()
crtice = pom.crtice(pojam)
print("Rec je:","".join(crtice))
dozvoljena_greska = 6
brojpokusaja = 3
while True:
    slovo = input("Unesite slvo ili pritisnite space da pogadjate rec: ").lower()
    if slovo != " ":
        izbor = pom.moje_slovo(pojam, crtice, slovo)
        if not pom.slovo_u_reci(pojam,slovo):
            dozvoljena_greska -= 1
            print("slovo {0} se ne nalazi u reci".format(slovo))
        print("Dozvoljen broj promasaja:", dozvoljena_greska)
    elif slovo == " ":
        rec = input("Unesite rec: ")
        if rec == pojam:
            print("Pogodili ste datu rec.")
            if dozvoljena_greska>4:
                print("Cestitamo!! Osvojili ste 100 bodova")
            elif dozvoljena_greska>2:
                print("Osovojili ste 50 bodova")
            elif dozvoljena_greska>=1:
                print("Osovjili ste 20 bodova")
            
            break
        else:
            brojpokusaja -= 1
            print("Niste pogodili. Imate jos {} pokusaja".format(brojpokusaja))
            if brojpokusaja == 0:
                print("Izgubili ste")
                break
            print("".join(pom.moje_slovo(pojam,crtice,slovo)))
            continue
    if dozvoljena_greska == 0:
        print("Nazalost, izgubili ste.")
        break
    print("".join(izbor))
    