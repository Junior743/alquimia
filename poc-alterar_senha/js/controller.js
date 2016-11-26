var $alterarSenha = angular.module('AlterarSenha', ['ui.router', 'ngAnimate', 'ui.bootstrap', 'angular-md5']);

// Cria o token
$alterarSenha.controller('EnviaTokenController', function ($scope, md5) {
    $scope.EnviarToken = function () {
        var email = $scope.user.email;
        var dataAtual = new Date();
        dataAtual = "" + dataAtual.getDay() + dataAtual.getMonth() + dataAtual.getFullYear() + dataAtual.getSeconds(); // dataAtual.getHours()
        var md5Email, md5DataAtaul;

        $scope.$watch('email', function() {
            $scope.message = "Seu email ficou assim: " + md5.createHash(email || '');
            md5Email = md5.createHash(email || '');
            md5DataAtaul = md5.createHash(dataAtual || '');

            alert(md5Email + "-" + md5DataAtaul);
            
            //return md5Email + "-" + md5DataAtaul; // Talvez separar os valores pelo valor de pi envolvido por algum padrão de letras
        });
    };
});