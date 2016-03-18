// Define a new module for our app
var app = angular.module("instantSearch", []);

// Create the instant search filter

app.filter('searchFor', function(){

	// All filters must return a function. The first parameter
	// is the data that is to be filtered, and the second is an
	// argument that may be passed with a colon (searchFor:searchString)

	return function(arr, searchString){

		if(!searchString){
			return arr;
		}

		var result = [];

		searchString = searchString.toLowerCase();

		// Using the forEach helper method to loop through the array
		angular.forEach(arr, function(item){

			if(item.name.toLowerCase().indexOf(searchString) !== -1){
				result.push(item);
			}

		});

		return result;
	};

});

// The controller
function InstantSearchController($scope, $http){

	$scope.items = null

	$http.jsonp('http://127.0.0.1:8000/api/recept/?callback=JSON_CALLBACK')
.success(function(data) {
	console.log(data.objects);
	$scope.items = data.objects;
	for (var i = 0; i < $scope.items.length; i++) {
    $scope.items[i].url = '/' + $scope.items[i].id;
		$scope.items[i].image = 'http://img3.goodfon.ru/original/1280x720/e/44/vtorye-blyuda-ryba-kartofel.jpg';
    $scope.items[i].title = 'Перловая крупа ( ячмень ) совершенно незаслуженно обделена нашим вниманием. Это ценный и питательный продукт, содержащий в себе незаменимые аминокислоты, а также более десяти процентов белка, который по пищевой ценности превосходит пшеничный. Предлагаю вашему вниманию простейший салат из перловой крупы, в котором она " зазвучит" по - новому. Рецепт от Гелии Делеринс. ';
	}
});
}
