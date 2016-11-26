'use strict';

angular.module('contatosApp', [
    'ngRoute',  // Incluindo o modulo 'angular-route.js'
    'keepr'     // Incluindo o modulo 'angular-keepr.s'
])
.config(function ($routeProvider) {
    $routeProvider
    .when('/', {
        templateUrl: 'lista.html',
        controller: 'ContatosController'
    })
    .when('/contatos', {
        templateUrl: 'lista.html',
        controller: 'ContatosController'
    })
    .when('/contatos/novo', {
        templateUrl: 'novo.html',
        controller: 'contatosController'
    })
    .when('/contatos/:id/editar', {
        templateUrl: 'editar.html',
        controller: 'contatosController',
        method: 'editar'
    })
    .otherwise({
        redirectTo: '/'
    });
});