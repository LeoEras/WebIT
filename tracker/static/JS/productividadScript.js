$(function () {
    var group_id = parseInt($("#group_id").text());
    var term_id = parseInt($("#term_id").text());
	var student = ($("#student").text());
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
        values_2[i] = -1 * parseFloat(values_2[i]);
    }
    var total_2 = values_2.reduce(function(a, b) { return a + b; }, 0);
    
    function toDate(value){
		value = Math.abs(value);
        var hour = Math.floor(value/3600);
        var minute = Math.floor((value - hour*3600)/60);
        var seconds = value - hour*3600 - minute*60;
        if (minute < 10) {
            minute = "0" + minute;
        } 
		if (seconds < 10) {
            seconds = "0" + seconds;
        }
        return hour + ':' + minute + ':' + seconds
    }
	
	function parseTerm(term_id){
		var str = "";
		if (term_id == 1){
			str = "2016-1T";
		} else if (term_id == 2){
			str = "2016-2T";
		} else if (term_id == 3){
			str = "2017-1T";
		}
		
		return str;
	}

	$('#container').highcharts({
		chart: {
			type: 'area',
			zoomType: 'x'
		},
		title: {
			text: parseTerm(term_id),//$( "li" ).text(),
			x: -20
		},
		subtitle: {
			text: 'Grupo # ' + group_id + ': Análisis de productividad individual<br>' + student,
			x: -20
		},
		xAxis: {
			categories: $(".alldates").map(function() {
				 return $(this).text();
			}).get(),
			minRange: 1
		},
		yAxis: {
			tickInterval: 3600,
			title: {
				text: 'Horas Trabajadas'
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
		plotOptions: {
			series: {
				cursor: 'pointer',
				point: {
					events: {
						click: function (e) {
							hs.htmlExpand(null, {
								pageOrigin: {
									x: e.pageX || e.clientX,
									y: e.pageY || e.clientY
								},
								headingText: this.series.name[0],
								maincontentText: this.series.data[this.x].category + ':<br/> ' +
									this.y + ' visits',
								width: 200
							});
							console.log(this.series);
						}
					}
				}
			}
		},
		series: [{
			name: ['Tiempo productivo', ' ' + toDate(total_1)],
			data: values_1,
			color: '#90CC90'
		}, {
			name: ['Tiempo no productivo', ' ' + toDate(total_2)],
			data: values_2,
			color: '#EC8E8E'
		}]
	});
});