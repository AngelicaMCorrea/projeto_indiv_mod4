#PROJETO INDIVIDUAL MÓDULO 4
#ANGELICA MONTEIRO CORREA
#RELATÓRIO DE RECEITAS E DESPESAS PARA UMA DETERMINADA EMPRESA

# Importando bibliotecas
import pandas as pd
import numpy as np

#Dados das receitas
receitas = {'DiaSemana':['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo'],
         'valReceitas':[2200,2420.50,3391,5322,4898.50,4200,3893]}
list1 = pd.DataFrame(receitas,index=[1,2,3,4,5,6,7])

#Cria uma coluna com o valor do imposto de 7% sobre a receita diária
list1['Imposto'] = list1['valReceitas'] * 0.07
list1

#Dados das despesas
despesas = {'DiaSemana':['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo'],
           'Limpeza':[100,0,100,0,100,100,0],
           'Comida':[221.60,375,412,495,411.53,245,164],
            'Transporte':[150,100,125,300,275,525,75],
            'Outros':[0,0,2310,500,0,0,820]}    
list2 = pd.DataFrame(despesas,index=[1,2,3,4,5,6,7])
list2

#Soma total das receitas na semana
soma_valReceitas = list1['valReceitas'].sum()
soma_valReceitas

#Soma total dos impostos
soma_ttImpostos = list1['Imposto'].sum()
soma_ttImpostos

#Subtração de impostos dos ganhos diários
ganhos_liquidos = soma_valReceitas - soma_ttImpostos
ganhos_liquidos

#Média semanal das receitas
media_ganhos = soma_valReceitas/7
media_ganhos = '{:.2f}'.format(media_ganhos)
media_ganhos

#Soma total das despesas
soma_limpeza = list2['Limpeza'].sum()
soma_comida = list2['Comida'].sum()
soma_transporte = list2['Transporte'].sum()
soma_outros = list2['Outros'].sum()

ttDespesas = soma_limpeza + soma_comida + soma_transporte + soma_outros
ttDespesas

# Soma total das despesas por categoria
soma_limpeza = list2['Limpeza'].sum()
print('Total Limpeza',soma_limpeza)
soma_comida = list2['Comida'].sum()
print('Total Comida',soma_comida)
soma_transporte = list2['Transporte'].sum()
print('Total Transporte',soma_transporte)
soma_outros = list2['Outros'].sum()
print('Total Outros',soma_outros)

#Média semanal das despesas
media_despesas = ttDespesas/7
media_despesas = '{:.2f}'.format(media_despesas)
media_despesas

# Lucro diário e total da semana
list1['lucroDiário'] = list1['valReceitas'] - list1['Imposto']
list3 = list1
print(list3)
print('Lucro Total da Semana: ',ganhos_liquidos)

# Imprimindo o relatório
print('#'*40)
print('Relatório Semanal de Ganhos e Despesas')
print('#'*40)
print("Ganhos Líquidos Diários (após impostos):")
print(list3['lucroDiário'])
print('#'*40)
print('Soma Total dos Ganhos na Semana')
print(soma_valReceitas)
print('#'*40)
print('Média Semanal dos Ganhos: ',media_ganhos)
print('#'*40)
print("Despesas por Categoria:")
print('Total Limpeza',soma_limpeza)
print('Total Comida',soma_comida)
print('Total Transporte',soma_transporte)
print('Total Outros',soma_outros)
print('#'*40)
print("Soma Total das Despesas: R${:.2f}".format(ttDespesas))
print('#'*40)
print('Média Semanal de Todas as Despesas: ',media_despesas)
print('#'*40)
print("Vendas Diárias:")
print(list4['valReceitas'])
print('#'*40)
print('Lucro Total da Semana: R${:.2f}'.format(soma_valReceitas))

