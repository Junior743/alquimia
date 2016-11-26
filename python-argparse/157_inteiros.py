import argparse

parser = argparse.ArgumentParser(description='Alguns processos inteiros.')
parser.add_argument('inteiros', metavar='N', type=int, nargs='+',
                    help='Um inteiro para o acumulador')
parser.add_argument('--sum', dest='acumulador', action='store_const',
                        const=sum, default=max,
                        help='Soma de inteiros (por default encontra o maximo)')

args = parser.parse_args()
print(args.acumulador(args.inteiros))