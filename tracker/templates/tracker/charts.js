$(function () {
$('#chart_container').highcharts({
chart: {
type: 'bar'
},
title: {
text: 'Monthly Sales'
},
xAxis: {
categories: ['Jan', 'Feb', 'Mar','Apr']
},
yAxis: {
title: {
text: 'numbers'
}
},
series: [{
name: 'John',
data: [1, 0, 4]
}, {
name: 'King',
data: [5, 7, 3]
}]
});
});