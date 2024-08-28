import React from 'react'
import Chart from "@/components/Echarts/echarts";
import './index.scss'
// This example requires ECharts v5.5.0 or later

export default function Activity({allActivity}) {
  let options = {
    color:['#ef4136','#78cdd1','#72777b'],
    tooltip: {
      trigger: 'item'
    },
    legend: {
      top: '5%',
      left: 'center'
    },
    series: [
      {
        name: 'Access From',
        type: 'pie',
        radius: ['40%', '70%'],
        center: ['50%', '70%'],
        // adjust the start and end angle
        startAngle: 180,
        endAngle: 360,
        data: [
          { value: 1048, name: '进行中' },
          { value: 735, name: '未开始' },
          { value: 580, name: '已结束' }
        ]
      }
    ]
  };
  // prettier-ignore
  let data = [["04-12", 2116], ["04-13", 8129], ["04-14", 3535], ["04-15", 5586], ["04-16", 2073]];
  let data2= [["04-12", 516], ["04-13", 129], ["04-14", 355], ["04-15", 586], ["04-16", 1073]];
  let dateList = data.map(function (item) {
    return item[0];
  });
  let valueList = data.map(function (item) {
    return item[1];
  });
  let valueList2 = data2.map(function (item) {
    return item[1];
  });
  let options2 = {
    // Make gradient line here
    visualMap: [
      {
        show: false,
        type: 'continuous',
        seriesIndex: 0,
        min: 0,
        max: 400
      },
      {
        show: false,
        type: 'continuous',
        seriesIndex: 1,
        dimension: 0,
        min: 0,
        max: dateList.length - 1
      }
    ],
    title: [
      {
        left: 'center',
        text: '活动经费'
      },
      {
        top: '50%',
        left: 'center',
        text: '活动参与人数'
      }
    ],
    tooltip: {
      trigger: 'axis'
    },
    xAxis: [
      {
        data: dateList,
        type: "category",         
   
      },
      {
        data: dateList,
        gridIndex: 1,
        type: "category",         
      },
 
    ],
    yAxis: [
      {},
      {
        gridIndex: 1,
   
      }
    ],
    grid: [
      {
        bottom: '60%'
      },
      {
        top: '60%'
      }
    ],
    series: [
      {
        type: 'line',
        showSymbol: false,
        data: valueList
      },
      {
        type: 'line',
        showSymbol: false,
        data: valueList2,
        xAxisIndex: 1,
        yAxisIndex: 1
      }
    ]
  };
  let type1 = 0;
  let type2 = 0;
  let type3 = 0;
  if(allActivity !== undefined){
    allActivity.forEach(item =>{
       switch(item.status){
        case'进行中':type1++;break;
        case'未开始':type2++;break;
        case'已结束':type3++;break;

       }
    })
   options.series[0].data[0].value = type1
   options.series[0].data[1].value = type2
   options.series[0].data[2].value = type3
  }
  return (
    <div className='echarts-user'>
      <h1>活动统计</h1>
      <div className='echarts-box'>
        <div className = 'first'> <Chart options={options}  style ={{height:'300px',width:'80%'}}></Chart></div>
       <div className='second'>      <Chart options={options2}  style ={{height:'400px',width:'80%'}}></Chart></div>

      </div>
     
    </div>
  )
}
