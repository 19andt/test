var app = angular.module('rbControllers')

app.controller('reviewController', function($scope, $rootScope, $location, updateRatingService){

    $scope.review = null
    $scope.rating = null
    $scope.topic_list = []
    $scope.comment_list = []
    $scope.username = null

    $scope.$watch('rating.personal_rating', function(){
        if($scope.rating != null){
            calculate_ranges(parseInt($scope.rating["personal_rating"]))
        }
    })

    function calculate_ranges(n){
        $scope.rating_range = []
        for(var i = 1; i < n + 1; i++)
        {
            $scope.rating_range.push(i)
        }

        $scope.negative_rating_range=[]
        for(var i = n + 1; i < $scope.max_rating + 1; i++)
        {
            $scope.negative_rating_range.push(i)
        }
    }

    $scope.rating_click = function(n){
        var rating_update = angular.toJson({
            review_id: $scope.review['id'],
            value: parseInt(n)
        })
        updateRatingService.post(rating_update, function(data){
            if(data['UpdateRatingStatus'] == true){
                $scope.rating['personal_rating'] = parseInt(n)
            }
        })
        $scope.rating['personal_rating'] = parseInt(n)
    }

    $scope.review_detail_click = function(event){
        if(event.target.nodeName != 'A'){
            if(event.target.nodeName == 'SPAN' && event.target.className == 'fa fa-star-o fa-6'){
                return
            }
            console.log($scope.review.id)
            $location.path('/review/' + $scope.review.id)
        }
    }
});