'use strict';

var app = angular.module('oauth', []);

app.component('oauth', {
        templateUrl: '/ang/templates/oauth.html'
    });

app.controller('oauthController', function($routeParams, $window){
    $window.location.href='/all_auth/' + $routeParams.provider + '/login/';
});