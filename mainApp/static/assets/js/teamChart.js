var endpoint = '/teamChart/';




    $.ajax({
    method: "GET",
    url: endpoint + slug+'/',
    success: function(data) {
        drawLineGraph(data, 'teamChart');
        console.log("drawing");
    },
    error: function(error_data) {
        console.log(error_data);
    }
    })



    function drawLineGraph(data, id) {

    // Gradient 
    var ctx = document.getElementById('teamChart').getContext("2d");
    var gradientStroke = ctx.createLinearGradient(500, 0, 100, 0);
    gradientStroke.addColorStop(0, '#80b6f4');
    gradientStroke.addColorStop(1, '#f49080');

    var gradientFill = ctx.createLinearGradient(500, 0, 100, 0);
    gradientFill.addColorStop(0, "rgba(128, 182, 244, 0.6)");
    gradientFill.addColorStop(1, "rgba(244, 144, 128, 0.6)");


    var labelsDay = data.labelsDay;
    var chartdataDay = data.chartdataDay;

    var labelsWeek = data.labelsWeek;
    var chartdataWeek = data.chartdataWeek;

    var labelsMonth = data.labelsMonth;
    var chartdataMonth = data.chartdataMonth;

    var labelsYear = data.labelsYear;
    var chartdataYear = data.chartdataYear;

    var ctx = document.getElementById(id).getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
        labels: labelsDay,
        datasets: [{
            borderColor: gradientStroke,
            pointBorderColor: gradientStroke,
            pointBackgroundColor: gradientStroke,
            pointHoverBackgroundColor: gradientStroke,
            pointHoverBorderColor: gradientStroke,
            pointBorderWidth: 10,
            pointHoverRadius: 1,
            pointHoverBorderWidth: 1,
            pointRadius: 0,
            fill: false,
            backgroundColor: gradientFill,
            data: chartdataDay,
            tension: 0.05
        }]
        },

        // Configuration options go here
        options: {
            tooltips: {
                mode: 'index',
                intersect: false,
                displayColors: false,
                callbacks: {
                    label: function(tooltipItems, data) { 
                        return '$'+ tooltipItems.yLabel ;
                    }
                }
            },
             hover: {
                mode: 'index',
                intersect: false
            },
            scales: {
                xAxes: [{
                display: false
                }],
                yAxes: [{
                ticks: {
                    beginAtZero: false,
                    display: false
                }
                }]
            },
            legend: {
                display:false
            }
        }

    });

    $("#1d").on("click", function() {
        // delete and re add canvas
        $('#teamChart').remove(); // this is my <canvas> element
        $('#chart-container').append('<canvas id="teamChart"><canvas>');
        var context1 = document.getElementById(id).getContext('2d');
        chart = new Chart(context1, {
            // The type of chart we want to create
            type: 'line',
    
            // The data for our dataset
            data: {
            labels: labelsDay,
            datasets: [{
                borderColor: gradientStroke,
                pointBorderColor: gradientStroke,
                pointBackgroundColor: gradientStroke,
                pointHoverBackgroundColor: gradientStroke,
                pointHoverBorderColor: gradientStroke,
                pointBorderWidth: 10,
                pointHoverRadius: 1,
                pointHoverBorderWidth: 1,
                pointRadius: 0,
                fill: false,
                backgroundColor: gradientFill,
                data: chartdataDay,
                tension: 0.05
            }]
            },
    
            // Configuration options go here
            options: {
                tooltips: {
                    mode: 'index',
                    intersect: false,
                    displayColors: false,
                    callbacks: {
                        label: function(tooltipItems, data) { 
                            return '$'+ tooltipItems.yLabel ;
                        }
                    }
                },
                 hover: {
                    mode: 'index',
                    intersect: false
                },
                scales: {
                    xAxes: [{
                    display: false
                    }],
                    yAxes: [{
                    ticks: {
                        beginAtZero: false,
                        display: false
                    }
                    }]
                },
                legend: {
                    display:false
                }
            }
    
        });
     });

    $("#1w").on("click", function() {
        // delete and re add canvas
        $('#teamChart').remove(); // this is my <canvas> element
        $('#chart-container').append('<canvas id="teamChart"><canvas>');
        var context1 = document.getElementById(id).getContext('2d');
        chart = new Chart(context1, {
            // The type of chart we want to create
            type: 'line',
    
            // The data for our dataset
            data: {
            labels: labelsWeek,
            datasets: [{
                borderColor: gradientStroke,
                pointBorderColor: gradientStroke,
                pointBackgroundColor: gradientStroke,
                pointHoverBackgroundColor: gradientStroke,
                pointHoverBorderColor: gradientStroke,
                pointBorderWidth: 10,
                pointHoverRadius: 1,
                pointHoverBorderWidth: 1,
                pointRadius: 0,
                fill: false,
                backgroundColor: gradientFill,
                data: chartdataWeek,
                tension: 0.05
            }]
            },
    
            // Configuration options go here
            options: {
                tooltips: {
                    mode: 'index',
                    intersect: false,
                    displayColors: false,
                    callbacks: {
                        label: function(tooltipItems, data) { 
                            return '$'+ tooltipItems.yLabel ;
                        }
                    }
                },
                 hover: {
                    mode: 'index',
                    intersect: false
                },
                scales: {
                    xAxes: [{
                    display: false
                    }],
                    yAxes: [{
                    ticks: {
                        beginAtZero: false,
                        display: false
                    }
                    }]
                },
                legend: {
                    display:false
                }
            }
    
        });
     });

     $("#1m").on("click", function() {
        // delete and re add canvas
        $('#teamChart').remove(); // this is my <canvas> element
        $('#chart-container').append('<canvas id="teamChart"><canvas>');
        var context1 = document.getElementById(id).getContext('2d');
        chart = new Chart(context1, {
            // The type of chart we want to create
            type: 'line',
    
            // The data for our dataset
            data: {
            labels: labelsMonth,
            datasets: [{
                borderColor: gradientStroke,
                pointBorderColor: gradientStroke,
                pointBackgroundColor: gradientStroke,
                pointHoverBackgroundColor: gradientStroke,
                pointHoverBorderColor: gradientStroke,
                pointBorderWidth: 10,
                pointHoverRadius: 1,
                pointHoverBorderWidth: 1,
                pointRadius: 0,
                fill: false,
                backgroundColor: gradientFill,
                data: chartdataMonth,
                tension: 0.05
            }]
            },
    
            // Configuration options go here
            options: {
                tooltips: {
                    mode: 'index',
                    intersect: false,
                    displayColors: false,
                    callbacks: {
                        label: function(tooltipItems, data) { 
                            return '$'+ tooltipItems.yLabel ;
                        }
                    }
                },
                 hover: {
                    mode: 'index',
                    intersect: false
                },
                scales: {
                    xAxes: [{
                    display: false
                    }],
                    yAxes: [{
                    ticks: {
                        beginAtZero: false,
                        display: false
                    }
                    }]
                },
                legend: {
                    display:false
                }
            }
    
        });
     });

     $("#1y").on("click", function() {
        // delete and re add canvas
        $('#teamChart').remove(); // this is my <canvas> element
        $('#chart-container').append('<canvas id="teamChart"><canvas>');
        var context1 = document.getElementById(id).getContext('2d');
        chart = new Chart(context1, {
            // The type of chart we want to create
            type: 'line',
    
            // The data for our dataset
            data: {
            labels: labelsYear,
            datasets: [{
                borderColor: gradientStroke,
                pointBorderColor: gradientStroke,
                pointBackgroundColor: gradientStroke,
                pointHoverBackgroundColor: gradientStroke,
                pointHoverBorderColor: gradientStroke,
                pointBorderWidth: 10,
                pointHoverRadius: 1,
                pointHoverBorderWidth: 1,
                pointRadius: 0,
                fill: false,
                backgroundColor: gradientFill,
                data: chartdataYear,
                tension: 0.05
            }]
            },
    
            // Configuration options go here
            options: {
                tooltips: {
                    mode: 'index',
                    intersect: false,
                    displayColors: false,
                    callbacks: {
                        label: function(tooltipItems, data) { 
                            return '$'+ tooltipItems.yLabel ;
                        }
                    }
                },
                 hover: {
                    mode: 'index',
                    intersect: false
                },
                scales: {
                    xAxes: [{
                    display: false
                    }],
                    yAxes: [{
                    ticks: {
                        beginAtZero: false,
                        display: false
                    }
                    }]
                },
                legend: {
                    display:false
                }
            }
    
        });
     });
}