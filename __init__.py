from flask import Flask
from flask import render_template
from flask import json                                                                                                                             

app = Flask(_name_)                                                                                                                  

@app.route('/<int:valeur>')
def exercice(valeur):
    a, b = 0, 1
    suite = [a, b]
    for i in range(2, valeur):
        c = a + b
        suite.append(c)
        a, b = b, c
    # Conversion de la liste en chaîne de caractères séparée par des virgules
    return ', '.join(str(num) for num in suite[:valeur])

if _name_ == "_main_":
  app.run(debug=True)
                                    
