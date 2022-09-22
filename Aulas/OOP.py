from hashlib import new
import imp
from Classes.carro import *

Carro1 = Carro()
Carro2 = Carro()

print("=-=-=-=-=- Carro 1 =-=-=-=-=-")
Carro1.atributos_carro()
Carro1.testar_motor_turbinado()

print("")
print("=-=-=-=-=- Carro 2 =-=-=-=-=-")
Carro2.trocar_rodas(21)
Carro2.trocar_cor("vermelho")
Carro2.turbinar_carro()
Carro2.atributos_carro()
Carro2.testar_motor_turbinado()
print("")
