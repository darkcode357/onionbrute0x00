from random import choice
import sys
from os import system

def gera_senha(tamanho):
        catacteres = '0123456789abcdefghijlmnopqrstuwvxyz'
        senha = ''
        for char in xrange(tamanho):
                senha += choice(catacteres)
	return (senha)

def gera_senha2(tamanho2):
	caracteres = "ABCDEFGHIJLMNOPQRSTUWVXYZ"
	senha = ''
	for char in xrange(tamanho2):
		senha += choice(caracteres)
	return (senha) 

while True:
	a = "http://www."+gera_senha(16)+".onion"+"\n"
        print(a)
        arquivo = system("touch link1.txt")
        arquivo = open('link1.txt', 'r+')
        print(str(arquivo.readlines())) #conseguiler
        arquivo.write(a)
############################################################
	b = "http://www."+gera_senha2(16)+".onion"+"\n"
	print(b)
	arquivo = system("touch link2.txt")
	arquivo = open('link2.txt', 'r+')
	print(str(arquivo.readlines())) #conseguiler
	arquivo.write(b)
#arquivo.close()
