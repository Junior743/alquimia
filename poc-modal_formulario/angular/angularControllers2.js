var $myApp = angular.module('AbrirModal',  ['ngAnimate', 'ui.bootstrap']);

$myApp.controller('ModalDemoCtrl', function ($scope, $uibModal, $log) {
    $urlRouterProvider.otherwise('/login');
    
    $stateProvider
        
        $stateProvider
        
        // HOME STATES AND NESTED VIEWS ========================================
        .state('login', {
            url: '/login',
            templateUrl: 'login.html'
        })

        // nested list with custom controller
        .state('alterar_senha', {
            url: '/alterar_senha',
            templateUrl: 'alterar_senha.html'
        })

        // nested list with just some random string data
        .state('confirma_email', {
            url: '/confirma_email',
            template: 'confirma_email.html'
        })
        
        // ABOUT PAGE AND MULTIPLE NAMED VIEWS =================================
        // .state('about', {
        //     // we'll get to this in a bit       
        // });
        
         
    // $scope.Open = function () {
    //     var modalInstance = $uibModal.open({
    //     animation: true,
    //     templateUrl: 'modalFormulario.html',
    //     size: 'lg'
    // });
    
    // modalInstance.result.then(function (selectedItem) {
    //     $scope.selected = selectedItem;
    // }, function () {
    //     $log.info('Modal dismissed at: ' + new Date());
    // });
    // };
    
    // //$scope.ValidacaoEmail = 

    // $scope.toggleAnimation = function () {
    //     $scope.animationsEnabled = !$scope.animationsEnabled;
    // };
    
    // $scope.email = "teste@teste.com.br";
});

// Se for implementar outro modal
$myApp.controller('modalInstanceCtrl',['$scope', '$uibModal', '$log', function ($scope, $uibModal, $log/*, $valida_email*/) {
    $scope.EnviarToken = function () {$scope, $uibModal, $log
        // Pegando o valor do input email de recuperar senha
        var textoEmail = $scope.user.rsEmail;
        
        // Analisa o e-mail e devolve o valor em uma variavel
        validacao = ValidacaoEmail(textoEmail);
        
        // Validacao do e-mail
        if (validacao) {
            enviarToken = EnviarToken(textoEmail, tempo /* e etc... */);
            $scope.esconder = true;
        }
        else {
            $scope.esconder = false;
        }
    };
}]);

function ValidacaoEmail(textoEmail) {
    return true;
}