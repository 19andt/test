'use strict';

var app = angular.module('newReview', []);

app.component('newReview', {
        templateUrl: '/ang/templates/new-review.html'
    });

app.controller('newReviewController', function($rootScope, $scope, $location, $q, $timeout, searchTopicService, addReviewService, addTopicService){
    $scope.search_topic = ''
    $scope.topic_list = []

    $scope.topic = ''
    $scope.caption = ''
    $scope.briefing = ''
    $scope.review_rating = 0
    $scope.add_topic = false

    $scope.addReview = function(){
        var selected_topics = [
            {
                type: 'old',
                text: $scope.topic
            }
        ]

        var new_review_data = angular.toJson({
            topic_list: selected_topics,
            caption: $scope.caption,
            briefing: $scope.briefing
        });
        addReviewService.post(new_review_data, function(data){
            $location.path('')
        });
    }

    $scope.changed_topic = function(search_text){
        var changed_data = angular.toJson({
            topic_name: search_text
        })
        $scope.topic_list=[]
        searchTopicService.post(changed_data, function(data){
            if(data.TopicList.length != 0){
                $scope.add_topic = false
            }else{
                $scope.add_topic = true
            }
            $scope.topic_list = data.TopicList
            //angular.forEach(data.TopicList, function(item){
            //    $scope.topic_list.push({text: item, type:'old'})
            //})
        });

        var deferred = $q.defer();
        $timeout(function () { deferred.resolve( $scope.topic_list ); }, Math.random() * 1000, false);
        return deferred.promise;
    }

    $scope.selectItem = function($suggestion, $model, $label){
        $scope.topic = $model
    }

    $scope.topic_add = function(){
        if($scope.topic != ''){
            var new_topic_data = angular.toJson({
                    name: $scope.topic,
                    description: ''
            });
            addTopicService.post(new_topic_data, function(data){
                $location.path('/topic/' + $scope.topic)
            });
        }
    }

//    $scope.transformChip = function(chip) {
//        // If it is an object, it's already a known chip
//        if (angular.isObject(chip)) {
//            return chip;
//        }
//
//        // Otherwise, create a new one
//        return { text: chip, type: 'new' }
//    }
});