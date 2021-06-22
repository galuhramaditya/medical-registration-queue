import xmlrpc.client as client
import time

#make stub/skeleton (proxy) on client
server = client.ServerProxy("http://0.0.0.0:8008")

#input patient identity
name = input("name : ")
medical_record_number = input("medical record number : ")
birthday = input("birthday : ")

#looping forever
while True:
    #border (name.upper() make name to be uppercase)
    print("================", name.upper(), "================")

    print("clinics :")

    #get all clinic datas and its index
    for idx_clinic, clinic in enumerate(server.getClinicDatas()):
        print("-------------------------------------")
        print("index of clinic :", idx_clinic) #print index of clinic
        print("name :", clinic["name"]) #print clinic name
        print("total of queue :", len(clinic["queue"])) #print total of queue (length of list)
        print("-------------------------------------")
    
    #menu
    print("MENU :")
    print("1. refresh")
    print("2. select clinic")

    #input menu
    menu = input("input : ")
    
    #if input menu = select clinic
    if menu == "2":
        print("\n------- select clinic -------")
        
        #input index of clinic and convert to integer
        idx_clinic = int(input("index of clinic : "))

        #looping forever
        while True:
            #get current clinic by index
            current_clinic = server.getCurrentClinic(idx_clinic)
    
            #border (current_clinic["name"].upper() make clinic name to be uppercase)
            print("================", current_clinic["name"].upper(), "================")
            
            print("patients :")
            
            #get all queue datas
            for patient in current_clinic["queue"]:
                print("-------------------------------------")
                for key, val in patient.items(): #get all item of patient
                    print(key, ":", val) #print key and val of each item
                print("-------------------------------------")
            
            #menu
            print("MENU :")
            print("1. refresh")
            print("2. take a queue")
            print("0. back")

            #input menu
            menu = input("input : ")

            #if input menu = back
            if menu == "0":
                break #stop current looping
            
            #if input menu = take a queue
            elif menu == "2":
                #add patient to queue and asign its queue number
                queue_number = server.addPatient(idx_clinic, name, medical_record_number, birthday)
                
                #looping forever
                while True:
                    #get current clinic by index
                    current_clinic = server.getCurrentClinic(idx_clinic)
                    
                    #get queue datas of current clinic
                    queue = current_clinic["queue"]

                    #if queue datas not empty
                    if len(queue) > 0:
                        #get queue number of first queue
                        first_queue_number = queue[0]["queue_number"]

                        #if first queue number is lower than current queue number
                        if first_queue_number < queue_number:
                            print("PLEASE TO BE WAITING")
                            print("your queue number is", queue_number)
                            print("=====================================")
                            print("now is", first_queue_number)
                            print(queue_number-first_queue_number, "patient more") #get different of queue number (to know how long the queue until current patient)
                        
                        #if first queue number is equal with queue number
                        elif first_queue_number == queue_number:
                            print("=====================================")
                            print("NOW IS YOU!")
                            print("=====================================")

                        #if first queue number is greater than current queue number
                        else:
                            #stop current looping
                            break
                        
                        time.sleep(1)
                    
                    #if queue datas is empty
                    else:
                        #stop current looping
                        break

                    #print 10 linebreak    
                    print("\n"*10)
            
            #print 10 linebreak                    
            print("\n"*10)
    
    #print 10 linebreak
    print("\n"*10)
