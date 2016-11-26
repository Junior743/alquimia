interface Person {
    nome: string;
    sobrenome: string;
}

function comunicador(person: Person) {
    return 'Hello, ' + person.nome + ' ' + person.sobrenome;
}

var usuario = { nome: 'Penny', sobrenome: 'Lane' };
document.body.innerHTML = comunicador(usuario);