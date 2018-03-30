import os
import numpy
from numpy import random
import matplotlib.pyplot as plt
life_cron = {0:0.125,1:0.125,2:0.125,3:0.125,4:0.125,5:0.125,6:0.125,7:0.125}
change = 0
areacounter = [0,0,0,0,0,0,0,0]
iteration = 0
entrada = 0
array = [0,0,0,0,0,0,0,0]
definicoes = 0
indicetarefa = [0,1,2,3,4,5,6,7]
nometarefa = [0,1,2,3,4,5,6,7]
grafico = 0
unidade_alterada = 24
medida_alterada = 'horas'

tratamento = 0

print('Medida padrao de alocacao? 1=s ou  0=n')
tratamento = input()
if tratamento != 1:
	print('Unidades')
	unidade_alterada = input()
	print('Medida')
	medida_alterada = raw_input()

while definicoes != 's':
	iteration += 1
	os.system('cls')
	os.system('clear')
	for i in indicetarefa:
		print i,'-',nometarefa[i]
	print('Escolha um numero')
	escolha = input()
	print('Atribua uma atividade')
	nometarefa[escolha] = raw_input()
	if iteration > 7:
		print('Pronto? s/n')
		definicoes = raw_input()

iteration = 0

def time_change(change):
	os.system('cls')
	os.system('clear')
	life_cron[change] += 1/24.
	if iteration >0:
		life_cron[numpy.argmin(areacounter)] -= 1/24.
	if iteration==0:
		life_cron[change] -= 1/24.
	for i in life_cron:
		print i,'-',nometarefa[i],' = ',life_cron[i]*unidade_alterada,medida_alterada
	print ''
	print 'Total: ',sum(life_cron.values())*unidade_alterada,medida_alterada
	print 'iteration',iteration
	print areacounter
	print ('Mostrar grafico? s/n')
	grafico = raw_input()
	if grafico == 's':
		labels = nometarefa[0] ,nometarefa[1] ,nometarefa[2] ,nometarefa[3] ,nometarefa[4] ,nometarefa[5] ,nometarefa[6] ,nometarefa[7]
		sizes = [life_cron[0], life_cron[1], life_cron[2], life_cron[3], life_cron[4], life_cron[5], life_cron[6], life_cron[7]]
		fig1, ax1 = plt.subplots()
		plt.ion()
		ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
		ax1.axis('equal')
		plt.show()
	print('')
	print('Qual atividade merece mais alocacao?')
	change = input()
	areacounter[change] += 1
	return change

while change != 'parar':
	print ''
	change = time_change(change)
	iteration += 1

# acrescentar um log dos inputs e array areacounter para ver quais foram minhas escolhas do dia, logar tambem array final de horas
