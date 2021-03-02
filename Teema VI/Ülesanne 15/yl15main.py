from yl15klass import Inimene

inimene1 = Inimene("Timmu", "Õunapuu", 5)
inimene2 = Inimene("Joonatan", "Rõngas", 3)
inimene3 = Inimene("Jaanus", "Toots", 1)
inimene1.tutvustus()
inimene2.tutvustus()
inimene3.tutvustus()
inimene1.getmin()
inimene2.getmin()
inimene3.getmin()
#suurendame esimese inimese logimiskatsed
inimene1.suurenda_sisselogimiskatsed()
inimene1.suurenda_sisselogimiskatsed()
inimene1.suurenda_sisselogimiskatsed()
#suurendame teise inimese logimiskatsed
inimene2.suurenda_sisselogimiskatsed()
inimene2.suurenda_sisselogimiskatsed()
inimene3.suurenda_sisselogimiskatsed()
#suurendame kolmanda inimese logimiskatsed
inimene1.reset_sisselogimiskatsed()
inimene2.reset_sisselogimiskatsed()
inimene3.reset_sisselogimiskatsed()
#muudame esimese inimese parooli apelsiniks ja näitame seda
inimene1.maara_parool("apelsin")
inimene1.naita_parool()
#kontrollime teise inimese parooli test
inimene2.kontrolli_parool("aa") # ei tööta sest parool on väiksem kui 6 tähte
inimene2.naita_parool() # väljastab qwerty kuna eelmisel real on vigane parool ja parooli seepärast ei muudetud
inimene2.kontrolli_parool("12345678") # töötab sest parooli pikkus on suurem kui 5 ja väiksem kui 11
inimene2.naita_parool() # väljastab uue parooli
#
inimene3.kasutajanimi()
inimene3.parool()
input()
