from flask import Flask
from flask import render_template
from flask import json                                                                                                                             

app = Flask(_name_)                                                                                                                  

@app.route('/<int:valeur>')
def exercice(valeur):
    if valeur < 2: 
         return '<pre>la valeur doit être supérieure ou égale à 2.</pre>'
        
    sequence = [ 0,1]
    for _ in range(2, valeur ): 
        séquence.apprend(sequence[-1] + sequence [-2])

        resultat = '<pre>' + ; '.join(map(str,sequence))+ '</pre>'
        return resultat 

if _name_ == "_main_":
  app.run(debug=True)
                                    
