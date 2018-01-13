'use strict';

var app = angular.module('interest', []);

app.component('interest', {
        templateUrl: '/ang/templates/interest.html'
    });

app.controller('interestController', function($rootScope, $scope, $window, $q, $timeout, getInterestService, searchTopicService, updateInterestService){

    $scope.topic = ''
    $scope.search_topic = ''
    $scope.selected_topics = []
    $scope.topic_list = []

    get_interest();

    function get_interest(){
        getInterestService.get(function(data){
            if(data.UserAuthenticated){
                $scope.selected_topics=[]
                angular.forEach(data.InterestList, function(item){
                    $scope.selected_topics.push({text: item, type: 'old'})
                })
            }
            else{
                $window.location.href = '';
            }
        });
    }

    $scope.changed_topic = function(search_text){
        var changed_data = angular.toJson({
            topic_name: search_text
        })
        $scope.topic_list=[]
        searchTopicService.post(changed_data, function(data){
            angular.forEach(data.TopicList, function(item){
                $scope.topic_list.push({text: item, type:'old'})
            })
        });

        var deferred = $q.defer();
        $timeout(function () { deferred.resolve( $scope.topic_list ); }, Math.random() * 1000, false);
        return deferred.promise;
    }

    $scope.transformChip = function(chip) {
        // If it is an object, it's already a known chip
        if (angular.isObject(chip)) {
            return chip;
        }

        // Otherwise, create a new one
        return { text: chip, type: 'new' }
    }

    $scope.update_interest = function(){
        var interests = angular.toJson({
            interests: $scope.selected_topics
        })

        console.log(interests)
        updateInterestService.post(interests, function(data){
            if(data.UpdateInterestStatus){
                $location.path('/')
            }
        })
    }
});