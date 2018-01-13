'use strict';

var app = angular.module('navBar', ['authentication']);

app.component('navBar', {
        templateUrl: '/ang/templates/nav-bar.html'
    });

app.controller('navBarController', function($rootScope, $scope, $location, $window, authenticationService, logoutService) {
    $scope.authentication_data = authenticationService.check_authentication();
    console.log($scope.authentication_data);

    $scope.logout_click = function(){
        logoutService.post({}, function(logout_status){
            console.log(logout_status);
            $window.location.href = '';
        });
    }
});