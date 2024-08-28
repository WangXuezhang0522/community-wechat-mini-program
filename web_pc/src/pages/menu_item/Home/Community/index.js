import React from 'react'
import Chart from "@/components/Echarts/echarts";
import './index.scss'
import { type } from '@testing-library/user-event/dist/type';

export default function Community({allCommunity}) {
  let options = {

    legend: {
      top: 'bottom'
    },
    series: [
      {
        name: '社团类型统计',
        type: 'pie',
        radius: [30, 100],
        center: ['50%', '50%'],
        roseType: 'area',
        itemStyle: {
          borderRadius: 8
        },
        data: [
          { value: 40, name: '学习交流' },
          { value: 38, name: '科技创新' },
          { value: 32, name: '数字网络' },
          { value: 30, name: '兴趣爱好' },
          { value: 28, name: '编程算法' },
          { value: 26, name: '体育运动' },
          { value: 22, name: '社会实践' }
        ]
      }
    ]
  };
  let options2 = {
    color:['#65c294'],
    xAxis: {
      type: 'category',
      data: ['学习', '科技', '数字', '兴趣', '编程', '体育', '社会']
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        data: [120, 200, 150, 80, 70, 110, 130],
        type: 'bar',
        showBackground: true,
        backgroundStyle: {
          color: 'rgba(180, 180, 180, 0.2)'
        }
      }
    ]
  };
  let type1 = 0;
  let type2 = 0;
  let type3 = 0;
  let type4 = 0;
  let type5 = 0;
  let type6 = 0;
  let type7 = 0;
  if(allCommunity !== undefined){
    allCommunity.forEach(item => {
     switch(item.type){
      case '学习交流': type1++; break;
      case '科技创新': type2++; break;
      case '数字网络': type3++; break;
      case '兴趣爱好': type4++; break;
      case '编程算法': type5++; break;
      case '体育运动': type6++; break;
      case '社会实践': type7++; break;
     }
    });
    options.series[0].data[0].value = type1
    options.series[0].data[1].value = type2
    options.series[0].data[2].value = type3
    options.series[0].data[3].value = type4
    options.series[0].data[4].value = type5
    options.series[0].data[5].value = type6
    options.series[0].data[6].value = type7
    options2.series[0].data[0] = type1
    options2.series[0].data[1] = type2
    options2.series[0].data[2] = type3
    options2.series[0].data[3] = type4
    options2.series[0].data[4] = type5
    options2.series[0].data[5] = type6
    options2.series[0].data[6] = type7
  }

  return (
    <div className='echarts-community'>
      <h1>社团统计</h1>
      <div className='echarts-box'>
        <div className = 'first'> <Chart options={options}  style ={{height:'300px',width:'80%'}}></Chart></div>
       <div className='second'>      <Chart options={options2}  style ={{height:'400px',width:'80%'}}></Chart></div>

      </div>
     
    </div>
  )
}
