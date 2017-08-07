$(function () {
	var group_id = parseInt($("#group_id").text());
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
	} else if (term_id == 3){
		($("#term_id")).text("2017-1T");
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
	
	var list1 = $("#list1").text();
	var arr1 = eval(list1);
	
	var list2 = $("#list2").text();
	var arr2 = eval(list2);
	
	var list3 = $("#list3").text();
	var arr3 = eval(list3);
	
	var list4 = $("#list4").text();
	var arr4 = eval(list4);

	var rotation = .99;

	var chord_options1 = {
		"gnames": arr1,
		"rotation": rotation,
		"colors": ["#FF0000", "#FFFF00", "#0064FF", "#FF6F0F", 
		"#32FF32", "#64C864", "#64C8C3", "#723FFF", "#FFFF00",
		"#7B75B7", "#779190", "#878787", "#96AD91", "#FBFF96"]
	};
	
	var chord_options2 = {
		"gnames": arr2,
		"rotation": rotation,
		"colors": ["#FF0000", "#FFFF00", "#0064FF", "#FF6F0F", 
		"#32FF32", "#64C864", "#64C8C3", "#723FFF", "#FFFF00",
		"#7B75B7", "#779190", "#878787", "#96AD91", "#FBFF96"]
	};
	
	var chord_options3 = {
		"gnames": arr3,
		"rotation": rotation,
		"colors": ["#FF0000", "#FFFF00", "#0064FF", "#FF6F0F", 
		"#32FF32", "#64C864", "#64C8C3", "#723FFF", "#FFFF00",
		"#7B75B7", "#779190", "#878787", "#96AD91", "#FBFF96"]
	};
	
	var chord_options4 = {
		"gnames": arr4,
		"rotation": rotation,
		"colors": ["#FF0000", "#FFFF00", "#0064FF", "#FF6F0F", 
		"#32FF32", "#64C864", "#64C8C3", "#723FFF", "#FFFF00",
		"#7B75B7", "#779190", "#878787", "#96AD91", "#FBFF96"]
	};
	
	Chord("#svg1", chord_options1, mat1, student1);
	Chord("#svg2", chord_options2, mat2, student2);
	Chord("#svg3", chord_options3, mat3, student3);
	Chord("#svg4", chord_options4, mat4, student4);
});

