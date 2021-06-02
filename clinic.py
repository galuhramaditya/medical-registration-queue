import xmlrpc.client as client

#make stub/skeleton (proxy) on client
server = client.ServerProxy("http://127.0.0.1:8008")

#input clinic name
name = input("clinic name : ")

#add clinic to server and asign index of clinic
idx_clinic = server.addClinic(name)

#looping forever
while True:
    #get current clinic by index
    current_clinic = server.getCurrentClinic(idx_clinic)
    
    #border (name.upper() make name to be uppercase)
    print("================", name.upper(), "================")
    
    #title (current_clinic["last_queue_number"] is get a last queue number data)
    print("patients (last queue number is", current_clinic["last_queue_number"], "):")
    
    #get all patient data of queue
    for patient in current_clinic["queue"]:
        print("-------------------------------------")
        for key, val in patient.items(): #get all item of patient
            print(key, ":", val) #print key and val of each item
        print("-------------------------------------")
    
    #menu
    print("MENU :")
    print("1. refresh")
    print("2. pop patient")
    print("3. reset queue")

    #input menu
    menu = input("input : ")
    
    #if input menu = pop patient
    if menu == "2":
        server.popQueue(idx_clinic) #call popQueue
    
    #if input menu = reset queue
    elif menu == "3":
        server.resetQueue(idx_clinic) #call resetQueue
    
    #print 10 linebreak
    print("\n"*10)