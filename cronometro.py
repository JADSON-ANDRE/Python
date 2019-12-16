import time, sys
from  time import sleep 

#for contagem in range(0,10):
#    sleep(1)

for i in range(1, 21):
    sys.stdout.write("\r{}".format(i))
    sys.stdout.flush()
    time.sleep(1)

print('\nTempo Esgotado. Fim de Jogo!')