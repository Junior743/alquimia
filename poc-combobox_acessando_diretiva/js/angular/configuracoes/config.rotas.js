var $modulePrincipal = angular.module('modulePrincipal', ['ui.router', 'ngAnimate', 'ui.bootstrap']);

$modulePrincipal.config(function ($stateProvider, $urlRouterProvider) {
    // Rota padrao
    $urlRouterProvider.otherwise('/home');

    // Rotas
    $stateProvider
    .state('home', {
        url: '/home',
        templateUrl: 'index.html',
        controller: 'controllerHome'
    })
    .state('tevequianos', {
        url: '/tevequianos',
        templateUrl: 'tevequianos.html',
        controller: 'controllerTevequianos'
    })
    .state('feedback', {
        url: '/feedback',
        templateUrl: 'feedback.html',
        controller: 'controllerFeedBack'
    })
});