function Chord(container, options, matrix, name) {
	// initialize the chord configuration variables
	var config = {
		width: 640,
		height: 560,
		rotation: 0,
		textgap: 10,
		colors: ["#7fc97f", "#beaed4", "#fdc086", "#ffff99", "#386cb0", "#f0027f", "#bf5b17", "#666666", "#ffff99", "#386cb0", "#f0027f", "#bf5b17", "#666666"]
	};
	
	var exp = getExp(getMaxSumRow());
	
	// add options to the chord configuration object
	if (options) {
		extend(config, options);
	}
	
	// set chord visualization variables from the configuration object
	var offset = Math.PI * config.rotation,
		width = config.width,
		height = config.height,
		textgap = config.textgap,
		colors = config.colors;
	
	// set viewBox and aspect ratio to enable a resize of the visual dimensions 
	var viewBoxDimensions = "0 0 " + width + " " + height,
		aspect = width / height;
	
	if (config.gnames) {
		gnames = config.gnames;
	} else {
		// make a list of names
		gnames = [];
		for (var i=97; i<matrix.length; i++) {
			gnames.push(String.fromCharCode(i));
		}
	}

	// start the d3 magic
	var chord = d3.layout.chord()
		.padding(.05)
		.sortSubgroups(d3.descending)
		.matrix(matrix);

	var innerRadius = Math.min(width, height) * .31,
		outerRadius = innerRadius * 1.1;

	var fill = d3.scale.ordinal()
		.domain(d3.range(matrix.length-1))
		.range(colors);

	var svg = d3.select(container)
		.attr("viewBox", viewBoxDimensions)
		.attr("preserveAspectRatio", "xMinYMid")    // add viewBox and preserveAspectRatio
		.attr("width", width)
		.attr("height", height)
		.append("g")
		.attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");
		
	//Add text
	var mysvg = d3.select(container);
	mysvg.append("text").attr("id", "text1" + mysvg.attr("id"));
		
	var textsvg = d3.select("#text1" + mysvg.attr("id"))
		.attr("x", 300)
		.attr("y", 50)
		.attr("text-anchor", "middle")
		.attr("class", "highcharts-title")
		.attr("style", "color:#333333;font-size:18px;fill:#333333;width:475px;")
		.append("tspan").text(name)

	var g = svg.selectAll("g.group")
		.data(chord.groups)
		.enter().append("svg:g")
		.attr("class", "group" + mysvg.attr("id"));

	g.append("svg:path")
		.attr("class", "arcs" + mysvg.attr("id"))
		.style("fill", function(d) { return fill(d.index); })
		.style("stroke", function(d) { return fill(d.index); })
		.attr("id", function(d, i) { return "group" + mysvg.attr("id") + d.index; })
		.attr("d", d3.svg.arc().innerRadius(innerRadius).outerRadius(outerRadius).startAngle(startAngle).endAngle(endAngle))
		.on("mouseover", fade(.1))
		.on("mouseout", fade(1))
		.append("svg:title").text(function(d, i) { return gnames[d.index];});
		
	var groupPath = d3.selectAll(".arcs" + mysvg.attr("id"));
		
	// Add a text label.
	var groupText = g.append("text")
		.attr("x", 6)
		.attr("dy", 15);

	groupText.append("textPath")
		.attr("xlink:href", function(d, i) { return "#group" + mysvg.attr("id") + d.index; })
		.text(function(d, i) { return gnames[d.index]; });

	// Remove the labels that don't fit. :(
	groupText.filter(function(d, i) { return groupPath[0][i].getTotalLength() / 2 - 16 < this.getComputedTextLength(); })
		.remove();
	
	var groupTick = g.selectAll(".group-tick")
	.data(function(d) { return groupTicks(d, exp/2); })
	.enter().append("g")
    .attr("class", "group-tick")
    .attr("transform", function(d) { return "rotate(" + (d.angle * 180 / Math.PI - 271.8) + ") translate(" + outerRadius + ",0)"; });
	
	groupTick.append("line")
		.attr("x2", 6);

	groupTick
		.filter(function(d) { return d.value % exp === 0; })
		.append("text")
		.attr("x", 8)
		.attr("dy", ".35em")
		.attr("transform", function(d) { return d.angle < Math.PI ? "rotate(180) translate(-16)" : null; }) //360,33
		.style("text-anchor", function(d) { return d.angle < Math.PI ? "end" : null; })
		.text(function(d) { return d3.format(".1s")(d.value); });
	
	svg.append("g")
		.attr("class", "chord")
		.selectAll("path")
		.data(chord.chords)
		.enter().append("path")
		.attr("d", d3.svg.chord().radius(innerRadius).startAngle(startAngle).endAngle(endAngle))
		.style("fill", function(d) { return fill(d.source.index); })
		.style("opacity", 1)
		.append("svg:title")
		.text(function(d) { 
			return d.source.value + " cambios desde " + gnames[d.source.index] + " hacia " + gnames[d.target.index]; 
		});

	// helper functions start here
	
	function startAngle(d) {
		return d.startAngle + offset;
	}

	function endAngle(d) {
		return d.endAngle + offset;
	}
	
	function extend(a, b) {
		for( var i in b ) {
			a[ i ] = b[ i ];
		}
	}
	
	//Max value of the matrix
	function getMaxSumRow() {
		var curr = 0;
		for (i = 0; i < matrix.length; i++) {
			var tmp = 0;
			var arr = matrix[i].length;
			while(arr--){
				tmp += matrix[i][arr];
			}
			if(curr <= tmp){
				curr = tmp;
			}
		}
		return curr;
	}
	
	//Chose appropriate value of exponent for chord
	function getExp(maxValue){
		return exp = maxValue > 1e5 ? 1e5 : maxValue > 1e4 ? 1e4 : maxValue > 1e3 ? 1e3: maxValue > 1e2 ? 1e2: 1e1;
	}

	// Returns an event handler for fading a given chord group.
	function fade(opacity) {
		return function(g, i) {
			svg.selectAll(".chord path")
				.filter(function(d) { return d.source.index != i && d.target.index != i; })
				.transition()
				.style("opacity", opacity);
		};
	}
	
	function groupTicks(d, step) {
		var k = (d.endAngle - d.startAngle) / d.value;
		return d3.range(0, d.value, step).map(function(value) {
			return {value: value, angle: value * k + d.startAngle};
		});
	}
	
	window.onresize = function() {
		var targetWidth = (window.innerWidth < width)? window.innerWidth : width;
		var svg = d3.select("#visual")
			.attr("width", targetWidth)
			.attr("height", targetWidth / aspect);
	}
}