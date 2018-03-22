'use strict';

var app = angular.module('editInterest', []);

app.service('editInterestService', function($http, $resource){
    var url = '/interest/edit_interest/:topic_name'
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