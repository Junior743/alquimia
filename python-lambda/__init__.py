## Uma expressão lambda eh uma funcao anonima
## () = lambda

## EXEMPLO 1
## uma funcao que espera x como argumento e devolve 3x+1
def f(x):
    return 3*x+1
function_value = f(3)

## uma expressão lambda que devolve 3x+1
lambda_value = lambda x: 3+x+1

print("Valor função: {}\n" \
    "Valor lambda: {}". \
    format(function_value, lambda_value))

## EXEMPLO 2
## formatando duas entradas nome e sobrenome
first_name = "   carlos Henrique "
last_name = "de sousa    jUniOR "

full_name_formated = lambda x, y: x.strip().title() + " " + y.strip().title()
print("Nome completou: {}".format(full_name_formated))

## EXEMPLO 3
## ordenando uma cadeia de nomes e numeros
names = ["Sydney Magal", "José Lopes", "Jeniffer Santos", "Lacerda Over", "Larissa Melissa", "Manuela Folguer"]
numbers = [1, 344, 34, 123, 54, 1, 56, 3, 76, 23, 56, 3452, 45, 123, 546]
names_and_numbers = names
names_and_numbers.extend(numbers)

## WHT? So good, no?
# print(help(names.sort))

names_sorted = names.sort()
print(names_sorted[1])

## EXEMPLO 4