var endpoint = '/chart';



                $.ajax({
                method: "GET",
                url: endpoint,
                
                success: function(data) {
                    drawLineGraph(data, 'chart');
                    console.log("drawing");
                },
                error: function(error_data) {
                    console.log(error_data);
                }
                })


            
                function drawLineGraph(data, id) {

                // Hover Line
                Chart.defaults.LineWithLine = Chart.defaults.line;
                Chart.controllers.LineWithLine = Chart.controllers.line.extend({
                draw: function(ease) {
                    Chart.controllers.line.prototype.draw.call(this, ease);

                    if (this.chart.tooltip._active && this.chart.tooltip._active.length) {
                        var activePoint = this.chart.tooltip._active[0],
                            ctx = this.chart.ctx,
                            x = activePoint.tooltipPosition().x,
                            topY = this.chart.scales['y-axis-0'].top,
                            bottomY = this.chart.scales['y-axis-0'].bottom;

                        // draw line
                        ctx.save();
                        ctx.beginPath();
                        ctx.moveTo(x, topY);
                        ctx.lineTo(x, bottomY);
                        ctx.lineWidth = 2;
                        ctx.strokeStyle = '#C1C1C1';
                        ctx.stroke();
                        ctx.restore();
                    }
                }
                });

                // Gradient 
                var ctx = document.getElementById('chart').getContext("2d");
                var gradientStroke = ctx.createLinearGradient(500, 0, 100, 0);
                gradientStroke.addColorStop(0, '#80b6f4');
                gradientStroke.addColorStop(1, '#f49080');

                var gradientFill = ctx.createLinearGradient(500, 0, 100, 0);
                gradientFill.addColorStop(0, "rgba(128, 182, 244, 0.6)");
                gradientFill.addColorStop(1, "rgba(244, 144, 128, 0.6)");
                
                // update these when a user clicks a new timeframe button

                
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
                    type: 'LineWithLine',
            
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
                    // Change net value
                    
                    $("#net_gain_week").hide();
                    $("#net_gain_month").hide();
                    $("#net_gain_year").hide();
                    $("#net_gain_day").show();


                    // delete and re add canvas
                    $('#chart').remove(); // this is my <canvas> element
                    $('#chart-container').append('<canvas id="chart"><canvas>');
                    var context1 = document.getElementById(id).getContext('2d');
                    chart = new Chart(context1, {
                        // The type of chart we want to create
                        type: 'LineWithLine',
                
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
                    // net gain hide / show
                    $("#net_gain_week").show();
                    $("#net_gain_month").hide();
                    $("#net_gain_year").hide();
                    $("#net_gain_day").hide();

                    // delete and re add canvas
                    $('#chart').remove(); // this is my <canvas> element
                    $('#chart-container').append('<canvas id="chart"><canvas>');
                    var context1 = document.getElementById(id).getContext('2d');
                    chart = new Chart(context1, {
                        // The type of chart we want to create
                        type: 'LineWithLine',
                
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

                    // net gain hide / show
                    $("#net_gain_week").hide();
                    $("#net_gain_month").show();
                    $("#net_gain_year").hide();
                    $("#net_gain_day").hide();

                    // delete and re add canvas
                    $('#chart').remove(); // this is my <canvas> element
                    $('#chart-container').append('<canvas id="chart"><canvas>');
                    var context1 = document.getElementById(id).getContext('2d');
                    chart = new Chart(context1, {
                        // The type of chart we want to create
                        type: 'LineWithLine',
                
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

                    // net gain hide / show
                    $("#net_gain_week").hide();
                    $("#net_gain_month").hide();
                    $("#net_gain_year").show();
                    $("#net_gain_day").hide();

                    // delete and re add canvas
                    $('#chart').remove(); // this is my <canvas> element
                    $('#chart-container').append('<canvas id="chart"><canvas>');
                    var context1 = document.getElementById(id).getContext('2d');
                    chart = new Chart(context1, {
                        // The type of chart we want to create
                        type: 'LineWithLine',
                
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
