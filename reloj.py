import time
from datetime import datetime

x = True

print(datetime.today().strftime('%A'))

while x == True:
    hora = time.strftime('%H:%M:%S', time.localtime())
    print(hora)
    print(hora[0:2])
    print(hora[3:5])
    time.sleep(5)

'AAAAAAAAAAAA'