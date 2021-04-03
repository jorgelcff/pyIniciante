import os
#importando a blibioteca do sistema operacional.

import time
#importando a biblioteca responsavel pelo tempo.

print("#" * 60)

with open("host") as file:
    leitor_ip = file.read()
    leitor_ip = leitor_ip.splitlines()
#pegando os ip e host do arquivo "host"

    for ip in leitor_ip:
#repretindo o ping em cada servidor
        print ("Verificando o ip: ", ip)
        print("_" * 60)
        os.system("ping -n 3 {}".format(ip)) 
#requisitando o ping com 3 pacotes em cada servidor
        print("_" * 60)
        time.sleep(2)
