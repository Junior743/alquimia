from bottle import run, get, post, request, delete

class Conexao(object):
    
    jsonAnimais = [{
                    'nome' : 'A',
                    'tipo' : 'Cachorro',
                    'altura' : 0.5,
                    'peso' : 20
                    },
                    {
                    'nome' : 'B',
                    'tipo' : 'Gato',
                    'altura' : 0.3,
                    'peso' : 10
                    },
                    {
                    'nome' : 'C',
                    'tipo' : 'Leopardo',
                    'altura' : 1,
                    'peso' : 70
                    },
                    {
                    'nome' : 'D',
                    'tipo' : 'Tatu',
                    'altura' : 0.2,
                    'peso' : 3
                    },
    ]

    @get('/animal')
    def listarAnimais(self):
        return {'animais', self.jsonAnimais}

    @get('/animal/<nome>')
    def listarAnimal(self, nome):
        
        for animal in self.jsonAnimais:
            if animal.nome == nome:
                return animal

        return 'Nome não encontrado'

    def rodar(self):
        
        run(reloader=True, debug=True)



Conexao.rodar(Conexao)