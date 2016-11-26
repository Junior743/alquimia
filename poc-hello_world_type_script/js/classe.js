var Estudante = (function () {
    function Estudante(nome, sobrenome) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.nomeCompleto = nome + ' ' + sobrenome;
    }
    return Estudante;
}());
function comunicador(person) {
    return 'Hello ' + person.nome + ' ' + person.sobrenome;
}
var usuario = new Estudante('Penny', 'Lane');
document.body.innerHTML = comunicador(usuario);
