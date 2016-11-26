var app = angular.module('app', ['ngAnimate']);

app.controller('controllerAnimacao', function ($scope){
    console.log('controllerAnimacao');

    var classeCssElementoFixo = 'displayNone'

    $scope.elemento = angular.element(document.querySelector('h3'));

    $scope.esconder = true;
    
    $scope.esconderConteudo = function () {
        $scope.animacao();
    }

    $scope.animacao = function () {
        if ($scope.esconder) {
            // $scope.elemento.style.opacity = 0;
            $scope.elemento.removeClass('opacidadeCem');
            $scope.elemento.addClass('opacidadeZero');

            setTimeout(function() {
                $scope.trocaDisplay();
            }, 500);
        } else {
            // $scope.elemento.style.opacity = 100;
            $scope.elemento.removeClass('opacidadeZero');
            $scope.elemento.addClass('opacidadeCem');

            setTimeout(function() {
                $scope.trocaDisplay();
            }, 0);
        }
    }

    $scope.trocaDisplay = function () {
        if ($scope.esconder) {
            $scope.elemento.addClass(classeCssElementoFixo);
        } else {
            $scope.elemento.removeClass(classeCssElementoFixo);
        }

        $scope.esconder = !$scope.esconder;
    }
});