'use strict';

var app = angular.module('getComments', []);

app.service('getCommentsService', function($http, $resource){
    var url = '/comment/get_comments/:id'
    return $resource(url, {}, {
        get: {
            method: 'GET',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});