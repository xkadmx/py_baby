Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
======== RESTART: C:/Users/ZuzannaRo/Desktop/python for kids/hello.py ========
Hello world
>>> 8*3.57
28.56
>>> monety_znalezione=20
>>> monety_magiczne=10
>>> monety_ukradzione=3
>>> monety_znalezione+monety_magiczne*365-monety_ukradzione*52
3514
>>> 
>>> monety_ukradzione=2
>>> monety_znalezione+monety_magiczne*365-monety_ukradzione*52
3566
>>> monety_magiczne=13
>>> monety_znalezione+monety_magiczne*365-monety_ukradzione*52
4661
>>> fred='''Wyznała mi: "Nocami czytuję pythona dla dzieciaków".'''
>>> print(fred)
Wyznała mi: "Nocami czytuję pythona dla dzieciaków".
>>> fred='''Wyznała mi: "Nocami czytuję 'pythona dla dzieciaków'".'''
>>> print(fred)
Wyznała mi: "Nocami czytuję 'pythona dla dzieciaków'".
>>> mójwynik=1000
>>> komunikat='zdobyto %s punktów'
>>> print(komunikat%mójwynik)
zdobyto 1000 punktów
>>> tekst_dowcipu='%s: urządzenie do znajdowania mebli po zmroku'
>>> część_ciała1='Kolano'
>>> 
>>> część_ciała2="Goleń"
>>> print(tekst_dowcipu % część_ciała)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(tekst_dowcipu % część_ciała)
NameError: name 'część_ciała' is not defined
>>> print(tekst_dowcipu % część_ciała1)
Kolano: urządzenie do znajdowania mebli po zmroku
>>> print(tekst_dowcipu % część_ciała2)
Goleń: urządzenie do znajdowania mebli po zmroku
>>> cyferki="Co cyfra %s mówi do cyfry %s? Fajny pasek!"
>>> print(cyferki%(0,8))
Co cyfra 0 mówi do cyfry 8? Fajny pasek!
>>> 
