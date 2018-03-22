'use strict';

var app = angular.module('interestList', []);

app.component('interestList', {
        templateUrl: '/ang/templates/interest-list.html'
    });

app.controller('interestListController', function($rootScope, $scope, getInterestsService){

    $scope.interest_list = ''

    get_interest_list();

    $scope.$on('InterestsUpdated', function(){
        get_interest_list();
    })

    function get_interest_list(){
        getInterestsService.get(function(data){
            if(data.UserAuthenticated){
                $scope.interest_list = data.InterestList;
            }
            else{
                $window.location.href = '';
            }
        });
    }
});