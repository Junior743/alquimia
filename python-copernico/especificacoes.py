"""

REFLEXOES:

-> Haverá cenarios que não foram mapeados, 
por este motivo a adptação deste app para o modelo 
de negocio da tevec não será apenas um copiar e colar.

"""

import traceback
from enum import Enum
from json import (
	dumps,
	loads
)

import polaris
polaris.iniciar("polaris.ini")

from polaris.globais import bd
sessao = bd.abrir_sessao_escrita()

from vega.reflection import importar_classe_dinamicamente


class API(object):

	## TODO: teste para dicionario
	class enDicionario(Enum):
		b = "\'\'\'\'"
		br = "<br>"
		item = "*"
		h1 = "="
		h2 = "=="
		h3 = "==="
		h4 = "===="
		h5 = "====="
		h6 = "======"

	def __init__(self, metodo_http, uri):

		self.uri = uri
		self.metodo_http = metodo_http
		self.contexto = self.uri_para_contexto()

	def uri_para_contexto(self):
		"""
		Metodo responsavel por pegar o contexto de determinada URI
		"""
		## TODO: da para pensar em uma maneira de capturar a informação do contexto na própria visao no sirius.
		_contexto_por_uri = {
			"POST":{
				"api/1.0/usuarios":Usuario,
				"api/1.0/perfis":Usuario,
				"api/1.0/permissoes":Usuario
			},
			"PUT":{
				"api/1.0/usuarios":Usuario,
				"api/1.0/perfis":Usuario,
				"api/1.0/permissoes":Usuario
			},
			"DELETE":{
				"api/1.0/usuarios":Usuario,
				"api/1.0/perfis":Usuario,
				"api/1.0/permissoes":Usuario
			}
		}

		return _contexto_por_uri[self.metodo_http][self.uri]

	def documentar(self):
		"""
		Metodo responsavel por documentar autonomamente a API
		"""
		try:

			if self.metodo_http == "GET": return self.compor_doc_get()
			elif self.metodo_http == "POST": return self.compor_doc_post()
			elif self.metodo_http == "PUT": return self.compor_doc_put()
			elif self.metodo_http == "PATCH": return self.compor_doc_patch()
			elif self.metodo_http == "DELETE": return self.compor_doc_delete()
			elif self.metodo_http == "LINK": return self.compor_doc_link()
			elif self.metodo_http == "UNLINK": return self.compor_doc_unlink()
			else: raise Exception("Metodo HTTP não mapeado.")

		except Exception as e:
			traceback.print_exc()
			raise e

	def compor_doc_get(self):
		"""
		Metodo responsavel por compor trecho da documentação para metodo HTTP GET
		"""
		return True

	def compor_doc_post(self):
		"""
		Metodo responsavel por compor trecho da documentação para metodo HTTP POST
		"""
		return True

	def compor_doc_put(self):
		"""
		Metodo responsavel por compor trecho da documentação para metodo HTTP PUT
		"""
		return True

	def compor_doc_patch(self):
		"""
		Metodo responsavel por compor trecho da documentação para metodo HTTP PATCH
		"""
		return True

	def compor_doc_delete(self):
		"""
		Metodo responsavel por compor trecho da documentação para metodo HTTP DELETE
		"""
		return True

	def compor_doc_link(self):
		"""
		Metodo responsavel por compor trecho da documentação para metodo HTTP LINK
		"""
		return True

	def compor_doc_unlink(self):
		"""
		Metodo responsavel por compor trecho da documentação para metodo HTTP UNLINK
		"""
		return True

