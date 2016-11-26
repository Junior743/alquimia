$aplicacao_tevec.directive('tevecItemFixoDinamico', function () {
    return {
        restrict: 'A',
        link: function ($scope, $element, $attrs) {

            var ultimoElementoVisivel = undefined;
            var scrollTopPadrao = undefined;
            var medidaTopElemento = undefined;

            $element.bind('scroll', function (e) {
                $scope.fixarCabecalho(e);
            });

            $scope.fixarCabecalho = function (e) {
                
                var elementoExpandido = undefined;
                var indexElementoAnterior = undefined;
                var indexElementoSelecionado = undefined;
                var indexElementoProximo = undefined;
                var elementoPai = undefined;
                var alturaElementoCorrente = 0;
                var elementosFilho = [];
                
                elementoPai = angular.element(document.querySelector('#tvc_accordion'));
                elementosFilho = elementoPai.children();
                elementosFilho = elementosFilho.children();

                elementoPai = e.path[0];

                scrollTopPadrao = scrollTopPadrao == undefined ? elementoPai.scrollTop : scrollTopPadrao;

                for (var i = 0; i < elementosFilho.length; i++) {

                    alturaElementoCorrente = elementoExpandido == undefined ? 
                                            ((alturaElementoCorrente + elementosFilho[0].children[0].clientHeight) + 3) : alturaElementoCorrente;

                    if (elementosFilho[i].classList.contains('panel-open')) {
                        indexElementoSelecionado = i;
                        elementoExpandido = elementosFilho[i].children;
                        elementoExpandido = elementoExpandido[0];
                    }
                }

                if (elementoExpandido != undefined) {
                    elementoExpandido.style.top = ((elementoPai.scrollTop - alturaElementoCorrente) + elementoExpandido.clientHeight) + "px";

                    if (elementosFilho[(indexElementoSelecionado - 1)] == undefined) {
                        if (elementosFilho[(indexElementoSelecionado + 1)] != undefined) {
                            indexElementoProximo = (indexElementoSelecionado+1);
                        }
                    } else {
                        if (elementosFilho[(indexElementoSelecionado + 1)] == undefined) {
                            indexElementoAnterior = (indexElementoSelecionado-1);
                        } else if (elementosFilho[(indexElementoSelecionado + 1)] != undefined) {
                            indexElementoAnterior = (indexElementoSelecionado-1);
                            indexElementoProximo = (indexElementoSelecionado+1);
                        }
                    }


                    if (ultimoElementoVisivel == undefined) {
                        ultimoElementoVisivel = elementoExpandido;
                    } else if (ultimoElementoVisivel != elementoExpandido) {
                        elementoExpandido.classList.remove("headAccordionFixo");
                        ultimoElementoVisivel = elementoExpandido;
                    }
                    
                    if (indexElementoAnterior == undefined) {
                        if (indexElementoProximo == undefined) {
                            elementoExpandido.classList.add("headAccordionFixo");
                        } else {
                            medidaTopElemento = (ultimoElementoVisivel != elementoExpandido) || (medidaTopElemento == undefined) ? 
                                                    elementosFilho[indexElementoProximo].offsetTop : medidaTopElemento;
                            var medidaSuperior = (medidaTopElemento - elementoPai.scrollTop) - elementoExpandido.clientHeight;

                            if (medidaSuperior <= elementoPai.clientHeight) {
                                elementoExpandido.classList.remove("headAccordionFixo");
                            } else {
                                elementoExpandido.classList.add("headAccordionFixo");
                            }
                        }

                        if (elementoPai.scrollTop <= scrollTopPadrao) {
                            elementoExpandido.classList.remove("headAccordionFixo");
                        }

                    } else {

                        if (indexElementoProximo == undefined) {
                            var medidaInferior = (elementosFilho[indexElementoAnterior].offsetTop - elementoPai.scrollTop);
                            
                            if (medidaInferior >= 0) {
                                elementoExpandido.classList.remove("headAccordionFixo");
                            } else {
                                elementoExpandido.classList.add("headAccordionFixo");
                            }
                        } else {

                            medidaTopElemento = (ultimoElementoVisivel != elementoExpandido) || (medidaTopElemento == undefined) ? 
                                                    elementosFilho[indexElementoProximo].offsetTop : medidaTopElemento;
                            var medidaSuperior = (medidaTopElemento - elementoPai.scrollTop) - elementoExpandido.clientHeight;
                            var medidaInferior = (elementosFilho[indexElementoAnterior].offsetTop - elementoPai.scrollTop);  

                            if ((medidaSuperior <= elementoPai.clientHeight) || medidaInferior >= 0) {
                                elementoExpandido.classList.remove("headAccordionFixo");
                            } else {
                                elementoExpandido.classList.add("headAccordionFixo");
                            }
                        }
                    }
                } else {
                    for (var i = 0; i < elementosFilho.length; i++) {
                        elementosFilho[i].children[0].classList.remove("headAccordionFixo");
                    }
                }
            }
        }
    }
});