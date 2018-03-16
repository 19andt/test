'use strict';

var app = angular.module('searchResults', []);

app.component('searchResults', {
        templateUrl: '/ang/templates/search-results.html'
    });

app.controller('searchResultsController', function($rootScope, $scope, $routeParams, $location, searchTextService, getTopicService, addTopicService){
    $scope.search_text = $routeParams.search_text;
    $scope.result = []
    $scope.topic_details = []
    $scope.topic_list = []

    $scope.$watch('result', function(newValue, oldValue){
        $scope.search_results = arrayUnique(newValue);
        get_topic_details();
    })

    getting_search_results();

    $scope.add_topic = function(){
        if($scope.search_text != ''){
            var new_topic_data = angular.toJson({
                name: $scope.search_text,
                description: ''
            });
            addTopicService.post(new_topic_data, function(data){
                $location.path('/topic/' + $scope.search_text)
            });
            console.log('Clicked.')
        }
    }

    function getting_search_results(){
        var query_list = combine($scope.search_text)
        console.log(query_list)
        console.log(typeof query_list)

        for(var item in query_list){
            if(query_list[item] != '' && query_list[item].length >= 3){
                var data = angular.toJson({
                    search_text: query_list[item],
                })

                searchTextService.post(data).$promise.then(function(data){
                    $scope.result = $scope.result.concat(data.TopicList)
                })

                //temp = result.concat(data.TopicList)
                //console.log('%d + %d = %d', result.length, data.TopicList.length, temp.length)
                //result = temp
                //console.log(temp)
                //temp = result.concat(temp);
                //result = temp
            }
        }
    }

    function get_topic_details(){
        for(var item in $scope.search_results){
            if($scope.topic_list.includes($scope.search_results[item]) == false){

                var url_params = {
                    topic_name: $scope.search_results[item]
                }

                getTopicService.get(url_params, function(data){
                    $scope.topic_details.push(data.Topic)
                    console.log($scope.topic_details)
                })

                $scope.topic_list.push($scope.search_results[item])
            }
        }
    }

    function arrayUnique(array) {
        var a = array.concat();
        for(var i=0; i<a.length; ++i) {
            for(var j=i+1; j<a.length; ++j) {
                if(a[i] === a[j])
                    a.splice(j--, 1);
            }
        }

        return a;
    }

    function combine(string) {
        function iter(i, temp) {
            if (i >= string.length) {
                result.push(temp);
                return;
            }
            iter(i + 1, temp + string[i]);
            iter(i + 1, temp);
        }

        var result = [];
        iter(0, '');
        return result;
    }
});