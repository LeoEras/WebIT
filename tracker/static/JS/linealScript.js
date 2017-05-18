$(function () {
    var grupo_id = parseInt($("#grupo_id").text());
    var names = ["Student 1", "Student 2", "Student 3", "Student 4"];
    //switch(grupo_id){
    //    case 2:
    //        names[0] = "Benitez";
    //        names[1] = "Mosquera";
    //        names[2] = "Rodriguez";
    //        names[3] = "Martínez";
    //        break;
    //    case 3:
    //        names[0] = "Moreno";
    //        names[1] = "Moreira, Edgar";
    //        names[2] = "Moreira, Maria";
    //        names[3] = "Manosalvas";
    //        break;
    //    case 4:
    //        names[0] = "Guerra";
    //        names[1] = "Garcia";
    //        names[2] = "Guilindro";
    //        names[3] = "Cedeño";
    //        break;
    //    case 5:
    //        names[0] = "Velez";
    //        names[1] = "Carvajal";
    //        names[2] = "Tenecela";
    //        names[3] = "Duchi";
    //        break;
    //    default:
    //        break;
    //}
    
    var values_1 = $(".ul1").map(function() {
                 return $(this).text();
              }).get();
    for (i = 0; i < values_1.length; i++) { 
        values_1[i] = parseFloat(values_1[i]);
    }
    var total_1 = values_1.reduce(function(a, b) { return a + b; }, 0);
    var values_2 = $(".ul2").map(function() {
                 return $(this).text();
              }).get();
    for (i = 0; i < values_2.length; i++) { 
        values_2[i] = parseFloat(values_2[i]);
    }
    var total_2 = values_2.reduce(function(a, b) { return a + b; }, 0);
    var values_3 = $(".ul3").map(function() {
                 return $(this).text();
              }).get();
    for (i = 0; i < values_3.length; i++) { 
        values_3[i] = parseFloat(values_3[i]);
    }
    var total_3 = values_3.reduce(function(a, b) { return a + b; }, 0);
    var values_4 = $(".ul4").map(function() {
                 return $(this).text();
              }).get();
    for (i = 0; i < values_4.length; i++) { 
        values_4[i] = parseFloat(values_4[i]);
    }
    var total_4 = values_4.reduce(function(a, b) { return a + b; }, 0);
    
    function toDate(value){
        var hour = Math.floor(value/3600);
        var minute = Math.floor((value - hour*3600)/60);
        var seconds = value - hour*3600 - minute*60;
        if (minute < 10)
        {
            minute = "0" + minute;
        }
        if (seconds < 10)
        {
            seconds = "0" + seconds;
        }
        return hour + ':' + minute + ':' + seconds
    }
   
    $('#container').highcharts({
        title: {
            text: 'Group #' + grupo_id,//$( "li" ).text(),
            x: -20
        },
        subtitle: {
            text: 'Comparative analysis #' + grupo_id,
            x: -20
        },
        xAxis: {
            categories: $(".alldates").map(function() {
                 return $(this).text();
            }).get()
        },
        yAxis: {
            min: 0,
            tickInterval: 3600,
            title: {
                text: 'Worked hours'
            },          
            labels: {
                formatter: function () {
                    return toDate(this.value)
                }            
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: { formatter: function() {
                return '<b>'+ this.series.name[0] +':</b> ' + toDate(this.point.y)
            }
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: [{
            name: [names[0], ' ' + toDate(total_1)],
            data: values_1
        }, {
            name: [names[1], ' ' + toDate(total_2)],
            data: values_2
        },  {
            name: [names[2], ' ' + toDate(total_3)],
            data: values_3
        },  {
            name: [names[3], ' ' + toDate(total_4)],
            data: values_4
        }]
    });
});