var $myApp = angular.module('my-app-login',  ['ui.router', 'ngAnimate', 'ui.bootstrap']);

$myApp.config(function($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/login');
    
    $stateProvider
    
        .state('login', {
            url: '/login',
            templateUrl: 'login.html',
            controller: 'LoginController'
        })
        .state('confirma_email', {
            url: '/confirma_email',
            templateUrl: 'confirma_email.html',
            controller: 'ConfirmaEmailController'
        })

        .state('alterar_senha', {
            url: '/alterar_senha/{token}',
            templateUrl: 'alterar_senha.html',
            controller: 'AlterarSenhaController'
        })
});

$myApp.controller('LoginController', function($scope) {
    // Metodos da tela de login.html
});

$myApp.controller('ConfirmaEmailController', function($scope) {
    $myApp.config(function($stateProvider, $urlRouterProvider) {
        $urlRouterProvider.otherwise('/login');
        
        var nova_senha = user.rsSenha;
        var nova_senha_confirmar = user.rsSenhaConfirmar;

        if(nova_senha == nova_senha_confirmar) {
            $stateProvider

            // Chamada da função para alterar senha

            .state('login', {
                url: '/login',
                template: 'Sua senha foi alterada com sucesso'
            })

            // Redirect para a tela de login

            // Tratamento de erro
        }
        else {
            $stateProvider
        
            .state('login', {
                url: '/login',
                template: 'Tente novamente. As senhas não correspondem.'
            })
        }
    });
});

$myApp.controller('AlterarSenhaController', function($scope, $stateParams) {
    var token = $stateParams.token + "";
    var token = token.split("-");

    var emailToken = token[0];  
    var dataToken = token[1];
    
    alert(emailToken + " ---- " + dataToken);

    if (emailToken == "verificar se existe no banco") { // Valida o email do usuario
        if (dataToken == "Verificar se a data ainda é valida") { // Valida se não foi gerado outro token
            if ("Validar data atual com data do banco, tem que ter diferença de no maximo 1 hora por exemplo"){ // Valida se o token não expirou
            }
        }
    }
});
