$.getJSON("data/time-dist.json", function(data) {
    var values = []
    var keys = []
    for (var key in data) {
        values.push(data[key])
        keys.push(key)
    }
    var ctx = document.getElementById("q1time").getContext('2d');
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: keys,
            datasets: [{
                pointRadius: 0,
                label: 'Frequency',
                data: values,
                pointBackgroundColor: 'rgba(255,99,132,1)',
                backgroundColor: 'rgba(255,99,132,1)',
                fill: true,
                cubicInterpolationMode: 'monotone',
                spanGaps: true,
                // borderWidth: 4,
            }]
        },
        options: {
            legend: { display: false },
            title: {
                display: true,
                text: 'Frequency of Minutes Per Ride'
              },        
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }

    });    
})
