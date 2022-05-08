```
/*
  {
      //name: '{{form.echart4.data[1].name}}',
      //data: {{form.echart4.data[1].value|safe}},
      type: 'line',
      smooth: true,
      symbol: 'circle',
      symbolSize: 5,
      showSymbol: false,
      lineStyle: {
          normal: {
      color: '#00d887',
              width: 2
          }
      },
      areaStyle: {
          normal: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                  offset: 0,
                  color: 'rgba(0, 216, 135, 0.4)'
              }, {
                  offset: 0.8,
                  color: 'rgba(0, 216, 135, 0.1)'
              }], false),
              shadowColor: 'rgba(0, 0, 0, 0.1)',
          }
      },
   itemStyle: {
   normal: {
      color: '#00d887',
      borderColor: 'rgba(221, 220, 107, .1)',
      borderWidth: 12
   }
},
  },
  */
```



```
itemStyle: {
        normal: {
            color:'#27d08a',
            opacity: 1,
barBorderRadius: 5,
        }
    }
```



```
<!--echarts5-->
<script>
$(function echarts_5() {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('echart5'));

    option = {
        //  backgroundColor: '#00265f',
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
    },
    grid: {
        left: '0%',
        top:'10px',
        right: '0%',
        bottom: '2%',
        containLabel: true
    },
    xAxis: [{
        type: 'category',
          data: {{form.echart5.xAxis|safe}},
        axisLine: {
            show: true,
            lineStyle: {
                color: "rgba(255,255,255,.1)",
                width: 1,
                type: "solid"
            },
        },
        axisTick: {
            show: false,
        },
      axisLabel:  {
            interval: 0,
           // rotate:50,
            show: true,
            splitNumber: 15,
            textStyle: {
                color: "rgba(255,255,255,.6)",
                fontSize: '12',
            },
        },
    }],
    yAxis: [{
        type: 'value',
        axisLabel: {
            //formatter: '{value} %'
            show:true,
            textStyle: {
                color: "rgba(255,255,255,.6)",
                fontSize: '12',
            },
        },
        axisTick: {
            show: false,
        },
        axisLine: {
            show: true,
            lineStyle: {
                color: "rgba(255,255,255,.1    )",
                width: 1,
                type: "solid"
            },
        },
        splitLine: {
            lineStyle: {
               color: "rgba(255,255,255,.1)",
            }
        }
    }],
    series: [{
        type: 'bar',
        data: {{form.echart5.series|safe}},
        barWidth:'35%', //柱子宽度
       // barGap: 1, //柱子之间间距
        itemStyle: {
            normal: {
                color:'#2f89cf',
                opacity: 1,
            barBorderRadius: 5,
            }
        }
    }
   ]
};

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    window.addEventListener("resize",function(){
        myChart.resize();
    });
})



</script>
```