$.getJSON("data/travel-distances.json", function(data) {
    var values = []
    var keys = []
    for (var key in data) {
        values.push(data[key])
        keys.push(key)
    }
    var ctx = document.getElementById("q3line").getContext('2d');
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: keys,
            datasets: [{
                label: 'Probability',
                data: values,
                pointBackgroundColor: 'rgba(54, 162, 235, 1)',
                backgroundColor: 'rgba(54, 162, 235, 1)',
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
                text: 'Probabilities of Miles Rode'
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
