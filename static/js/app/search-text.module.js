'use strict';

var app = angular.module('searchText', []);

app.service('searchTextService', function($http, $resource){
    var url = '/search'
    return $resource(url, {}, {
        post: {
            method: 'POST',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});