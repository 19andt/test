'use strict';

var app = angular.module('navBar', ['authentication', 'ui.bootstrap']);

app.component('navBar', {
        templateUrl: '/ang/templates/nav-bar.html'
    });

app.controller('navBarController', function($rootScope, $scope, $location, $window, $q, $timeout, searchTextService, authenticationService, logoutService, updateControllerService) {
    $scope.authentication_data = authenticationService.check_authentication();
    console.log($scope.authentication_data);

    $scope.search_text = null
    $scope.search_counter = 0

    $scope.search_query = function(search_text){
        var data = angular.toJson({
            search_text: search_text,
        })

        var result = null

        searchTextService.post(data, function(data){
            result = data.TopicList
        })

        var deferred = $q.defer();
        $timeout(function () { deferred.resolve( result ); }, Math.random() * 1000, false);
        return deferred.promise;
        //return ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Dakota', 'North Carolina', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'];
    }

    $scope.$on('UserLoggedIn', function(){
        $scope.authentication_data = authenticationService.check_authentication();
    })

    $scope.$on('UserLoggedOut', function(){
        $scope.authentication_data = authenticationService.check_authentication();
    })

    $scope.selectItem = function($suggestion, $model, $label){
        $location.path('/topic/' + $label)
        $scope.search_text = ''
    }

    $scope.search_click = function(){
        console.log('Entered here.')
        $location.path('/search-results/' + $scope.search_text)
        $scope.search_text = ''
    }

    $scope.logout_click = function(){
        logoutService.post({}, function(logout_status){
            console.log(logout_status);
            updateControllerService.user_logged_out();
            $window.location.href = '';
        });
    }
});