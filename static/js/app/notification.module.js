'use strict';

var app = angular.module('notification', []);

app.service('notificationService', function($http, $resource){
    var url = '/notification'
    return $resource(url, {}, {
        get: {
            method: 'get',
            params: {},
            isArray: false,
            cache: false,
        },
        post: {
            method: 'post',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});