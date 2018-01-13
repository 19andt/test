'use strict';

var app = angular.module('interestList', []);

app.component('interestList', {
        templateUrl: '/ang/templates/interest-list.html'
    });

app.controller('interestListController', function($rootScope, $scope, getInterestService){

    $scope.interest_list = ''

    get_interest_list();

    function get_interest_list(){
        getInterestService.get(function(data){
            if(data.UserAuthenticated){
                $scope.interest_list = data.InterestList;
            }
            else{
                $window.location.href = '';
            }
        });
    }
});