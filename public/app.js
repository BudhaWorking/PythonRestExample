app = angular.module('myApp',[])

app.controller('myController',['$scope','$http',function($scope,$http){

    $scope.message = "Hello Abhishek"

        
    $http({
                method: 'GET',
                url: 'http://localhost:5000/boeing/suppliers'
            }).then(function (res){
               $scope.result = res.data.Users
                // console.log(res)
            },function (error){
                alert("ERRRORR")
                console.log(error)
            })
            

}])