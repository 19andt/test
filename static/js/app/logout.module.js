'use strict';

var app = angular.module('logout', []);

app.service('logoutService', function($resource){
    var url = '/person/logout'
    return $resource(url, {}, {
        post: {
            method: 'post',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});