class MetodoHTTP(object):

	def __init__(self, contexto):
		self.contexto = contexto
		self.atributos_contexto = self._pegar_atributos_contexto()
		self.dicionario_tipos = self._pegar_dicionario_de_tipos()

	@staticmethod
	def _pegar_dicionario_de_tipos():
		"""
		Metodo responsavel por pegar o dicionario de conversão
		"""
		return {
			"BOOLEAN":True,
			"bool":True,
			"int":0,
			"INTEGER":0,
			"float":0.0,
			"FLOAT":0.0,
			"DECIMAL":0.0,
			"String":"",
			"str":"",
			"STR":"",
			"date":"0000-00-00",
			"datetim":"0000-00-00T03:00:00Z",
			"dict":{},
			"{}":{},
			"object":{},
			"Enum":""
		}

	def _pegar_atributos_contexto(self):
		"""
		Metodo responsavel por recuperar todos atributos externalizados no contexto
		"""
		return self.contexto._pegar_atributos_modelo()

	def _repr_entity_type(self, atributo:object):
		_entity_type = atributo.entity_type
		if isinstance(_entity_type, Enum):
			return "Enum"
		else:
			return _entity_type.__name__
		
	def _formatar_atributo_como_resposta(self, atributo:object):
		_valor = None
		_repr_tipo = _repr_entity_type(atributo)

		if _repr_tipo in tipos:
			_valor = _compor_valor(atributo)
			_valor = _compor_collection(atributo, _valor)
		else:
			_valor = _repr_tipo

		_valor = _compor_hateoas(atributo, _valor)

		return _valor

	def _formatar_atributo_como_envio(self, atributo:object):
		_valor = None
		_repr_tipo = _repr_entity_type(atributo)

		if _repr_tipo in tipos:
			_valor = _compor_valor(atributo)
		else:
			_valor = _repr_tipo

		_valor = _compor_relacionamento_como_envio(atributo, _valor)
		_valor = _compor_collection(atributo, _valor)

		return _valor

	def _formatar(self, atributo:object, tipo_envio:bool):
		if tipo_envio:
			return [atributo.name, _formatar_atributo_como_resposta(atributo)]
		else:
			return [atributo.name, _formatar_atributo_como_envio(atributo)]

	def _compor_valor(self, atributo):
		_repr_tipo = _repr_entity_type(atributo)
		return tipos[_repr_tipo]

	def _compor_collection(atributo, valor):
		if atributo.is_collection:
			return [valor]
		else:
			return valor

	def _compor_hateoas(self, atributo, valor):
		if atributo.is_relationship:
			return {
				"rel":"",
				"href":""
			}
		else:
			return valor

	def _compor_relacionamento_como_envio(self, atributo, valor):
		if atributo.is_relationship:
			return {
				"codigo_externo":"{codigo_externo}"
			}
		else:
			return valor

	def compor_descricao_atributos(self):
		"""
		Metodo responsavel por construir a descrição dos atributos dado um contexto
		"""
		_descricoes_atributos = ""

		for _atributo in self.atributos_contexto:
			_descricoes_atributos = _descricoes_atributos + \
							"\n<br>**" + \
							_atributo.__name__ + \
							"**: " + \
							_atributo.__doc__

		return _descricoes_atributos + "\n\n<br>"

	def compor_json(self, tipo_envio):
		# declarando variavel com dicionario
		_raw_json = {}
		# pegando atributos da entidade
		_atributos_objeto = self._pegar_atributos_contexto()

		for _atributo in _atributos_objeto:
			_key, _value = self._formatar(_atributo, tipo_envio)
			_raw_json[_key] = _value

		# convertendo para JSON
		_json = dumps(_raw_json)
		return _json

class Get(MetodoHTTP):

	def __init__(self, uri, contexto):
		self.uri = uri
		super().__init__(contexto)

	def compor_cabecalho(self, parametro_01):
		"""
		Metodo responsavel por compor o cabecalho da rota
		"""
		pass

	def documentar(self):
		"""
		Metodo responsavel por documentar a sessão de um metodo HTTP GET na documentação
		"""
		pass

class Post(MetodoHTTP):

	def __init__(self, uri, contexto):
		self.uri = uri
		super().__init__(contexto)

class Put(MetodoHTTP):

	def __init__(self, uri, contexto):
		self.uri = uri
		super().__init__(contexto)

class Patch(MetodoHTTP):

	def __init__(self, uri, contexto):
		self.uri = uri
		super().__init__(contexto)

class Delete(MetodoHTTP):

	def __init__(self, uri, contexto):
		self.uri = uri
		super().__init__(contexto)

class Link(MetodoHTTP):

	def __init__(self, uri, contexto):
		self.uri = uri
		super().__init__(contexto)

class Unlink(MetodoHTTP):

	def __init__(self, uri, contexto):
		self.uri = uri
		super().__init__(contexto)
