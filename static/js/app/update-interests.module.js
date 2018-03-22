'use strict';

var app = angular.module('updateInterests', []);

app.service('updateInterestsService', function($http, $resource){
    var url = '/interest/update_interests'
    return $resource(url, {}, {
        post: {
            method: 'POST',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});