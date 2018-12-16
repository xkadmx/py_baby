Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> wielkiewlochategaloty=['wielkie','wlochate','galoty']
>>> for i in wielkiewlochategaloty:
	print(i)
	print(i)

	
wielkie
wielkie
wlochate
wlochate
galoty
galoty
>>> 
>>> wielkiewlochategaloty=['wielkie','wlochate','galoty']
>>> for i in wielkiewlochategaloty
SyntaxError: invalid syntax
>>> for i in wielkiewlochategaloty:
	print(i)
	for j in wielkiewlochategaloty:
		print(j)

		
wielkie
wielkie
wlochate
galoty
wlochate
wielkie
wlochate
galoty
galoty
wielkie
wlochate
galoty
>>> 
