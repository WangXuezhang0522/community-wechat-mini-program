import React from 'react'
import Chart from "@/components/Echarts/echarts";
import './index.scss'

export default function Post({allPost}) {
  let options = {
    color:['#f15a22'],
    xAxis: {
      type: 'category',
      boundaryGap: false,
      data: ['学习专题','社交专题','运动专题','生活专版','默认板块'],
      type: "category",         
      axisLabel: {
        //x轴文字的配置
        show: true,
        interval: 0,//使x轴文字显示全
       }

    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        data: [100, 532, 301, 634],
        type: 'line',
        areaStyle: {}
      }
    ]
  };
  
  let options2 = {
    title:{
      text:'点赞数与评论数比例',
      textStyle:{
        verticalAlign:'bottom'
      }
      },
    color: ['#fb7c41', '#10d8ba'],
    xAxis: {},
    yAxis: {},
    series: [
      {
        symbolSize: 6,
        data: [
     
        ],
        type: 'scatter'
      }
    ]
  };
  let type1 = 0;
  let type2 = 0;
  let type3 = 0;
  let type4 = 0;
  let type5 = 0;
  if(allPost !== undefined){
    allPost.forEach((item,index) =>{
      switch(item.type){
          case '默认板块': type1++; break;
          case '学习专题': type2++; break;
          case '社交专题': type3++; break;
          case '运动专题': type4++; break;
          case '生活专版': type5++; break;
      }
      options2.series[0].data.push([item.likeCount,item.commentCount])
    })
    options.series[0].data[0] = type2
    options.series[0].data[1] = type3
    options.series[0].data[2] = type4
    options.series[0].data[3] = type5
    options.series[0].data[4] = type1
  }
  return (
    <div className='echarts-user'>
      <h1>帖子统计</h1>
      <div className='echarts-box'>
        <div  className = 'first'> <Chart options={options}  style ={{height:'300px',width:'80%'}}></Chart></div>
       <div className='second'>      <Chart options={options2}  style ={{height:'400px',width:'80%'}}></Chart></div>

      </div>
     
    </div>
  )
}
