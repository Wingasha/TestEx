var myApp = angular.module('myApp', ['chart.js']);

myApp.controller('mainCtrl', function ($scope, $http) {

    $scope.outputData = ''       //содержит текст возвращаемый сервером
    $scope.offset = ''           //содержит смещение, задаваемое пользователем для отправки на сервер
    $scope.inputData = ''        //содержит текст, задаваемый пользователем для отправки на сервер

    $scope.sendRequest = function (event) {
        /*
        Отправляет запросы на шифровку/дешифровку текста
         */
        $http({
            method: 'POST',
            url: '/cipher_caesar/' + event.target.value + '/',
            data: {'text': $scope.inputData, 'offset': $scope.offset},
            headers:{
                'Content-Type': 'application/json'
            }
        })
            .then(function (success) {
            $scope.outputData = success.data.result;
        },function (error) {
            console.log(error.data);
            console.log(error.status);
            });
    }


    $scope.labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']; // названия столбцов
    $scope.data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]];//количество каждой буквы
    var backgroundColours = [];  //содержит коды цветов для каждого поля(labels)

    //цикл поочерёдно записывает значения цветов в массив backgroundColours
     for( var i = 0; i < $scope.data[0].length + 3;  ) {
         backgroundColours[i++] = '#9400D3';
         backgroundColours[i++] = '#4169E1';
         backgroundColours[i++] = '#27ae60';
         backgroundColours[i++] = '#87CEEB';
     }

    // Записать в scope массив фоновых цветов
    $scope.datasetOverride = [{ backgroundColor: backgroundColours }];

    //В опциях графика задать начало оси Y с 0 и минимальное значение данных 0
    $scope.options = {
    barShowStroke: false,
    scales: {
      yAxes: [{
        ticks: {
          min: 0,
            beginAtZero: true
            }
      }]
    }
    };


    $scope.chartChange = function () {
        /*
        При каждом изменении текста график перерисовывается. В цикле используем каждую букву алфавита для разделения
        исходной строки на подстроки и тем самым подсчитываем количество каждой буквы в тексте соответственно
         */
        for(var i = 0; i < $scope.labels.length; i++){
            $scope.data[0][i] = $scope.inputData.split($scope.labels[i]).length - 1;

        }
    }


    $scope.keyValidate = function (event) {
        /*
        При нажатии клавиши проверяет  входит ли набраный символ в диапазон ASCII-кодировки. Если нет то прерывает
        распостранение события и соответственно символ не печатается в поле.
         */
        if(/^[\x00-\x7F]*$/.test(String.fromCharCode(event.which)) == false)
        {
            if(event.preventDefault()) event.preventDefault();
            else event.returnValue = false;                    // для IE8 и ниже
        }
    }

    $scope.pasteValidate = function (event) {
        /*
        При вставки текста проверяет  входит ли вставляемый текст в диапазон ASCII-кодировки. Если нет то прерывает
        распостранение события и соответственно текст не вставляется в поле.
         */
        if(/^[\x00-\x7F]*$/.test(event.clipboardData.getData('Text')) == false)
        {
            if(event.preventDefault()) event.preventDefault();
            else event.returnValue = false;                    // для IE8 и ниже
        }
    }

});
