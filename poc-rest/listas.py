class Listas(object):
    
    lista_itens_receita = [
        {
            "id":1,
            "nome":"receita 1",
            "quantidade":10,
            "produto":{"id":1}
        },
        {
            "id":2,
            "nome":"receita 2",
            "quantidade":1,
            "produto":{"id":2}
        },
        {
            "id":3,
            "nome":"receita 3",
            "quantidade":5,
            "produto":{"id":3}
        },
        {
            "id":4,
            "nome":"receita 4",
            "quantidade":6,
            "produto":{"id":4}
        },
        {
            "id":5,
            "nome":"receita 5",
            "quantidade":7,
            "produto":{"id":5}
        },
        {
            "id":6,
            "nome":"receita 6",
            "quantidade":1,
            "produto":{"id":6}
        },
        {
            "id":7,
            "nome":"receita 7",
            "quantidade":1,
            "produto":{"id":7}
        },
        {
            "id":8,
            "nome":"receita 8",
            "quantidade":1,
            "produto":{"id":8}
        },
    ]

    lista_pdm = [
        {
            "id":1,
            "nome":"pdm 1",
            "endereco":"rua teste, 100, bairro teste",
            "receitas":[
                {"id":1},{"id":2},{"id":3}
            ],
            "planograma":[
                {"id":1},{"id":2}
            ],
            "produto":[
                {"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8}
            ],
            "categoria":[
                {"id":1},{"id":2}
            ]
        },
        {
            "id":2,
            "nome":"pdm 2",
            "endereco":"rua teste, 200, bairro teste",
            "receitas":[
                {"id":4},{"id":5}
            ],
            "planograma":[
                {"id":3}
            ],
            "produto":[
                {"id":1},{"id":2},{"id":3},{"id":4},{"id":5}
            ],
            "categoria":[
                {"id":3}
            ]
        }
    ]

    lista_planograma = [
        {
            "id":1,
            "nome":"planograma 1",
            "pdm":{"id":1}
        },
        {
            "id":2,
            "nome":"planograma 2",
            "pdm":{"id":2}
        },
        {
            "id":3,
            "nome":"planograma 3",
            "pdm":{"id":3}
        }
    ]

    lista_produtos = [
        {
            "id":1,
            "nome":"pao sete graos"
        },
        {
            "id":2,
            "nome":"pao original"
        },
        {
            "id":3,
            "nome":"pao integral"
        },
        {
            "id":4,
            "nome":"pao light"
        },
        {
            "id":5,
            "nome":"pao recheado"
        },
        {
            "id":6,
            "nome":"pao doce"
        },
        {
            "id":7,
            "nome":"pao sem casca"
        },
        {
            "id":8,
            "nome":"pao caseiro"
        }
    ]

    lista_receitas = [
        {
            "id":1,
            "nome":"receita 1",
            "itens_receita":[
                {"id":1},{"id":2}
            ],
            "produto_final":{"id":3}
        },
        {
            "id":2,
            "nome":"receita 2",
            "itens_receita":[
                {"id":3},{"id":2}
            ],
            "produto_final":{"id":4}
        },
        {
            "id":3,
            "nome":"receita 3",
            "itens_receita":[
                {"id":1},{"id":3}
            ],
            "produto_final":{"id":5}
        },
        {
            "id":4,
            "nome":"receita 4",
            "itens_receita":[
                {"id":1},{"id":4}
            ],
            "produto_final":{"id":6}
        },
        {
            "id":5,
            "nome":"receita 5",
            "itens_receita":[
                {"id":6},{"id":8}
            ],
            "produto_final":{"id":7}
        },
    ]