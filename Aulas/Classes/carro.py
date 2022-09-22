class Carro(): 
    marca = "Mitsubishi"
    cor = "vermelho"
    motor = 2.0
    turbinado = False
    rodas_aro = 18

    def __init__(self):
        pass
    
    def atributos_carro(self):
        print(f"O carro possui os atributos:")
        print(f"Marcas: {self.marca}")
        print(f"Cor: {self.cor}")
        print(f"Motor: {self.motor}")
        print(f"Rodas aro: {self.rodas_aro}") 

    def trocar_rodas(self, novas_rodas):
        self.rodas_aro = novas_rodas
        print(f"Rodas trocadas por aro: {novas_rodas}")
    
    def trocar_cor(self, nova_cor):
        self.cor = nova_cor
        print(f"Cor trocada para: {nova_cor}")
    
    def turbinar_carro(self):
        self.turbinado = True
        print("Carro Turbinado")
 
    def testar_motor_turbinado(self):
        if self.turbinado == True:
            print("O Motor está turbinado")
        else:
            print("O motor nao esta turbinado")
    