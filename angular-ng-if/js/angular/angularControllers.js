var myApp = angular.module('myApp', ['ui.router', 'ngAnimate', 'ui.bootstrap']);

myApp.controller('myController', function ($scope) {
    $scope.variavelTeste = "sectionThree";

    $scope.AlterarValor = function () {
        alert($scope.valor);

        $scope.variavelTeste = $scope.valor; 
    }
});