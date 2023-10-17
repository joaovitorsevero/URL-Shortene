#pip install pyshorteners

import pyshorteners

url_longa = input("Cole aqui o seu link: ")
type_tiny = pyshorteners.Shortener() 

link_curto = type_tiny.tinyurl.short(url_longa)

print("O seu link curto eh este aqui: " + link_curto)