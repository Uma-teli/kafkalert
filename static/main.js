const displayChart = () => {
    
  const ctx = document.getElementById('myChart').getContext("2d");

  const mychart = new Chart(ctx, {
    type: 'pie',
    data: {
      labels: ['Model Scoring Percent', 'not'],
      datasets: [{
        
        data: [12, 19],
        backgroundColor: ["#e63946", "#14213d"],
        borderWidth: 0,
      },
    ],
    },
    
    
  });

};

displayChart();