'use strict';

var app = angular.module('addUser', []);

app.service('addUserService', function($resource){
    var url = '/person/add_user'
    return $resource(url, {}, {
        post: {
            method: 'post',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});