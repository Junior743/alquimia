var moduloApp = angular.module('App', []);

moduloApp.directive('diretivaAcessar', function () {
    return {
        restrict: 'A',
        link: function ($scope, element, attrs) {
            alert("Entrei na diretiva");

            $scope.Entrar = function () {
                alert("Entrei na função da diretiva");
            }

            $scope.EntrarEmOutraFuncao = function () {
                alert("Entrei em outra função da diretiva");
            }
        }
    }
});