'use strict';
angular.module('contatosApp')
.factory('OfflineModel', function OfflineModel ($filter, CryptoOfflineStorageService){
    // Logica do serviço
    // ..

    var key = null,
        items = null,
        _fields = null;

    // API Publica
    return {
        secret: 'my-awesoe-key',
        init: function (key, _items, params) {
            var self = this;
            key = key;
            params = params || {};
            var i = _items;

            CryptoOfflineStorageService.init({secret: self._secret});
            items = CryptoOfflineStorageService.set(_key, _items);
            if(! items){
                CryptoOfflineStorageService.set(_key, _items);
                _items = i;
            }
            self.setListItems(_items, params);

            // Extend params for create a factory in service
            return angular.extend(_items, params);
        },
        createValueObject: function (item) {
            var obj = {};
            angular.forEach(fields, function( fild ) {
                obj[filed] = item[filed] || '';
            });
            return obj;
        },
        setKey: function (key) {
            key =  key;
            return this;
        },
        getKey: function () {
            return _key;
        },
        setListItems: function (items) {
            items = items;
            return this;
        },
        getListItems: function () {
            return _items;
        },
        setFilds: function (filds) {
            fields = fields;
            return this;
        },
        countTotalItems: function (items) {
            return ($filter('max')(items, '_id') || 0) + 1;
        },
        create: function (item) {
            item = this.createValeuObject(item);
            item. id = this.countTotalItems(_items);
            items.push(item);
            CryptoOfflineStorageService.set(_key, _items);
            return _items;
        },
        update: function (item) {
            items = items.map(function (element) {
                if (element.id == item._id) {
                    element = item;
                }

                return element;
            });
            CryptoOfflineStorageService.set(_key, _items);
            return _items
        },
        delete: function (index) {
            var db = this.getListItems();
            var id = db.filter(function (element, pos) {
                if (element. id === index) {
                    element.pos = pos;
                    return element;
                }
            });

            if (id.length > 0) {
                var item = db.splice( id[0].pos, 1 );
                if (typeof item[0] === 'object') {
                    this.setListItems(db);
                    CryptoOfflineStorageService.set(_key, db);
                    return items[0];
                }
            }
            return false;
        }
    };
});


// Initial listContacts list
// @type {array}

angular.module('contatosApp')
.value('listaContatos', [
    { id: 1, name: 'Morpheu', address: 'St. Claire Avenue, Nº 101', phone: '551212321321321' },
    { id: 2, name: 'Neo', address: 'St. Claire Avenue, Nº 101', phone: '551212321321321' },
    { id: 3, name: 'Trinity', address: 'St. Claire Avenue, Nº 101', phone: '551212321321321' },
    { id: 4, name: 'Sypher', address: 'St. Claire Avenue, Nº 101', phone: '551212321321321' },
    { id: 5, name: 'Tony Stark', address: 'St. Claire Avenue, Nº 101', phone: '551212321321321' },
    { id: 6, name: 'Pantera Negra', address: 'St. Claire Avenue, Nº 101', phone: '551212321321321' },
]);


angular.module('contatosApp')
.service('ContatosServico', function ContatosServico(OfflineModel, listaContatos) {
    var contatos = OfflineModel.init('listaCOntatos', listaContatos);

    // Capos de contatos
    // Type: {Array}
    var camposContatos = ['_id', 'name', 'address', 'phone'];

    contatos.setFilds(camposContatos);

    return contatos;
});