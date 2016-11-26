from bottle import run, get, post, request, delete

animais = [{
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
def listar():
    return {'animais', animais} 

run(reloader=True, debug=True)