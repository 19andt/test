'use strict';

var app = angular.module('newReview', []);

app.component('newReview', {
        templateUrl: '/ang/templates/new-review.html'
    });

app.controller('newReviewController', function($rootScope, $scope, $window, $q, $timeout, searchTopicService, addReviewService){
    $scope.topic = ''
    $scope.search_topic = ''
    $scope.selected_topics = []
    $scope.topic_list = []

    $scope.caption = ''
    $scope.briefing = ''
    $scope.review_rating = 0

    $scope.addReview = function(){
        var new_review_data = angular.toJson({
            topic_list: $scope.selected_topics,
            caption: $scope.caption,
            briefing: $scope.briefing
        });
        addReviewService.post(new_review_data, function(data){
            $window.location.href = ''
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

    $scope.topic_selected = function(text){
        $scope.topic = text;
    }

    $scope.transformChip = function(chip) {
        // If it is an object, it's already a known chip
        if (angular.isObject(chip)) {
            return chip;
        }

        // Otherwise, create a new one
        return { text: chip, type: 'new' }
    }
});