from random import choice
import sys
from os import system

def gera_senha(tamanho):
        catacteres = '0123456789abcdefghijlmnopqrstuwvxzABCDEFGHIJLMNOPKQRSTUWVXZ'
        senha = ''
        for char in xrange(tamanho):
                senha += choice(catacteres)
	return (senha)

while True:
	a = "http://www."+gera_senha(16)+".onion"+"\n"
        arquivo = system("touch link1.txt")
	arquivo = open('link1.txt', 'r+')
	print(str(arquivo.readlines())) #conseguiler
	arquivo.write(a)
arquivo.close()
