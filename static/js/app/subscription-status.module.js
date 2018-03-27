'use strict';

var app = angular.module('subscriptionStatus', []);

app.service('subscriptionStatusService', function($http, $resource){
    var url = '/subscription/subscription_status/:username'
    return $resource(url, {}, {
        get: {
            method: 'GET',
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