'use strict';

var app = angular.module('userAuthentication', []);

app.component('userAuthentication', {
        templateUrl: '/ang/templates/user-authentication.html'
    });

app.controller('userAuthenticationController', function($rootScope, $scope, $window, addUserService, loginService){
    $scope.gender_list = ['Male', 'Female', 'Not interested to tell']
    $scope.type_list = ['Individual', 'Company']

    $scope.registration = {
        name: '',
        gender: '',
        email: '',
        mobile: '',
        type: '',
        password: '',
        confirmPassword: '',
        tos: false
    }
    $scope.login = {
        email: '',
        password: '',
    }
    $scope.show_registration_error = false
    $scope.show_login_error = false

    $scope.registration_click = function(){
        var registration_data = angular.toJson({
            full_name: $scope.registration.name,
            gender: $scope.registration.gender,
            email: $scope.registration.email,
            mobile_number: $scope.registration.mobile,
            type: $scope.registration.type,
            password: $scope.registration.password,
        })

        console.log(registration_data)
        addUserService.post(registration_data, function(registration_status){
            console.log(registration_status);

            if(registration_status.AddUserStatus == false){
                $scope.show_registration_error = true;
            }
            else{
                $window.location.href = '';
            }
        });
    }

    $scope.login_click = function(){
        var login_data = angular.toJson({
            email: $scope.login.email,
            password: $scope.login.password,
        })

        console.log(login_data)
        loginService.post(login_data, function(login_status){
            console.log(login_status)

            if(login_status.LoginUserStatus == false){
                $scope.show_login_error = true;
            }
            else{
                $window.location.href = '/interest';
            }
        });
    }
})
.directive('passwordVerify', function(){
    return {
        restrict: 'A',
        require: '?ngModel',
        link: function(scope, elem, attrs, ngModel){
            if(!ngModel) return;

            scope.$watch(attrs.ngModel, function(){
                validate();
            });

            attrs.$observe('passwordVerify', function(val){
                validate();
            })

            var validate=function(){
                var val1=ngModel.$viewValue;
                var val2=attrs.passwordVerify;

                ngModel.$setValidity('passwordVerify', val1===val2);
            };
        }
    }
});