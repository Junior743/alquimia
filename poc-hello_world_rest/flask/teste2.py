from flask import Flask

app = Flask(__name__)

animais = [
    {
        'nome':'A',
        'tipo':'Cachorro',
        'medidas':{
            'altura':0.5,
            'peso':20
        }
    },
    {
        'nome':'B',
        'tipo':'Gato',
        'medidas':{
            'altura':0.3,
            'peso':10
        }
    },
    {
        'nome':'C',
        'tipo':'Leopardo',
        'medidas':{
            'altura':1,
            'peso':70
        }
    }
]

@app.route('/')
def olaMundo():
    
    return 'Ola mundo!'

@app.route('/animal')
def listar(self):
    
    return {'animal':self.animais}

@app.route('/animal/<nome>')
def pegar(self, nome):

    for animal in self.animais:
        if animal.nome == nome:
            return animal

    return 'Animal não encontrado'

@app.route('/animal')
def adicionar(self, animal):
    
    self.animais.append(animal)
    return self.animais

if __name__ == '__main__':
    app.run()