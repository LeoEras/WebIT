
$(function () {
	var grupo_id = parseInt($("#grupo_id").text());
	var term_id = parseInt($("#term_id").text());
	var names = ["Student 1", "Student 2", "Student 3", "Student 4"];
		

	if (term_id == 1){
		($("#term_id")).text("2016-1T");
	} else if (term_id == 2){
		($("#term_id")).text("2016-2T");
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
			type: 'pie'
		},
		title: {
			text: names[0]
		},
		subtitle: {
			text: 'Click the slices to view with more detail.'
		},
		plotOptions: {
			series: {
				dataLabels: {
					enabled: true,
					format: '{point.name}: {point.y:.1f}%'
				}
			}
		},
		tooltip: {
			headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
			pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
		},
		series: [{
			name: names[0],
			colorByPoint: true,
			data: [{
				name: 'Relevant',
				y: percent_imp1,
				sliced: true,
				selected: true,
				drilldown: 'Relevant1'
			}, {
				name: 'Non Relevant',
				y: percent_nimp1,
				drilldown: 'Non Relevant1'
			}]
		}],
		drilldown: {
			series: [{
				name: 'Relevant',
				id: 'Relevant1',
				data: combinedful1
			}, {
				name: 'Non Relevant',
				id: 'Non Relevant1',
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
				text: 'Click the slices to view with more detail.'
			},
			plotOptions: {
				series: {
					dataLabels: {
						enabled: true,
						format: '{point.name}: {point.y:.1f}%'
					}
				}
			},
			tooltip: {
				headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
				pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
			},
			series: [{
				name: names[1],
				colorByPoint: true,
				data: [{
					name: 'Relevant',
					y: percent_imp2,
					sliced: true,
					selected: true,
					drilldown: 'Relevant2'
				}, {
					name: 'Non Relevant',
					y: percent_nimp2,
					drilldown: 'Non Relevant2'
				}]
			}],
			drilldown: {
				series: [{
					name: 'Relevant',
					id: 'Relevant2',
					data: combinedful2
				}, {
					name: 'Non Relevant',
					id: 'Non Relevant2',
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
				text: 'Click the slices to view with more detail.'
			},
			plotOptions: {
				series: {
					dataLabels: {
						enabled: true,
						format: '{point.name}: {point.y:.1f}%'
					}
				}
			},
			tooltip: {
				headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
				pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
			},
			series: [{
				name: names[2],
				colorByPoint: true,
				data: [{
					name: 'Relevant',
					y: percent_imp3,
					sliced: true,
					selected: true,
					drilldown: 'Relevant3'
				}, {
					name: 'Non Relevant',
					y: percent_nimp3,
					drilldown: 'Non Relevant3'
				}]
			}],
			drilldown: {
				series: [{
					name: 'Relevant',
					id: 'Relevant3',
					data: combinedful3
				}, {
					name: 'Non Relevant',
					id: 'Non Relevant3',
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
				text: 'Click the slices to view with more detail.'
			},
			plotOptions: {
				series: {
					dataLabels: {
						enabled: true,
						format: '{point.name}: {point.y:.1f}%'
					}
				}
			},
			tooltip: {
				headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
				pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
			},
			series: [{
				name: names[3],
				colorByPoint: true,
				data: [{
					name: 'Relevant',
					y: percent_imp4,
					sliced: true,
					selected: true,
					drilldown: 'Relevant4'
				}, {
					name: 'Non Relevant',
					y: percent_nimp4,
					drilldown: 'Non Relevant4'
				}]
			}],
			drilldown: {
				series: [{
					name: 'Relevant',
					id: 'Relevant4',
					data: combinedful4
				}, {
					name: 'Non Relevant',
					id: 'Non Relevant4',
					data: combinedless4
				}]
			}
		});
	}
});