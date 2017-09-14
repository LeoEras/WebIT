$(function () {
	var grupo_id = parseInt($("#grupo_id").text());
	var term_id = parseInt($("#term_id").text());
	var student1 = ($("#student1").text());
	var student2 = ($("#student2").text());
	var student3 = ($("#student3").text());
	var student4 = ($("#student4").text());
    var names = [student1, student2, student3, student4];
	if (term_id == 1){
		($("#term_id")).text("2016-1T");
	} else if (term_id == 2){
		($("#term_id")).text("2016-2T");
	}
	
	// From http://mkweb.bcgsc.ca/circos/guide/tables/
	var str1 = ($("#matrix1").text());
	var mat1 = eval(str1);
	
	var str2 = ($("#matrix2").text());
	var mat2 = eval(str2);
	
	var str3 = ($("#matrix3").text());
	var mat3 = eval(str3);
	
	var str4 = ($("#matrix4").text());
	var mat4 = eval(str4);
	
	drawCircle("#svg1", mat1, student1);
	drawCircle("#svg2", mat2, student2);
	drawCircle("#svg3", mat3, student3);
	drawCircle("#svg4", mat4, student4);
});

function drawCircle(svg, matrix, student){
	var svg = d3.select(svg),
	width = +svg.attr("width"),
	height = +svg.attr("height"),
	outerRadius = Math.min(width, height) * 0.5 - 55,
	innerRadius = outerRadius - 30;

	//Add text
	svg.append("text").attr("id", "text1" + svg.attr("id"));
	var textsvg = d3.select("#text1" + svg.attr("id"));
	textsvg.append("tspan").text(student);
	textsvg.attr("x", 270);
	textsvg.attr("y", 24);
	textsvg.attr("text-anchor", "middle");
	textsvg.attr("class", "highcharts-title");
	textsvg.attr("style", "color:#333333;font-size:18px;fill:#333333;width:475px;");

	//Esta parte es para los numeros en el criculo
	var formatValue = d3.formatPrefix(",.0", 1e2);

	var chord = d3.chord()
		.padAngle(0.05)
		.sortSubgroups(d3.descending);

	var arc = d3.arc()
		.innerRadius(innerRadius)
		.outerRadius(outerRadius);

	var ribbon = d3.ribbon()
		.radius(innerRadius);

	var color = d3.scaleOrdinal()
		.domain(d3.range(4))
		.range(["#000000", "#FFDD89", "#957244", "#F26223", 
		"33CCCC", "0066FF", "FF00FF", "FF0000", "FFFF00",
		"33CC33", "003300", "330000", "000033"]);

	var g = svg.append("g")
		.attr("transform", "translate(" + width / 2 + "," + height / 2 + ")")
		.datum(chord(matrix));

	var group = g.append("g")
		.attr("class", "groups")
		.selectAll("g")
		.data(function(chords) { return chords.groups; })
		.enter().append("g");
	
	//Arco externo
	group.append("path")
		.style("fill", function(d) { return color(d.index); })
		.style("stroke", function(d) { return d3.rgb(color(d.index)).darker(); })
		.attr("d", arc);

	//Numero de ticks en la grafica
	var groupTick = group.selectAll(".group-tick")
		.data(function(d) { return groupTicks(d, 1e2); })
		.enter().append("g")
		.attr("class", "group-tick")
		.attr("transform", function(d) { return "rotate(" + (d.angle * 180 / Math.PI - 90) + ") translate(" + outerRadius + ",0)"; });

	groupTick.append("line")
		.attr("x2", 6);

	groupTick
		.filter(function(d) { return d.value % 5e2 === 0; })
		.append("text")
		.attr("x", 8)
		.attr("dy", ".35em")
		.attr("transform", function(d) { return d.angle > Math.PI ? "rotate(180) translate(-16)" : null; })
		.style("text-anchor", function(d) { return d.angle > Math.PI ? "end" : null; })
		.text(function(d) { return formatValue(d.value); });
	
	//Enlaces
	g.append("g")
		.attr("class", "ribbons")
		.selectAll("path")
		.data(function(chords) { return chords; })
		.enter().append("path")
		.attr("d", ribbon)
		.style("fill", function(d) { return color(d.target.index); })
		.style("stroke", function(d) { return d3.rgb(color(d.target.index)).darker(); });
		
	// On Click, we want to add data to the array and chart
	svg.on("mouseover", fade(.1)).on("mouseout", fade(1));
}

// Returns an array of tick angles and values for a given group and step.
function groupTicks(d, step) {
	var k = (d.endAngle - d.startAngle) / d.value;
	return d3.range(0, d.value, step).map(function(value) {
		return {value: value, angle: value * k + d.startAngle};
	});
}

function fade(opacity) {
	return function(g, i) {
		svg.selectAll(".chord path")
			.filter(function(d) { return d.source.index != i && d.target.index != i; })
			.transition()
			.style("opacity", opacity);
	};
}