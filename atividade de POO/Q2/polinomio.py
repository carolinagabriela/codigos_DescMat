import csv
import matplotlib.pyplot as plt

class Polinomio:
    def __init__(self, expressao):
        self.termos = self.parse_expressao(expressao)
        self.simplificar()

    def parse_expressao(self, expressao):
        expressao = expressao.replace(" ", "")
        
        termos = {}
        i = 0
        n = len(expressao)
        coeficiente = ''
        expoente = ''
        sinal = 1  

        while i < n:
            char = expressao[i]
            if char == '+':
                sinal = 1
                i += 1
            elif char == '-':
                sinal = -1
                i += 1
            
            while i < n and expressao[i].isdigit():
                coeficiente += expressao[i]
                i += 1
            
            if coeficiente == '':
                coeficiente = '1'
            
            coeficiente = int(coeficiente) * sinal

            if i < n and expressao[i] == 'x':
                i += 1  
                if i < n and expressao[i] == '^':
                    i += 1  
                    while i < n and expressao[i].isdigit():
                        expoente += expressao[i]
                        i += 1
                else:
                    expoente = '1'  
            else:
                expoente = '0' 
            
            expoente = int(expoente)
            
            if expoente in termos:
                termos[expoente] += coeficiente
            else:
                termos[expoente] = coeficiente
            
            coeficiente = ''
            expoente = ''

        return termos

    def simplificar(self):
        self.termos = {exp: coef for exp, coef in self.termos.items() if coef != 0}

    def __str__(self):
        if not self.termos:
            return "0"
        
        termos = []
        for exp in sorted(self.termos.keys(), reverse=True):
            coef = self.termos[exp]
            if exp == 0:
                termos.append(f"{coef}")
            elif exp == 1:
                termos.append(f"{coef}x")
            else:
                termos.append(f"{coef}x^{exp}")
        
        return " + ".join(termos).replace("+ -", "- ")

    def __add__(self, outro):
        resultado = Polinomio("0")
        resultado.termos = self.termos.copy()

        for exp, coef in outro.termos.items():
            if exp in resultado.termos:
                resultado.termos[exp] += coef
            else:
                resultado.termos[exp] = coef

        resultado.simplificar()
        return resultado

    def __sub__(self, outro):
        resultado = Polinomio("0")
        resultado.termos = self.termos.copy()

        for exp, coef in outro.termos.items():
            if exp in resultado.termos:
                resultado.termos[exp] -= coef
            else:
                resultado.termos[exp] = -coef

        resultado.simplificar()
        return resultado

    def __mul__(self, outro):
        resultado = Polinomio("0")
        for exp1, coef1 in self.termos.items():
            for exp2, coef2 in outro.termos.items():
                novo_exp = exp1 + exp2
                novo_coef = coef1 * coef2
                if novo_exp in resultado.termos:
                    resultado.termos[novo_exp] += novo_coef
                else:
                    resultado.termos[novo_exp] = novo_coef

        resultado.simplificar()
        return resultado
    
    def __eq__(self, outro):
        return self.termos == outro.termos

    def avaliar(self, x):
        resultado = 0
        for exp, coef in self.termos.items():
            resultado += coef * (x ** exp)
        return resultado

    def salvar_csv(self, inicio, fim, arquivo):
        with open(arquivo, 'w', newline='') as f:
            escritor = csv.writer(f)
            escritor.writerow(["x", "f(x)"])
            for x in range(inicio, fim + 1):
                escritor.writerow([x, self.avaliar(x)])

    def plotagem(self, minx, maxx):
        valores_x = [x / 10 for x in range(minx * 10, maxx * 10 + 1)]
        valores_y = [self.avaliar(x) for x in valores_x]

        plt.figure(figsize=(10, 6))
        plt.plot(valores_x, valores_y, label=str(self), color='blue')
        plt.title('Gráfico do Polinômio')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.axhline(0, color='black', lw=0.5, ls='--')
        plt.axvline(0, color='black', lw=0.5, ls='--')
        plt.grid()
        plt.legend()
        plt.show()


#Exemplo de uso:
p1 = Polinomio("2x^2 + 3x - 5")  
p2 = Polinomio("x^2 - 2")  

soma = p1 + p2 
produto = p1 * p2 
avaliacao = p1.avaliar(2)  

# Salva os dados em um CSV para o intervalo de x = -10 a 10
p1.salvar_csv(-10, 10, "grafico_polinomio.csv")
print("Arquivo CSV salvo como 'grafico_polinomio.csv'.")
p1.plotagem(-10, 10)