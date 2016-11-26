var moduloApp = angular.module('App', []);

moduloApp.directive('tevecItemFixoDinamico', function () {
    return {
        restrict: 'A',
        link: function ($scope, element, attrs) {

            var varPai = element.find("div");
            var UltimoObjetoVisivel = undefined;
            var ScrollTopPadrao = undefined;

            varPai.bind('scroll', function (e) {
                $scope.comparacao(e);
            });

            $scope.comparacao = function (e) {
                var varFilhos = varPai.find("h3");
                var itemSelecionado = undefined;
                var indexFilhoSelecionado = undefined;
                var itemAnterior = undefined;
                var itemCorrente = undefined;
                var itemProximo = undefined;
                var indexFilhoAnterior = undefined;
                var indexFilhoProximo = undefined;
                var classeElemento = undefined;
                var listaObjetosInvisiveis = [];
                var listaObjetosVisiveis = [];
                var listaIndeces = [];
                var elementoFixo = false;

                ScrollTopPadrao = ScrollTopPadrao == undefined ? varPai[0].scrollTop : ScrollTopPadrao;    

                var elemento = element.find("h3");

                for (var i = 0; i < varFilhos.length; i++) {
                    var elementoSelecionado = elemento[i].attributes['aria-expanded'];

                    if (elementoSelecionado.value == 'true') {
                        itemSelecionado = elemento[i];
                        indexFilhoSelecionado = i;
                    }
                }

                if (elemento[(indexFilhoSelecionado - 1)] == undefined) {

                    if (elemento[(indexFilhoSelecionado + 1)] == undefined) {

                            itemCorrente = elemento[indexFilhoSelecionado];

                    } else if (elemento[(indexFilhoSelecionado + 1)] != undefined) {

                        itemCorrente = elemento[indexFilhoSelecionado];
                        itemProximo = elemento[(indexFilhoSelecionado+1)];
                        indexFilhoProximo = (indexFilhoSelecionado+1);
                        listaIndeces = [indexFilhoSelecionado, indexFilhoSelecionado+1];
                        
                        for (var i = 0; i < listaIndeces.length; i++) {
                            
                            var elementoPosicaoSuperior = (elemento[listaIndeces[i]].offsetTop - elemento[listaIndeces[i]].clientHeight) - varPai[0].scrollTop;   
                            var elementoPosicaoInferior = elemento[listaIndeces[i]].offsetTop - varPai[0].scrollTop;

                            if (elementoFixo) {
                                listaObjetosVisiveis.push(elemento[listaIndeces[i]]);
                            }

                            if (elementoPosicaoSuperior <= 0 || elementoPosicaoInferior >= varPai[0].clientHeight) {
                                listaObjetosInvisiveis.push(elemento[listaIndeces[i]]);
                            } else {
                                listaObjetosVisiveis.push(elemento[listaIndeces[i]]);
                            }

                        }

                    }

                } else {

                    if (elemento[(indexFilhoSelecionado + 1)] == undefined) {

                        itemAnterior = elemento[(indexFilhoSelecionado-1)];
                        itemCorrente = elemento[indexFilhoSelecionado];
                        indexFilhoAnterior = (indexFilhoSelecionado-1);
                        listaIndeces = [indexFilhoSelecionado-1, indexFilhoSelecionado];

                        for (var i = 0; i < listaIndeces.length; i++) {
                            
                            var elementoPosicaoSuperior = (elemento[listaIndeces[i]].offsetTop - elemento[listaIndeces[i]].clientHeight) - varPai[0].scrollTop;   
                            var elementoPosicaoInferior = elemento[listaIndeces[i]].offsetTop - varPai[0].scrollTop;

                            if (elementoFixo) {
                                listaObjetosVisiveis.push(elemento[listaIndeces[i]]);
                            }

                            if (elementoPosicaoSuperior <= 0 || elementoPosicaoInferior >= varPai[0].clientHeight) {
                                listaObjetosInvisiveis.push(elemento[listaIndeces[i]]);
                            } else {
                                listaObjetosVisiveis.push(elemento[listaIndeces[i]]);
                            }

                        }

                    } else if (elemento[(indexFilhoSelecionado + 1)] != undefined) {

                        itemAnterior = elemento[(indexFilhoSelecionado-1)];
                        itemCorrente = elemento[indexFilhoSelecionado];
                        itemProximo = elemento[(indexFilhoSelecionado+1)];
                        indexFilhoAnterior = (indexFilhoSelecionado-1);
                        indexFilhoProximo = (indexFilhoSelecionado+1);
                        listaIndeces = [indexFilhoSelecionado-1, indexFilhoSelecionado, indexFilhoSelecionado+1];

                        for (var i = 0; i < listaIndeces.length; i++) {
                            
                            var elementoPosicaoSuperior = (elemento[listaIndeces[i]].offsetTop - elemento[listaIndeces[i]].clientHeight) - varPai[0].scrollTop;   
                            var elementoPosicaoInferior = elemento[listaIndeces[i]].offsetTop - varPai[0].scrollTop;

                            if (elementoFixo) {
                                listaObjetosVisiveis.push(elemento[listaIndeces[i]]);
                            }

                            if (elementoPosicaoSuperior <= 0 || elementoPosicaoInferior >= varPai[0].clientHeight) {
                                listaObjetosInvisiveis.push(elemento[listaIndeces[i]]);
                            } else {
                                listaObjetosVisiveis.push(elemento[listaIndeces[i]]);
                            }

                        }

                    }

                }



                if (UltimoObjetoVisivel == undefined) {
                    UltimoObjetoVisivel = itemCorrente;
                } else if (UltimoObjetoVisivel != itemCorrente) {

                    classeElemento = UltimoObjetoVisivel.attributes["class"];
                    classeElemento.value = "";

                    UltimoObjetoVisivel = itemCorrente;
                }

                if (indexFilhoAnterior == undefined) {

                    if (indexFilhoProximo == undefined) {

                        classeElemento = itemCorrente.attributes["class"];
                        classeElemento.value = "headAccordionFixo";

                    } else {

                        var medidaSuperior = ((elemento[indexFilhoProximo].offsetTop) - varPai[0].scrollTop);

                        if (medidaSuperior <= varPai[0].clientHeight) {
                            classeElemento = itemCorrente.attributes["class"];
                            classeElemento.value = "";
                        } else {
                            classeElemento = itemCorrente.attributes["class"];
                            classeElemento.value = "headAccordionFixo";
                        }

                    }

                    if (varPai[0].scrollTop <= ScrollTopPadrao) {
                        classeElemento = itemCorrente.attributes["class"];
                        classeElemento.value = "";
                    }

                } else {

                    if (indexFilhoProximo == undefined) {

                        var medidaInferior = (elemento[indexFilhoAnterior].offsetTop - varPai[0].scrollTop);
                        
                        if (medidaInferior >= 0) {
                            classeElemento = itemCorrente.attributes["class"];
                            classeElemento.value = "";
                        } else {
                            classeElemento = itemCorrente.attributes["class"];
                            classeElemento.value = "headAccordionFixo";
                        }

                    } else {

                        var medidaSuperior = ((elemento[indexFilhoProximo].offsetTop) - (varPai[0].scrollTop - elemento[indexFilhoProximo].clientHeight));
                        var medidaInferior = (elemento[indexFilhoAnterior].offsetTop - varPai[0].scrollTop);  

                        if ((medidaSuperior <= varPai[0].clientHeight) || medidaInferior >= 0) {
                            classeElemento = itemCorrente.attributes["class"];
                            classeElemento.value = "";
                        } else {
                            classeElemento = itemCorrente.attributes["class"];
                            classeElemento.value = "headAccordionFixo";
                        }

                    }
                }
            }
        }
    }
});
