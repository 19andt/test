'use strict';

var app = angular.module('getSubscriptionList', []);

app.service('getSubscriptionListService', function($http, $resource){
    var url = '/subscription/get_subscription_list'
    return $resource(url, {}, {
        get: {
            method: 'GET',
            params: {},
            isArray: false,
            cache: false,
        }
    });
});