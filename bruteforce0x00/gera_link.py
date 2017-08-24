from random import choice
import requests,sys
from os import system
proxies = {
    'http': 'socks5://127.0.0.1:9150',     'https': 'socks5://127.0.0.1:9150'
}

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
	b = "http://www."+gera_senha(16)+".onion"+"\n"
        
	c = "http://www."+gera_senha(16)+".onion"+"\n"
        
	d = "http://www."+gera_senha(16)+".onion"+"\n"
	
	print("=>"+" " + a)
	print("="*40)
	print("==>"+" " + b)
	print("===>"+" " + c)
	print("====>"+" " + d)

'''	
 try:
                        arquivo = system("touch link1.txt")
                        arquivo = open('link1.txt', 'r+')
                        arquivo.readlines() #conseguiler
                        arquivo.write(a)
                except IndexError, KeyboardInterrupt:
                        arquivo.close()
                print("=>"+" " + a)
                print("="*40)
'''
