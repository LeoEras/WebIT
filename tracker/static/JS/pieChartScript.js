$(function () {
	var group_id = parseInt($("#group_id").text());
	var term_id = parseInt($("#term_id").text());
	var student1 = ($("#student1").text());
	var student2 = ($("#student2").text());
	var student3 = ($("#student3").text());
	var student4 = ($("#student4").text());
    var names = [student1, student2, student3, student4];
	if (term_id == 1){
		($("#term_id")).text("2016 - 1T");
	} else if (term_id == 2){
		($("#term_id")).text("2016 - 2T");
	}
			
	//Datos
	for (j = 1; j < 5; j++){
		//Seleccion de datos importantes/no importantes
		eval("var values_" + j + " = $('.values" + j + "').map(function() { return $(this).text(); }).get();");
		eval("for (i = 0; i < values_" + j + ".length; i++) { values_" + j + "[i] = parseFloat(values_" + j + "[i]); }");
		eval("var percent_imp" + j + " = values_" + j + "[0]/(values_" + j + "[0] + values_" + j + "[1]) * 100;");
		eval("var percent_nimp" + j + " = values_" + j + "[1]/(values_" + j + "[0] + values_" + j + "[1]) * 100;");
		//Seleccion de datos de actividades productivas/no productivas con sus respectivos tiempos
		eval("var activitiesful" + j + " = $('.activitiesful" + j + "').map(function() { return $(this).text(); }).get();");
		eval("var timesful" + j + " = $('.timesful" + j + "').map(function() { return $(this).text(); }).get();");
		eval("var activitiesless" + j + " = $('.activitiesless" + j + "').map(function() { return $(this).text(); }).get();");
		eval("var timesless" + j + " = $('.timesless" + j + "').map(function() { return $(this).text(); }).get();");
		eval("for (i = 0; i < timesful" + j + " .length; i++) { timesful" + j + "[i] = parseFloat(timesful" + j + "[i]); }");
		eval("var combinedful" + j + " = new Array(activitiesful" + j + ".length);");
		eval("var sum = timesful" + j + ".reduce(function(a, b) { return a + b; }, 0);");
		eval("for (i = 0; i < timesful" + j + ".length; i++) { combinedful" + j + "[i] = [activitiesful" + j + "[i], (timesful" + j + "[i]/sum) * 100]; }");
		eval("for (i = 0; i < timesless" + j + " .length; i++) { timesless" + j + "[i] = parseFloat(timesless" + j + "[i]); }");
		eval("var combinedless" + j + " = new Array(activitiesless" + j + ".length);");
		eval("var sum = timesless" + j + ".reduce(function(a, b) { return a + b; }, 0);");
		eval("for (i = 0; i < timesless" + j + ".length; i++) { combinedless" + j + "[i] = [activitiesless" + j + "[i], (timesless" + j + "[i]/sum) * 100]; }");
	}
	$('#container').highcharts({
		chart: {
			reflow: true,
			type: 'pie'
		},
		title: {
			text: names[0]
		},
		subtitle: {
			text: 'Presione una sección para ver con mayor detalle.'
		},
		plotOptions: {
			series: {
				dataLabels: {
					enabled: true,
					format: '{point.name}: {point.y:.1f}%'
				}
			}
		},
		lang: {
			drillUpText: '<< Completa'
		},
		tooltip: {
			headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
			pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
		},
		series: [{
			name: names[0],
			colorByPoint: true,
			data: [{
				name: 'Importante',
				y: percent_imp1,
				sliced: true,
				selected: true,
				drilldown: 'Importante1'
			}, {
				name: 'No Importante',
				y: percent_nimp1,
				drilldown: 'No Importante1'
			}]
		}],
		drilldown: {
			series: [{
				name: 'Importante',
				id: 'Importante1',
				data: combinedful1
			}, {
				name: 'No Importante',
				id: 'No Importante1',
				data: combinedless1
			}]
		}
	});
	if(!isNaN(percent_imp2)){
		$('#container2').highcharts({
			chart: {
				type: 'pie'
			},
			title: {
				text: names[1]
			},
			subtitle: {
				text: 'Presione una sección para ver con mayor detalle.'
			},
			plotOptions: {
				series: {
					dataLabels: {
						enabled: true,
						format: '{point.name}: {point.y:.1f}%'
					}
				}
			},
			lang: {
				drillUpText: '<< Completa'
			},
			tooltip: {
				headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
				pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
			},
			series: [{
				name: names[1],
				colorByPoint: true,
				data: [{
					name: 'Importante',
					y: percent_imp2,
					sliced: true,
					selected: true,
					drilldown: 'Importante2'
				}, {
					name: 'No Importante',
					y: percent_nimp2,
					drilldown: 'No Importante2'
				}]
			}],
			drilldown: {
				series: [{
					name: 'Importante',
					id: 'Importante2',
					data: combinedful2
				}, {
					name: 'No Importante',
					id: 'No Importante2',
					data: combinedless2
				}]
			}
		});
	}
	if(!isNaN(percent_imp3)){
		$('#container3').highcharts({
			chart: {
				type: 'pie'
			},
			title: {
				text: names[2]
			},
			subtitle: {
				text: 'Presione una sección para ver con mayor detalle.'
			},
			plotOptions: {
				series: {
					dataLabels: {
						enabled: true,
						format: '{point.name}: {point.y:.1f}%'
					}
				}
			},
			lang: {
				drillUpText: '<< Completa'
			},
			tooltip: {
				headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
				pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
			},
			series: [{
				name: names[2],
				colorByPoint: true,
				data: [{
					name: 'Importante',
					y: percent_imp3,
					sliced: true,
					selected: true,
					drilldown: 'Importante3'
				}, {
					name: 'No Importante',
					y: percent_nimp3,
					drilldown: 'No Importante3'
				}]
			}],
			drilldown: {
				series: [{
					name: 'Importante',
					id: 'Importante3',
					data: combinedful3
				}, {
					name: 'No Importante',
					id: 'No Importante3',
					data: combinedless3
				}]
			}
		});
	}
	if(!isNaN(percent_imp4)){
		$('#container4').highcharts({
			chart: {
				type: 'pie'
			},
			title: {
				text: names[3]
			},
			subtitle: {
				text: 'Presione una sección para ver con mayor detalle.'
			},
			plotOptions: {
				series: {
					dataLabels: {
						enabled: true,
						format: '{point.name}: {point.y:.1f}%'
					}
				}
			},
			lang: {
				drillUpText: '<< Completa'
			},
			tooltip: {
				headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
				pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
			},
			series: [{
				name: names[3],
				colorByPoint: true,
				data: [{
					name: 'Importante',
					y: percent_imp4,
					sliced: true,
					selected: true,
					drilldown: 'Importante4'
				}, {
					name: 'No Importante',
					y: percent_nimp4,
					drilldown: 'No Importante4'
				}]
			}],
			drilldown: {
				series: [{
					name: 'Importante',
					id: 'Importante4',
					data: combinedful4
				}, {
					name: 'No Importante',
					id: 'No Importante4',
					data: combinedless4
				}]
			}
		});
	}
});