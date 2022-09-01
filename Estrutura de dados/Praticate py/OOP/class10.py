"""
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel

Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e 
mostra a quantidade de litros que foi colocada no veículo

abastecerPorLitro( ) – método onde é informado a quantidade em litros 
de combustível e mostra o valor a ser pago pelo cliente.

alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""

def div():
    print(14*" - ")

class bombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade = quantidade
    
    #Calculo simples para definir quanto litros abastecer pelo valor dado
    def abastecer_valor(self, qntd_valor):
        if qntd_valor <= self.quantidade:
            qntd_valor /= self.valor_litro
            self.quantidade -= qntd_valor
            print("Bomba abasteceu %s litros"%qntd_valor)
            div()
            print("A bomba possui %s litros"%self.quantidade)
            div()
        else:
            print("Voce tentou abastecer {} litros, mas bomba possui {} litros".format(qntd_valor, self.quantidade))
            div()

    #abastece por litro, se ainda tiver algo na bomba
    def abastecer_litro(self, qntd_lito):
        if qntd_lito <= self.quantidade:
            self.quantidade -= qntd_lito
            print("Bomba abasteceu %s litros"%qntd_lito)
            div()
            print("A bomba possui %s litros"%self.quantidade)
            div()
        else:
            print("Voce tentou abastecer {} litros, mas bomba possui {} litros".format(qntd_lito, self.quantidade))
            div()

    #não consegui usar o return por que preciso do print, então criei o "new_valor_litro"
    def mudar_valor(self, new_valor_litro):
        print("Valor do combustivel atalizado! {}R$ -> {}R$".format(self.valor_litro, new_valor_litro))
        div()
        self.valor_litro = new_valor_litro
        
    #O mesmo caso do anterior 
    def muda_combustivel(self, new_tipo_combustivel):
        print("Combustivel da bomba alterado! {} -> {}".format(self.tipo_combustivel, new_tipo_combustivel))
        div()
        self.tipo_combustivel = new_tipo_combustivel
        
    #voce não pode abastecer a bomba com valores negativos esperto :)
    def mudar_quantidade(self, new_quantidade):
        if new_quantidade < 0:
            print("Quantidade de combustivel incompatível!")
            div()
        else:
            self.quantidade += new_quantidade
            print("Bomba abastecida! quantidade restante {} litros.".format(self.quantidade))
            div()
            
            

bomba1 = bombaCombustivel("gasolina", 5, 150)
bomba1.abastecer_litro(34)
bomba1.abastecer_litro(34)
bomba1.abastecer_litro(31.99)
bomba1.abastecer_valor(5)
bomba1.mudar_valor(7.13)
bomba1.muda_combustivel("Diesel")
bomba1.mudar_quantidade(15)
bomba1.mudar_quantidade(9)
bomba1.abastecer_litro(60)