'use strict';

var app = angular.module('navBar', ['authentication', 'ui.bootstrap']);

app.component('navBar', {
        templateUrl: '/ang/templates/nav-bar.html'
    });

app.controller('navBarController', function($rootScope, $scope, $location, $window, $q, $timeout, $interval, $filter, searchTextService, authenticationService, logoutService, updateControllerService, notificationService) {
    $scope.authentication_data = authenticationService.check_authentication();
    console.log($scope.authentication_data);

    $scope.search_text = null
    $scope.search_counter = 0
    $scope.notification_count = 0

    get_notifications();

    $interval(get_notifications, 1000 * 20)

    $scope.search_query = function(search_text){
        var data = angular.toJson({
            search_text: search_text,
        })

        var result = []

        searchTextService.post(data, function(data){
            var UserList = $filter('orderBy')(data.UserList, false)
            for(var item in UserList.slice(0, 10)){
                result.push({
                    name: UserList[item].first_name,
                    username: UserList[item].username,
                    group: 'User'
                })
            }

            var TopicList = $filter('orderBy')(data.TopicList, false)
            for(var item in TopicList.slice(0, 10)){
                result.push({
                    name: TopicList[item],
                    group: 'Topic'
                })
            }

            result = _(result)
                        .groupBy('group')
                        .map(function (g) {
                            g[0].first_in_group = true;  // the first item in each group
                            return g;
                        })
                        .flatten()
                        .value();

            console.log(result)
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
        if($model.group == 'Topic'){
            $location.path('/topic/' + $model.name)
        }if($model.group == 'User'){
            $location.path('/profile/' + $model.username)
        }
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

    $scope.notification_click = function(){
        if($scope.notification_count > 0){
            notificationService.post(function(data){
//                $scope.reviews = []
//                $scope.observers = []
//                $scope.notification_count = 0
            })
        }
    }

    function get_notifications(){
        notificationService.get(function(data){
            if(data.UserAuthenticated){
                $scope.reviews = data.Reviews;
                $scope.observers = data.Observers;
                $scope.notification_count = data.Observers.length + data.Reviews.length;
            }
        })
    }
});