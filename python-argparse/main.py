import argparse

class Principal(object):

    def __init__(self):
        
        programa_argumentos = argparse.ArgumentParser(description='Conjunto de ferramentas para operacoes em geral')
        programa_argumentos_parcionados = programa_argumentos.add_subparsers()

        Principal.construirArgumentos(self, programa_argumentos_parcionados)

        programa_argumentos.add_argument('-s', '--setar', type=str, default='/', nargs=1, help='Setar o caminho do diretorio.')

        argumentos = programa_argumentos.parse_args()
        print(argumentos)


    def construirArgumentos(self, programa_argumentos_parcionados):
        
        programa_argumentos_parcionados = programa_argumentos_parcionados.add_parser('principal', help='Ferramentas gerais.')

        diretorios_argumentos = programa_argumentos_parcionados.add_subparsers()

        diretorios_argumentos_diretorio = diretorios_argumentos.add_parser('diretorio', help='Ferramentas para diretorios.')
        diretorios_argumentos_diretorio.add_argument('-ls', '--listar', type=str, default='/', nargs=1, help='Lista a arquitetura de pastas do diretorio.')
        diretorios_argumentos_diretorio.add_argument('-cp', '--copy', type=str, default='/', nargs=2, help='Copia um arquivo de um diretorio para outro.')
        diretorios_argumentos_diretorio.add_argument('-mv', '--move', type=str, default='/', nargs=2, help='Move um arquivo de um diretorio para outro.')


    def _listarDiretorios(self):
        
        return 1


Principal()