class Fracao():

    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("O denominador não pode ser zero.")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def mdc(self, a, b):
        while b != 0:
            a, b = b, a%b
        return a

    def simplificar(self):
        mdc = self.mdc(self.numerador, self.denominador)
        self.numerador //= mdc
        self.denominador //= mdc

    def soma(self, other):
        denominador = self.denominador * other.denominador
        numerador = (self.numerador * other.denominador) + (other.numerador * self.denominador)
        return Fracao(numerador, denominador)

    def subtracao(self, other):
        denominador = self.denominador * other.denominador
        numerador = (self.numerador * other.denominador) - (other.numerador * self.denominador)
        return Fracao(numerador, denominador)

    def multiplicacao(self, other):
        numerador = self.numerador * other.numerador
        denominador = self.denominador * other.denominador
        return Fracao(numerador, denominador)

    def divisao(self, other):
        if other.numerador == 0:
            raise ZeroDivisionError("Divisão por zero.")
        numerador = self.numerador * other.denominador
        denominador = self.denominador * other.numerador
        return Fracao(numerador, denominador)

    def comparacao(self, other):
        if float(self.numerador/self.denominador) > float(other.numerador/other.denominador):
            return "Maior"
        elif float(self.numerador/self.denominador) < float(other.numerador/other.denominador):
            return "Menor"
        else:
            return "Igual"
        
    def conversao_para_decimal(self):
        return self.numerador/self.denominador

    def impressao(self):
        return f"{self.numerador}/{self.denominador}"

    def __str__(self):
        return self.impressao()