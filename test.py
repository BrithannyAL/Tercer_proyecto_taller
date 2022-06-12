from datetime import datetime
 
hora1 = datetime.strptime("00:00:00", "%X").time()
hora2 = datetime.strptime("00:15:00", "%X").time()
hora_act = datetime.now().time()
 
if hora_act > hora1 and hora_act < hora2:
    print ("SI")
    print(hora_act)
elif hora_act < hora1 and hora_act > hora2:
    print ("NO")
