from yl13adminklass import *
# Teeme kolme kasutaja eksemplaarid
kasutaja1 = Admin("Timmu","Õunapuu")
kasutaja2 = Admin("Oliver","Mõttus")
kasutaja3 = Admin("Joonatan","Kelder")
### täpsustame kasutajate domeeni
kasutaja1.set_privileeg("root")
kasutaja2.set_privileeg("user")
kasutaja3.set_privileeg("user")
### täpsustame kasutajate privileegid
kasutaja1.set_domain("Domeen")
kasutaja2.set_domain("Domeen 2.0")
kasutaja3.set_domain("WorkGroup 3.0")


kasutaja1.kirjelda_kasutajat(kasutaja1.get_domain(),kasutaja1.get_privileeg())
kasutaja2.kirjelda_kasutajat(kasutaja2.get_domain(),kasutaja2.get_privileeg())
kasutaja3.kirjelda_kasutajat(kasutaja3.get_domain(),kasutaja3.get_privileeg())

kasutaja1.show_privileges()
kasutaja2.show_privileges()
kasutaja3.show_privileges()