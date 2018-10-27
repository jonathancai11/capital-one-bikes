$.getJSON("data/pass-types.json", function(data) {
    // console.log(data)
    var values = []
    var keys = []
    for (var key in data) {
        values.push(data[key])
        keys.push(key)
    }
    var ctx = document.getElementById("q4chart").getContext('2d');
    new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: keys,
          datasets: [
            {
              label: "Population (millions)",
              backgroundColor: [
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
              ],
              data: values,
            }
          ]
        },
        options: {
        }
    });
    
})


