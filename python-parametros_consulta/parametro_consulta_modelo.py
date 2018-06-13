# coding: utf-8

_params = {
    "limit":"10",
    "offset":"20",
    "sort":"nome",
    "nome":"[1, 2, 3]"
}

class ArgumentoConsulta(object):

    def __init__(self, **kwargs):
        self.nome = kwargs.get("nome", None)
        self.tipo = kwargs.get("tipo", None)
        self.padrao = kwargs.get("padrao", None)
        self.valor = kwargs.get("valor", None)

    def definir_valor(valor):
        self.valor = valor

class ParametroConsulta(object):
    CHAVES_CONHECIDAS = {
        "sort": ArgumentoConsulta(nome="sort", tipo="", padrao = ""),
        "filter": ArgumentoConsulta(nome="filter", tipo="", padrao = ""),
        "portifolio_integral": ArgumentoConsulta(nome="portifolio_integral", tipo="", padrao = ""),
        "abastecimento_integral": ArgumentoConsulta(nome="abastecimento_integral", tipo="", padrao = ""),
    }
    
    def __init__(self, parametros, **kwargs):
        
        self.parametros = parametros
        self.parametros_conhecidos = {
            k:CHAVES_CONHECIDAS[k].definir_valor(v) 
            for k, v in parametros.items() 
            if k in self.CHAVES_CONHECIDAS
        }
        
        self.parametros_desconhecidos = {
            k:ArgumentoConsulta(nome=k, valor=v) 
            for k, v in parametros.items() 
            if k not in self.CHAVES_CONHECIDAS
        }
        
    def __repr__(self):
        return self.__dict__

    def __str__(self):
        return str(self.parametros)

    @property
    def portifolio_integral(self):
        return self.parametros_conhecidos.get("portifolio_integral", False)

    @property
    def abastecimento_integral(self):
        return self.parametros_conhecidos.get("abastecimento_integral", False)

    @property
    def ordenacao(self):
        return self.parametros_conhecidos.get("sort", None)

    @property
    def filtros(self):        
        return self.parametros_conhecidos.get("filter", None)

    def compor_ordenacao_orm(self, contexto):
        """
        """
        return self

    def compor_filtros_orm(self, contexto):
        """
        """
        _atributos_contexto [
            k:v
            for k,v in self.parametros_desconhecidos
            if contexto.__atributo_locais__()
        ]


_parametro_consulta = ParametroConsulta(_params)
_parametro_consulta.sort
