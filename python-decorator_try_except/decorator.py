from functools import wraps
import sys, traceback

class Decorator(object):
    
    # Este decorator retorna uma excecao em caso da funcao apresentar um erro,
    #o programador pode escolher uma mensagem para retornar em caso de erro e
    #ainda pode dizer se deseja retornar também a mensagem de erro padrao gerada
    #pelo python.
    #Os dois parametros nao sao obrigatorios, portanto... O decoretor em caso de
    #erro pode retornar somente a mensagem customizada, somente o erro padrao do
    #python ou os dois juntos.
    #
    # Parametros:
    # mensagem(string)      -> mensagem customizada pelo usuario
    # erro_padrao(boolean)  -> Se verdadeiro, retorna o erro padrão do python
    def tentar(mensagem = None, erro_padrao = False):
        def tentar(funcao):
            @wraps(funcao)
            def tentar(self):
                try:
                    funcao()
                except:
                    if mensagem:
                        print('Erro: ' + mensagem)

                        if erro_padrao:
                            raise
                    else:
                        raise

            return tentar

        return tentar

    # Este decorator retorna uma excecao caso seja gerado um erro que esteja listado
    #em 'nome_erros[]'. Se o erro gerado for igual, o comportamento será semelhante
    #ao decorator 'tentar()'. Se o erro gerado nao estiver na lista de erros ('nome_erros[]')
    #não é gerada excecao e o fluxo da funcao continua normalmente.
    #
    # Parametros:
    # mensagem(string)      -> mensagem customizada pelo usuario
    # erro_padrao(boolean)  -> Se verdadeiro, retorna o erro padrão do python
    # nome_erros[](list)    -> Lista contendo nome de erros
    def tentarCondicional(mensagem = None, erro_padrao = False, nome_erros = []):
        def tentarCondicional(funcao):
            @wraps(funcao)
            def tentarCondicional(self):
                try:
                    funcao()
                except:
                    # Pegando o erro
                    erro = traceback.format_exc().splitlines()
                    erro = erro[-1].split(':')[0]

                    # Comparando erro gerado com lista de erros "nome_erros"
                    if erro in nome_erros:
                        if mensagem:
                            print('Erro: ' + mensagem)

                            if erro_padrao:
                                raise
                        else:
                            raise

            return tentarCondicional

        return tentarCondicional



    def tentarCondicionalReverso(mensagem = None, erro_padrao = False, nome_erros = []):
        def tentarCondicionalReverso(funcao):
            @wraps(funcao)
            def tentarCondicionalReverso(self):
                try:
                    funcao()
                except:
                    # Pegando o erro
                    erro = traceback.format_exc().splitlines()
                    erro = erro[-1].split(':')[0]

                    # Comparando erro gerado com lista de erros "nome_erros"
                    if erro in nome_erros:
                        pass
                    else:
                        if mensagem:
                            print('Erro: ' + mensagem)

                            if erro_padrao:
                                raise
                        else:
                            raise

            return tentarCondicionalReverso

        return tentarCondicionalReverso


    def tentarDetalhado(mensagem = None, erro_padrao = False, nome_erros = [], nome_projeto = None, nome_arquivo = None, nome_classe = None, nome_metodo = None):
        def tentarDetalhado(funcao):
            @wraps(funcao)
            def tentarDetalhado(self):
                try:
                    funcao()
                except:
                    # Pegando o erro
                    erro = traceback.format_exc().splitlines()
                    erro = erro[-1].split(':')[0]

                    # Comparando erro gerado com lista de erros "nome_erros"
                    if erro in nome_erros:
                        if mensagem:
                            if nome_projeto or nome_arquivo or nome_classe or nome_metodo:
                                print('Projeto: ' + str(nome_projeto))
                                print('Arquivo: ' + str(nome_arquivo))
                                print('Classe: ' + str(nome_classe))
                                print('Metodo: '+ str(nome_metodo))
                                print('Erro: ' + mensagem)

                            else:
                                print('Erro: ' + mensagem)

                            if erro_padrao:
                                raise
                        else:
                            raise

            return tentarDetalhado

        return tentarDetalhado


    def tentarDetalhadoDinamico(mensagem = None, erro_padrao = False, nome_erros = []):
        def tentarDetalhadoDinamico(funcao):
            @wraps(funcao)
            def tentarDetalhadoDinamico(self):
                try:
                    funcao()
                except:
                    # Pegando o erro
                    erro_detalhado = traceback.format_exc().splitlines()
                    nome_projeto = None
                    nome_arquivo = str(erro_detalhado[3]).split("\"")[1].strip()
                    nome_classe = str(traceback.format_stack()[0].split('\n')[1]).strip()
                    nome_metodo = str(erro_detalhado[3]).split(",")[2].strip().split(" ")[1]
                    nome_erro = str(erro_detalhado[-1]).split(':')[0].strip()

                    # Comparando erro gerado com lista de erros "nome_erros"
                    if nome_erro in nome_erros:
                        if mensagem:
                            if nome_projeto or nome_arquivo or nome_classe or nome_metodo:
                                print('Projeto: ' + str(nome_projeto))
                                print('Arquivo: ' + str(nome_arquivo))
                                print('Classe: ' + str(nome_classe))
                                print('Metodo: '+ str(nome_metodo))
                                print('Erro: ' + mensagem)

                            else:
                                print('Erro: ' + mensagem)

                            if erro_padrao:
                                raise
                        else:
                            raise

            return tentarDetalhadoDinamico

        return tentarDetalhadoDinamico