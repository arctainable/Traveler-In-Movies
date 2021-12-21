<script>
import {Radar} from 'vue-chartjs'

export default {
  extends: Radar,
  props: {
    dataset: Object,
  },
  data () {

    return {
      dataCollection: {
        labels: Object.keys(this.dataset),
        datasets: [
          {
              label: '영화 수',
              data: Object.values(this.dataset),
              fill: true,
              backgroundColor: "rgba(54, 162, 235, 0.2)",
              borderColor: "rgb(54, 162, 235)",
              // backgroundColor: 'blue', //'#f87979',
              pointBackgroundColor: 'white',
              // borderColor: "rgb(54, 162, 235)",
              // fillColor: "rgba(102,45,145,.1)",
              // strokeColor: "rgba(102,45,145,1)",
              // pointColor : "rgba(220,220,220,1)",
              // pointStrokeColor : "#fff",
              spanGaps: true,
              pointHoverBackgroundColor: "pink",
              pointHoverBorderColor: 'blue',
              pointHoverBorderWidth: 2,
              pointHoverRadius: 10,
              borderWidth: 2,
              pointBorderColor: '#249EBF',
              
          }
        ]
      },
      chartOptions: {
        // hover: {
        //  onHover: function(evt, item) { 
        // if (item.length) {
        //     console.log(item[0]._index);
        //     }
        //   }
        // },
        title: {
                display: false,
                text: this.title,
                align: 'center',
                font: {
                  size: 15,
                },
                position: 'bottom',
                // padding: {
                //   top: 0,
                //   bottom: 0,
                // }
            },
        tooltips: {
          callbacks: {
            title: (tooltipItem, data) => data.labels[tooltipItem[0].index],
            // label: function (tooltipItem, data) {
            //   console.log(tooltipItem, data)
            //   console.log(this)
            // }
            //   console.log(data, this)
            //   return tooltipItem.index
            //   // console.log(tooltipItem.index, data)
            //   // window.hidx = tooltipItem.index
            //   // console.log(hidx)
            //   // window.getChartHoverIdx(tooltipItem.index)
            //   // this.$store.dispatsch('getChartHoverIdx',tooltipItem._index)
            // },
          }
        },
        responsive: true,

        legend: {
          display: false,

        },
  
        // onClick : function (evt, item) {

        //   // console.log(this.hidx)
        //   if (item.length) {
        //     console.log('pointLabel click',evt, item)
        //     // console.log(item[0]._index)
        //     // this.getChartHoverIdx(item[0]._index)
        //   }
          
        // },
        

        scale: {
          pointLabels: {
            label: 'here',
            fontSize: 14,
            fontColor: "blue",
            fontStyle: "bold",
            fontFamily: "'Raleway', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",
          },
          ticks: {
            color: 'red',
          },
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
                display: false,
                min: 0,
                max: 200,
              },
              gridLines: {
                display: false,
              },
              scaleLabel: {
                display: false,
              }
            }
          ],
          xAxes: [
            {
              gridLines: {
                display: false,
              },
              ticks: {
                display: false,
              },
              
            }
          ]
        }
      }
    }
  },


  mounted() {
    this.renderChart(this.dataCollection, this.chartOptions, {responsive: true, maintainAspectRatio: false, onClick:this.handle})
    
  },
  methods: {
    handle (point, event) {
      console.log(event)
      const item = event[0]
      this.$emit('on-receive', {
        index: item._index,
        value: item._index
      })
    }
  },
}


</script>

<style>

</style>