from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
#list of fonts
fonts = figlet.getFonts()
if len(sys.argv) ==1:
  figlet.setFont(font=random.choice(fonts))
elif len(sys.argv) ==3 and (sys.argv[1] == "-f" or sys.argv["--font"])  and sys.argv[2] in fonts:
  figlet.setFont(font=sys.argv[2])
else:
  sys.exit("Invalid Usage")

text = input ("Input: ")
print(figlet.renderText(text))











#print(fonts)
#text = "hellow, world"
#figlet.setFont(font="alphabet")
#print(figlet.renderText(text))