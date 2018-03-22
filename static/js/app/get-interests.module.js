'use strict';

var app = angular.module('getInterests', []);

app.service('getInterestsService', function($http, $resource){
    var url = '/interest/get_interests'
    return $resource(url, {}, {
        get: {
            method: 'GET',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});