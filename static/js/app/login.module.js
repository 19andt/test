'use strict';

var app = angular.module('login', []);

app.service('loginService', function($http, $resource){
    var url = '/person/login'
    return $resource(url, {}, {
        post: {
            method: 'post',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});