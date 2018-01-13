'use strict';

var app = angular.module('checkAuthentication', []);

app.service('checkAuthenticationService', function($http, $resource){
    var url = '/person/check_authentication'
    return $resource(url, {}, {
        get: {
            method: 'GET',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});