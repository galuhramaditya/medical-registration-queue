from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler

#make requesthandler class
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ("/RPC2",) #limit to path /RPC2 only

#make server
with SimpleXMLRPCServer(("0.0.0.0", 8008), requestHandler=RequestHandler, allow_none=True) as server:
    #make register function
    server.register_introspection_functions()

    #make Clinic Class
    class Clinic:
        #constructor
        def __init__(self):
            #make empty clinics data
            self.clinics = []
        
        #for get all clinic datas
        def getClinicDatas(self):
            #return all clinic datas
            return self.clinics
        
        #for get current clinic data
        def getCurrentClinic(self, idx_clinic):
            #return current clinic by index of clinic
            return self.clinics[idx_clinic]

        #for add new clinic
        def addClinic(self, name):
            #append new clinic to hopital datas
            self.clinics.append({
                "name": name,
                "queue": [],
                "last_queue_number": 0
            })
            
            #return index of new clinic
            return len(self.clinics)-1

        #for reset current clinic queue
        def resetClinicQueue(self, idx_clinic):
            #get current clinic by index of clinic
            current_clinic = self.clinics[idx_clinic]

            current_clinic["queue"] = [] #reset queue to be empty
            current_clinic["last_queue_number"] = 0 #reset last queue number to be 0

        def sortingPatient(self, idx_clinic):
            self.clinics[idx_clinic]["queue"].sort(key=lambda x: x["medical_record_number"])

        #for add patient to queue of current clinic
        def addPatient(self, idx_clinic, name, medical_record_number, birthday):
            #get current clinic by index of clinic
            current_clinic = self.clinics[idx_clinic]
            
            #increment last queue number (new queue number)
            current_clinic["last_queue_number"] += 1

            #asign new queue number
            queue_number = current_clinic["last_queue_number"]

            #append patient to queue datas
            current_clinic["queue"].append({
                "queue_number": queue_number,
                "name": name,
                "medical_record_number": medical_record_number,
                "birthday": birthday
            })

            #return queue number of patient
            return queue_number
        
        #for remove first data of queue
        def popQueue(self, idx_clinic):
            #remove first data of queue by index of clinic
            self.clinics[idx_clinic]["queue"].pop(0)

    #register class
    server.register_instance(Clinic())

    print("server running...")
    
    #run server
    server.serve_forever()