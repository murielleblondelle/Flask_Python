from flask import Flask
from flask import render_template
from flask import json                                                                                                                             

app = Flask(name)
@app.route('/<int:valeur>')
def exercice(valeur):
somme = 0
for i in range(1, n + 1):
 if i % 11 == 0:
        continue
 if i % 5 == 0 or i % 7 == 0:
        somme += i
 if somme >= 5000:
        print("La somme a atteint ou dépassé 5000. Arrêt du programme.")
        break
print("La somme finale est :", somme)

