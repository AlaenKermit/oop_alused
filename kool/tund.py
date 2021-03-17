from oppimine import *

def choices():
    print("Tunni programm")
    print("1 - lisa aine teemad")
    print("2 - trüki aine teemad")
    print("3 - lisa õpilased klassi")
    print("4 - näita klassis olevaid õpilasi")
    print("5 - eemalda õpilane klassist")
    print("6 - õpeta teema õpilastele")
    print("7 - kontrolli õpilaste teadmised")
    print("8 - lase õpilasele unustada teemat")
    option = int(input("Vali sobilik tegevus: "))
    return option

def add_topic():
    topics = Andmed()
    while(True):
        topic = input("Sisesta teema: ")
        if(topic == ""):
            break
        topics.add_info(topic)
    return topics

def output_topics(lesson_topics):
    if(len(lesson_topics.info) == 0):
        print("Teemad pole sisestatud")
    else:
        print("Aine teemad on järgnevad:")
        for topic in lesson_topics:
            print("* " + topic)
        print("---")

def add_student(): # see on varajasem versioon mis töötab, aga on vale.
    opilane = str(input("Sisesta õpilase nimi keda lisada klassi: "))
    classroom.append(opilane)
    show_classroom()

''' selle peab korda saama, kuna ma pean õpilase tegema ju Opilane klassi objektiks
def add_student():
    opilane = str(input("Sisesta õpilase nimi keda lisada klassi: "))
    print(opilane)
    opilane = Opilane(opilane)
    print(opilane)
    classroom.append(opilane)
    show_classroom()
'''

def show_classroom():
    print("Klassi on lisatud hetkel järgnevad õpilased:")
    counter = 0
    for i in classroom:
        counter += 1
        print(counter, "- " + str(i))

def remove_student():
    print("Praegu on klassis järgnevad õpilased:")
    show_classroom()
    whotoremove = int(input("Sisestage number keda soovite klassist eemaldada: "))
    correction = whotoremove - 1
    print("Õpilane " + classroom[correction] + " on eemaldatud klassist.")
    del classroom[correction]

def teach_topic():
    Anna.opetab(lesson_topics, classroom)

def show_knowledge():
    pass


# TESTS START FROM HERE ON OUT

lesson_topics = []
classroom = []
Anna = Opetaja
while(True):
    option = choices()
    if(option == 1): # lisa teemad
        lesson_topics = add_topic()
    if(option == 2): # näitab kõik tunniteemad
        output_topics(lesson_topics)
    if(option == 3): # lisab õpilase klassi
        add_student()
    if(option == 4): # näitab klassi sisu
        klassisisu = show_classroom()
    if(option == 5): # eemaldab õpilase klassist
        remove_student()
    if(option == 6): # õpetab teema õpilastele
        teach_topic()
    if(option == 7): # kontrollib õpilaste teadmisi
        pass
    if(option == 8): # laseb õpilasel unustada teemat
        pass



'''
aineteemad = Andmed()
print("Aine teemad: ")
for teema in aineteemad:
    print("* " + teema)

Timmu = Opilane("Timmu")
Lisette = Opilane("Lisette")
Anna = Opetaja("Anna")

Timmu.kirjeldus()
Timmu.opib(aineteemad[0])
Timmu.kirjeldus()

Anna.opetab(aineteemad[1], Timmu, Lisette)
Lisette.kirjeldus()
Timmu.kirjeldus()

print("UNUSTAMISE TEST")
print("Timmu unustab ära " + aineteemad[1])
Timmu.unutab(aineteemad[1])
Timmu.kirjeldus()
'''