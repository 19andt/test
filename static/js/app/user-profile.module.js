'use strict';

var app = angular.module('userProfile', []);

app.service('userProfileService', function($resource){
    var url = '/person/profile/:username'
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