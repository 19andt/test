'use strict';

var app = angular.module('getInterest', []);

app.service('getInterestService', function($http, $resource){
    var url = '/interest/get_interest'
    return $resource(url, {}, {
        get: {
            method: 'GET',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});