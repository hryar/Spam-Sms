import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""
	;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	;       S P A M  S M S      ;
	;---------------------------;
	;       Author : Hry Ar     ;
	;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

Menu :

1. OTP KANTOR PRESIDEN
2. OTP KANTOR BUPATI
3. OTP KANTOR DPRD
4. OTP KANTOR CAMAT
5. OTP KANTOR POLISI
""")
		pilih=int(input('noobie/> '))
		if pilih == 1:
			import src.presiden
		elif pilih == 2:
			import src.bupati
		elif pilih == 3:
			import src.dprd
		elif pilih == 4:
			import src.camat
		elif pilih == 5:
			import src.polisi
		else: print("[!] lihat menu dong(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))
