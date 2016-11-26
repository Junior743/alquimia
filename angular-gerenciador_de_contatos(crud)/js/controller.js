'use strict';

angular.module('contatosApp')
.controller('ContatosController', function ($scope, $location, $route, $filter, ServicoDeAlerta, ContatosService) {
    // Valor inicial dos formulários de inserção/alteração de contatosApp
    // @type: {Array}
    $scope.contato = [];

    // Reinicia o valor dos campos do formulário com os valores vazios
    $scope.reset = function () {
        $scope.contato = [
            {
                name: '',
                address: '',
                phone: '',
            }
        ];
    };

    // Retorna a quantidade de contatos
    // @return {int}
    $scope.numeroDePaginas = function () {
        return Math.ceil($scope.filteredData.length/$scope.pageSize);
    };

    // Insere um contato
    $scope.create = function () {
        $scope.listaContatos = ContatosServico.create(contato);
    };

    // Retorna um contato especifico selecionado para ser editado
    $scope.edit = function () {
        var id = $routeParams.id;
        $scope.contato = $filter('filter')($scope.listaContatos, {_id: id})[0];
        window.scrollTo(0, 0);
    };

    // Altera um contato
    // @param {object} item informações do contato
    $scope.update = function (item) {
        $scope.listaContatos = ContatosService.update(item);
    };

    // Abstração dos métodos de inserir/alterar
    // @param {object} item informações do contato
    $scope.save = function (item) {
        if(typeof item.id !== 'undefined') {
            $scope.update(item);
        }
        else {
            $scope.create(item);
        }
        $scope.reset();
        $location.path('/contatos');
    };

    // Remove um contato da lista de contatos
    // @param {integer} index - valor do 'id' do contato
    // @param {boolean} confirmacao - verificação de chamada da função 'window.confirm()' na aplicação
    // return {boolean}
    $scope.delete = function (index, confirmacao) {
        confirmacao = (typeof confirmacao !== 'undefined') ? confirmacao: true;
        if(confirmDelete(confirmacao)) {
            var mensagem,
                item = ContatosServico.delete(index);
            if(!!item) {
                mensagem = 'O contato "' + item.name + '" com id "' + item._id + '" foi removido de sua lista de contatos ';
                ServicoDeAlerta.add('sucess', mensagem, 5000);
                $scope.listaContatos = ContatosService.getListItems();
                return true;
            }
            AlertService.add('error', 'Houston, we have a problem. This operation cannot be executed correctly.', 5000);
            return false;
        }
        AlertService.add('error', 'Houston, we have a problem. This operation cannot be executed correctly.', 5000);
        return false;
    }
});