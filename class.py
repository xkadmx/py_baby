Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Zwierzęta(Żywotne):
	def oddycha(self):
		pass
	def rusza_się(self):
		pass
	def je(self):
		pass

	
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    class Zwierzęta(Żywotne):
NameError: name 'Żywotne' is not defined
>>> class SSaki(Zwierzęta):
	def karmi_młode_mlekiem(self):
		pass

	
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    class SSaki(Zwierzęta):
NameError: name 'Zwierzęta' is not defined
>>> class Rzeczowniki:
	pass

>>> class Nieżywotne(Rzeczowniki):
	pass

>>> class Żywotne(Rzeczowniki):
	pass

>>> class Chodniki(Żywotne):
	pass

>>> class Chodniki(Nieżywotne):
	pass

>>> class Zwierzęta(Żywotne):
	pass

>>> class Ssaki(Zwierzęta):
	pass

>>> class Żyrafy(Ssaki):
	pass

>>> reginald=Żyrafy()
>>> # definiowanie funkcji klas
>>> 
>>> def to_jest_normalna_funkcja():
	print('Jestem normalną funkcją')

	
>>> class ToMojaBezsensownaKlasa:
	def to_jest_funkcja_klasy():
		print('Jestem funkcją klasy')
	def to_też_jest_funkcja_klasy():
		print('Ja też jestem funkcją klasy. Rozumiemy się?')


