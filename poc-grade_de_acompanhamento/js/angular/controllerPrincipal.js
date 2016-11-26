var $moduleApp = angular.module('app', []);

$moduleApp.controller('controllerPrincipal', function ($scope) {

    ///////////////////////
    // VARIAVEIS
    ///////////////////////

    // Inicializando variaveis
    $scope.dias_do_mes = [];
    $scope.dias_da_semana_do_mes = [];
    $scope.dias_de_acompanhamento = [];
    $scope.dias_de_acompanhamento = [];

    ///////////////////////
    // SCOPES
    ///////////////////////
    
    // Grades //
    var dias_de_acompanhamento = {
        pdms: [{
            id: undefined,
            data_pedido: [],
            data_entrega: [],
            data_faturamento: []
        }]
    }
    
    $scope.grades_por_ponto_movimentacao = {
        grades:[{
            id: 1,
            nome: 'PdM Um',
            datas: [{
                id: 1,
                data_faturamento: '04/01/2015',
                data_entrega: '03/01/2015',
                data_pedido: '01/01/2015'
            }, {
                id: 2,
                data_faturamento: '07/01/2015',
                data_entrega: '06/01/2015',
                data_pedido: '05/01/2015'
            }]
        }, {
            id: 2,
            nome: 'PdM Dois',
            datas: [{
                id: 1,
                data_faturamento: '04/01/2015',
                data_entrega: '03/01/2015',
                data_pedido: '01/01/2015'
            }, {
                id: 2,
                data_faturamento: '07/01/2015',
                data_entrega: '06/01/2015',
                data_pedido: '05/01/2015'
            }, {
                id: 3,
                data_faturamento: '07/01/2015',
                data_entrega: '06/01/2015',
                data_pedido: '05/01/2015'
            }, {
                id: 4,
                data_faturamento: '07/01/2015',
                data_entrega: '06/01/2015',
                data_pedido: '05/01/2015'
            }
            ]
        }, {
            id: 3,
            nome: 'PdM Três',
            datas: [{
                id: 1,
                data_faturamento: '04/01/2015',
                data_entrega: '03/01/2015',
                data_pedido: '01/01/2015'
            }, {
                id: 2,
                data_faturamento: '07/01/2015',
                data_entrega: '06/01/2015',
                data_pedido: '05/01/2015'
            }
            ]
        }]
    }

    // Datas //
    $scope.meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
    $scope.mesesString = ['Janeiro', 'Fevereiro', 'Marco', 'Maio', 'Abril', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'];
    $scope.dias_da_semana = ['Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo']
    $scope.dias_da_semana_abreviado = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']


    ///////////////////////
    // CONSTRUTOR
    ///////////////////////

    // Populando os dias do mes
    var mes_atual = new Date();
    GetDiasDoMes(mes_atual.getMonth(), false);

    // Populando os dias da semana do mes
    GetDiasDaSemanaDoMes($scope.dias_do_mes);

    // Populando os dias de acompanhamento
    CarregarDias($scope.grades_por_ponto_movimentacao.grades);


    ///////////////////////
    // METODOS
    ///////////////////////
    function GetDiasDoMes(_mes, _ano_bissexto) {
        if (_mes == 0) { $scope.dias_do_mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]; }
        else if (_mes == 1) {
            if (_ano_bissexto) { $scope.dias_do_mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]; }
            else { $scope.dias_do_mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]; }
        }
        else if (_mes == 2) { $scope.dias_do_mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]; }
        else if (_mes == 3) { $scope.dias_do_mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]; }
        else if (_mes == 4) { $scope.dias_do_mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]; }
        else if (_mes == 5) { $scope.dias_do_mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]; }
        else if (_mes == 6) { $scope.dias_do_mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]; }
        else if (_mes == 7) { $scope.dias_do_mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]; }
        else if (_mes == 8) { $scope.dias_do_mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]; }
        else if (_mes == 9) { $scope.dias_do_mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]; }
        else if (_mes == 10) { $scope.dias_do_mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]; }
        else if (_mes == 11) { $scope.dias_do_mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]; }
    }
    
    function GetDiasDaSemanaDoMes(_dias_do_mes) {
        for(i = 0, j = 0; i < _dias_do_mes.length; i++, j++) {
            if (j == 7) j = 0;

            $scope.dias_da_semana_do_mes[i] = {'valor': $scope.dias_da_semana_abreviado[j]};
        }
    }

    function CarregarDias(_pdm_dados) {
        _pdm_dados.forEach(function(pdm, i) {

            dias_de_acompanhamento.pdms.id = pdm.id;

            pdm.datas.forEach(function(d, j) {
                if (d.data_pedido != null) dias_de_acompanhamento.pdms.data_pedido = d.data_pedido.split('/')[0];
                if (d.data_entrega != null) dias_de_acompanhamento.pdms.data_entrega = d.data_entrega.split('/')[0];
                if (d.data_faturamento != null) dias_de_acompanhamento.pdms.data_faturamento = d.data_faturamento.split('/')[0]; 

            });
        });

        $scope.dias_de_acompanhamento = dias_de_acompanhamento;

        alert(dias_de_acompanhamento.pdms.data_pedido.indexOf(05)); 

    }
});
