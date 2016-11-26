(function () {
    var myApp = angular.module('myApp', ['ui.router', 'ngAnimate', 'ui.bootstrap']);
    
    myApp.directive('controleAcesso', function () {
        return {
            restrict: 'A',
            link: function ($scope, element, attrs) {
                if (attrs.controleAcesso === 'bloqueado') {
                    element.attr('disabled', 'disabled');
                    //element.append('<h1>O elemento foi bloqueado!</h1>');
                }
            }
        };
    });
})();