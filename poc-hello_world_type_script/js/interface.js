function greenter(person) {
    return 'Hello, ' + person.nome + ' ' + person.sobrenome;
}
var usuario = { nome: 'Penny', sobrenome: 'Lane' };
document.body.innerHTML = greenter(usuario);
