// Initialize start/end data
var startData, endData;
// Wait for each JSON file to be loaded
$.when(
    $.getJSON("data/start-stations-frequency.json", function(data1) {
        startData = data1;
    }),
    $.getJSON("data/end-stations-frequency.json", function(data2) {
        endData = data2;
    })
).then(function() {
    // Make sure each are loaded in correctly
    if (startData && endData) {
        // Retrieve context for canvas element
        var ctx = document.getElementById("q2bar").getContext('2d');

        // Store keys/values of start data separately
        var count = 0

        var startValues = []
        var startKeys = []

        var endValues = []
        var endKeys = []

        // Keys for both start and end
        var totalKeys = []

        for (var key in startData) {
            // Increment count
            count += 1
            // Only taking top 5
            if (count < 6) {
                startValues.push(0)
                startValues.push(startData[key][1])
                endValues.push(endData[key][1])
                endValues.push(0)

                totalKeys.push(startData[key][0])
                totalKeys.push(endData[key][0])
            } else {
                break
            }
        }
        console.log(totalKeys)
        console.log(endValues)
        console.log(startValues)

        // Create our chart with both data sets   
        var myBarChart = new Chart(ctx, {
            type: 'horizontalBar',
            data: {
                labels: totalKeys,
                datasets: [{
                    label: 'Start Station Frequencies',
                    data: startValues,
                    borderColor: 'rgba(153, 102, 255, 1)',
                    backgroundColor: 'rgba(153, 102, 255, 1)',
                }, 
                {
                    label: 'End Station Frequencies',
                    data: endValues,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 1)',

                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:true
                        }
                    }]
                },
                barThickness: 'flex',        
            }
            });
    }
});
