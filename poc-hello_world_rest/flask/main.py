from flask import Flask, jsonify, request
from flask_restful import reqparse

app = Flask(__name__)

class ApiREST():
            
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

    @app.route('/', methods=['GET'])
    def olaMundo():
        
        return "Olá mundo!"

    @app.route('/animal', methods=['GET'])
    def listar():
        
        return jsonify({'animal':ApiREST.animais})
    
    @app.route('/animal/<nome>', methods=['GET'])
    def pegar(nome):

        for animal in ApiREST.animais:
            if animal['nome'] == nome:
                return jsonify(animal)

        return 'Animal não encontrado'

    @app.route('/animal', methods=['POST'])
    def adicionar():

        # nome = request.json.get('nome')
        # tipo = request.json.get('tipo')
        # medidas = request.json.get('madidas')

        # animal = {
        #     'nome':nome,
        #     'tipo':tipo,
        #     'medidas':medidas
        # }

        args = parser.parse_args()
        print(args)
        ApiREST.animais.append(animal)
        return jsonify(ApiREST.animais)
        
    def rodar():
        
        app.run()


ApiREST.rodar()