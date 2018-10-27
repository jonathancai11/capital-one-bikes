$.getJSON("data/bike-freq.json", function(data) {
    // console.log(data)
    var values = []
    var keys = []
    count = 0
    for (var key in data) {
        count += 1 
        values.push(data[key][1])
        keys.push(data[key][0])
    }
    var ctx = document.getElementById("q1chart").getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: keys,
            datasets: [{
                label: '# of Uses',
                data: values,
                backgroundColor: 'rgba(255, 206, 86, 1)',
                borderColor: 'rgba(255, 206, 86, 1)',
                pointRadius: 0,
                // fill: false,             
            }]
        },
        options: {
            legend: { display: false },
            title: {
                display: true,
                text: 'Frequency of Use Across Unique Bike ID\'s Ordered By Frequency'
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

