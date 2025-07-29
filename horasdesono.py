# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt # type: ignore

# Dados fictício: horas de computador e horas de sono 
horas_coputador = [5, 4, 6, 3, 7, 2, 5, 4, 6, 8]  # horas de computador por dia 
horas_sono  =     [7, 6, 8, 7, 9, 5, 6, 8, 7, 8]  # horas de sono por dia 

def plotar_grafico(horas_computador, horas_sono):
    plt.scatter(horas_computador, horas_sono, color='blue')
    plt.xlabel('Horas de Computador por Dia')
    plt.ylabel('Horas de Sono por Dia')
    plt.title('Correlação entre Horas de computador e Horas de Sono')
    plt.grid(True)
    plt.show()

def main():
    print("Analisando a correlação entre o tempo gasto n0o computador e as horas de sono...\n") 
    plotar_grafico(horas_coputador, horas_sono)  

    # verificar a possível correlação 
    correlacao = sum(horas_coputador[i] * horas_sono[i] for i in range(len(horas_coputador))) / len(horas_sono)
    print("A correlção entre o tempo gasto no computador e as horas de sono é: {:.2f}".format(correlacao))
        
    if correlacao >= 6:
        print("Existe uma correlação positiva entre gastos no computador e as horas de sono.")
        print("Isso sugere que quanto mais gatos mais tempo você passa no computador, mais horas de sono você tem.")
    else:
        print("Existe uma correlção negativa  entre o tempo  gastos no computador e as horas de sono.")
        print("Isso sugere que quanto mais gatos mais tempo você passa no computador, menos  horas de sono você tem.")

if __name__== "__main__":
    main()            