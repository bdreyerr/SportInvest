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
                
                // Gradient 
                var ctx = document.getElementById('chart').getContext("2d");
                var gradientStroke = ctx.createLinearGradient(500, 0, 100, 0);
                gradientStroke.addColorStop(0, '#80b6f4');
                gradientStroke.addColorStop(1, '#f49080');

                var gradientFill = ctx.createLinearGradient(500, 0, 100, 0);
                gradientFill.addColorStop(0, "rgba(128, 182, 244, 0.6)");
                gradientFill.addColorStop(1, "rgba(244, 144, 128, 0.6)");

                
                var labels = data.labels;
                var chartdata = data.chartdata;
                var ctx = document.getElementById(id).getContext('2d');
                var chart = new Chart(ctx, {
                    // The type of chart we want to create
                    type: 'line',
            
                    // The data for our dataset
                    data: {
                    labels: labels,
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
                        fill: true,
                        backgroundColor: gradientFill,
                        data: chartdata,
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
                }