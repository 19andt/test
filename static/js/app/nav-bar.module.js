'use strict';

var app = angular.module('navBar', ['authentication', 'ui.bootstrap']);

app.component('navBar', {
        templateUrl: '/ang/templates/nav-bar.html'
    });

app.controller('navBarController', function($rootScope, $scope, $location, $window, searchTextService, authenticationService, logoutService) {
    $scope.authentication_data = authenticationService.check_authentication();
    console.log($scope.authentication_data);

    $scope.search_text = null
    $scope.search_counter = 0

    $scope.search_query = function(search_text){
        var query_results = searching(search_text);

        //return ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Dakota', 'North Carolina', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'];
        return query_results;
    }

    function searching(search_text){
        var url_params = angular.toJson({
            search_text: search_text,
        })

        var response = searchTextService.post(url_params)
        var result = response.$promise.then(function(data){
            return data.TopicList
        })

        return result;
    }

    $scope.selectItem = function($suggestion, $model, $label){
        $location.path('/topic/' + $label)
        $scope.search_text = ''
        //console.log('Selected:' + $suggestion)
    }

    $scope.logout_click = function(){
        logoutService.post({}, function(logout_status){
            console.log(logout_status);
            $window.location.href = '';
        });
    }
});