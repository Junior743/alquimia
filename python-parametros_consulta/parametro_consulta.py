# coding: utf-8

import re


class ArgumentoConsulta(object):

    def __init__(self, nome, **kwargs):
        self._valor = None
        self.nome = nome
        self.tipo = kwargs.get("tipo", str)
        self.padrao = kwargs.get("padrao", self.tipo())
        self.valor = kwargs.get("valor", self.padrao)

    @property
    def valido(self):
        try:
        
            self.validar()
            return True
        
        except Exception:
            return False

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, value):
        if self.validar_valor(value):
            self._valor = self.tipo(value)
        else:
            raise Exception()

    def validar_valor(self, valor):
        try:

            self.tipo(valor)
            return True

        except ValueError as ex:
            return False
        except Exception as ex:
            raise ex

    def validar(self):
        try:
        
            if not self.nome:
                raise Exception()
            if not self.validar_valor(self.valor):
                raise Exception()

            return True
        
        except Exception as ex:
            return False

class ArgumentoFiltro(ArgumentoConsulta):

    def __init__(self, **kwargs):
        ArgumentoConsulta.__init__(self, **kwargs)
        self.contexto = kwargs.get("contexto", None)

    def __repr__(self):
        return "filter"

    @property
    def valor(self):
        import ipdb; ipdb.set_trace()
        return self._valor

    @valor.setter
    def valor(self, value):
        self._valor = value

        if not self.valido:
            raise Exception()

    @classmethod
    def atribuir_parametros(cls, contexto, parametros):
        _self = cls(nome="filter")
        _self.valor = {
            k:v.valor 
            for k, v in parametros.items() 
            if contexto.validar_attr(k)
        }

        return _self

    def validar(self):
        try:
        
            if not self.nome:
                raise Exception()
            if not self.validar_valor(self.valor):
                raise Exception()
            if self.contexto:
                for k in self.valor:
                    if not self.contexto.validar_attr(k):
                        raise Exception()

            return True
        
        except Exception:
            return False

    def para_orm(self, contexto):
        _filtro = ()

        if self.valor:
            for k, v in self.valor.items():
                _filtro = _filtro + (
                    self._compor_filtro(contexto, k, v),
                )

        return _filtro

    def _compor_filtro(self, contexto, atributo, valor):
        return (getattr(contexto, atributo) == valor)

class ArgumentoOrdenacao(ArgumentoConsulta):

    def __init__(self, **kwargs):
        ArgumentoConsulta.__init__(self, **kwargs)

    def __repr__(self):
        return "sort"

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, value):
        self._valor = []
        _valores = [x.strip() for x in value.split(",")]

        for _valor in _valores:
            self._valor.append(
                {
                    "atributo": re.sub("\s|-", "", _valor),
                    "descendente": _valor.strip().startswith("-")
                }
            )

    def para_orm(self, contexto):
        _ordenacao = ()

        if self.valor:
            for _valor in self.valor:

                if not contexto.validar_attr(_valor["atributo"]):
                        raise Exception()

                _ordenacao = _ordenacao + (self._compor_ordenacao(
                        contexto, 
                        _valor["atributo"], 
                        _valor["descendente"]
                        ),)

        return _ordenacao

    def _compor_ordenacao(self, contexto, atributo, descendente):
        if descendente:
            return (getattr(contexto, atributo).desc())
        else:
            return (getattr(contexto, atributo))

class ParametroConsulta(object):
    CHAVES_CONHECIDAS = {
        "limit": {"objeto":ArgumentoConsulta, "parametros":{"tipo":int}},
        "offset": {"objeto":ArgumentoConsulta, "parametros":{"tipo":int}},
        "sort": {"objeto":ArgumentoOrdenacao, "parametros":{"tipo":str}},
        "relationship": {"objeto":ArgumentoConsulta, "parametros":{"tipo":str}},
        "field": {"objeto":ArgumentoConsulta, "parametros":{"tipo":str}},
        "portifolio_integral": {"objeto":ArgumentoConsulta, "parametros":{"tipo":bool, "padrao":False}},
        "abastecimento_integral": {"objeto":ArgumentoConsulta, "parametros":{"tipo":bool, "padrao": False}}
    }
    
    def __init__(self, parametros, **kwargs):
        self.parametros = parametros
        self.parametros_conhecidos = {
            k:self.CHAVES_CONHECIDAS[k]["objeto"](nome=k, valor=v, **self.CHAVES_CONHECIDAS[k]["parametros"]) 
            for k, v in parametros.items() 
            if k in self.CHAVES_CONHECIDAS
        }

        self.parametros_desconhecidos = {
            k:ArgumentoConsulta(nome=k, valor=v) 
            for k, v in parametros.items() 
            if k not in self.CHAVES_CONHECIDAS
        }

    #region [Propriedades]
    @property
    def limite(self):
        return self.parametros_conhecidos.get("limit", None)

    @property
    def deslocamento(self):
        return self.parametros_conhecidos.get("offset", None)

    @property
    def ordenacao(self):
        return self.parametros_conhecidos.get("sort", None)

    @property
    def filtros(self):
        return self.parametros_desconhecidos

    @property
    def portifolio_integral(self):
        return self.parametros_conhecidos.get("portifolio_integral", None)

    @property
    def abastecimento_integral(self):
        return self.parametros_conhecidos.get("abastecimento_integral", None)
    #endregion

    #region [Metodos Publicos]
    def __repr__(self):
        return self.__dict__

    def __str__(self):
        return str(self.parametros)

    def compor_ordenacao_orm(self, contexto):
        """
        """
        return self.ordenacao.para_orm(contexto)

    def compor_filtros_orm(self, contexto):
        """
        """
        _filtro = ArgumentoFiltro.atribuir_parametros(contexto, self.filtros)
        return _filtro.para_orm(contexto)

    #endregion


def executar():
    import polaris
    polaris.iniciar("polaris.ini")

    from polaris.globais import bd
    from polaris.materiais import ProdutoCatalogo

    sessao = bd.abrir_sessao_escrita()

    _params = {
        "limit":"10",
        "offset":"20",
        "sort":"  -nome , preco_venda",
        "nome":"[1, 2, 3]",
        "idade":"19",
        "custo_compra":"10.2"
    }

    _param_consulta = ParametroConsulta(_params)
    # print(_param_consulta.ordenacao)
    # print(_param_consulta.compor_ordenacao_orm(ProdutoCatalogo))
    print(_param_consulta.filtros)
    print(_param_consulta.compor_filtros_orm(ProdutoCatalogo))

executar()
