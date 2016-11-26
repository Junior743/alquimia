class Estudante {
    nomeCompleto: string;

    constructor(public nome, public sobrenome) {
        this.nomeCompleto = nome + ' ' + sobrenome;
    }
}

interface Person {
    nome: string;
    sobrenome: string;
}

function comunicador(person: Person) {
    return 'Hello ' + person.nome + ' ' + person.sobrenome;
}

var usuario = new Estudante('Penny', 'Lane');
document.body.innerHTML = comunicador(usuario);