'use strict';

var app = angular.module('test', []);

app.component('test', {
        templateUrl: '/ang/templates/test.html'
    });

app.controller('testController', function($rootScope, $scope, authenticationService){
});