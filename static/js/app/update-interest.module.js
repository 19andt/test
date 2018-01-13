'use strict';

var app = angular.module('updateInterest', []);

app.service('updateInterestService', function($http, $resource){
    var url = '/interest/update_interest'
    return $resource(url, {}, {
        post: {
            method: 'POST',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});