'use strict';

var app = angular.module('credentials', []);

app.component('credentials', {
        templateUrl: '/ang/templates/credentials.html'
    });

app.controller('credentialsController', function($rootScope, $scope, $window, $route, userProfileService, authenticationService){
    $scope.email = '';
    $scope.password = '';
    $scope.confirm_password = '';
    $scope.password_incorrect = false;

    check_authentication();

    $scope.save = function(value){
        if(value == 'email'){
            var url_params = {
                username: $scope.authentication_data.User.username
            }

            var data = angular.toJson({
                email: $scope.email
            });

            userProfileService.post(url_params, data, function(data){
                console.log(data)
                if(data.UpdateStatus == true){
                    alert('Email changed successfully.\n\nLogin again....')

                    $window.location.href = '/';
                }
            })
        }else{
            var url_params = {
                username: $scope.authentication_data.User.username
            }

            var data = angular.toJson({
                password: $scope.password
            });

            userProfileService.post(url_params, data, function(data){
                console.log(data)
                if(data.UpdateStatus == true){
                    alert('Password changed successfully.\n\nLogin again....')

                    $window.location.href = '/';
                }
            })
        }
    }

    $scope.$watch('password', function(newValue, oldValue){
        if(newValue == $scope.confirm_password && newValue != '' && newValue.length >= 8){
            $scope.password_incorrect = false;
        }else{
            $scope.password_incorrect = true;
        }
    });

    $scope.$watch('confirm_password', function(newValue, oldValue){
        if(newValue == $scope.password && newValue != '' && newValue.length >= 8){
            $scope.password_incorrect = false;
        }else{
            $scope.password_incorrect = true;
        }
    });

    function check_authentication(){
        console.log('Function Entered.');
        $scope.authentication_data = authenticationService.check_authentication();

        if($scope.authentication_data.UserAuthenticated == false && $scope.authentication_data.SuperUser == false){
            $window.location.href = '/';
        }
    }
});