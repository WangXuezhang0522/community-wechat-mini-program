import React, { useState } from 'react'
import Chart from "@/components/Echarts/echarts";
import { useEffect } from 'react';
import './index.scss'



export default function User({allUser}) {
  // 角色统计
  let options = {
    color: ['#fb7c41', '#10d8ba','#1059d8'],
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
        avoidLabelOverlap: false,
        padAngle: 5,
        itemStyle: {
          borderRadius: 10
        },
        label: {
          show: false,
          position: 'center'
        },
        emphasis: {
          label: {
            show: true,
            fontSize: 40,
            fontWeight: 'bold'
          }
        },
        labelLine: {
          show: false
        },
        data: [
          { value: 1048, name: '社长' },
          { value: 735, name: '游客' },
          { value: 580, name: '社员' },
        ]
      }
    ]
  };
  let options2 = {
    color:['#4e72b8','#f391a9'],
    title: {
      text: '性别统计',
      left: 'center'
    },
    tooltip: {
      trigger: 'item'
    },
    legend: {
      orient: 'vertical',
      left: 'left'
    },
    series: [
      {
        name: '性别',
        type: 'pie',
        radius: '50%',
        data: [
          { value: 1, name: '男' },
          { value: 1, name: '女' },
        ],
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          }
        }
      }
    ]
  };
    const userList = allUser.user
    // 当有值时进行判断赋值
    if(userList !== undefined){
      let manNumber =  0;
      let womanNumber = 0;
      let presidentNumber = 0;
      let visitorNumber = 0;
      let memberNumber = 0
      userList.forEach(item => {
        if(item.sex == '男'){
          manNumber++;
        }
        if(item.sex == '女'){
          womanNumber++;
        }
        if(item.role == '社长'){
          presidentNumber++
        }
        if(item.role == '游客'){
          visitorNumber++
        }
        if(item.role == '社员'){
          memberNumber++
        }
      });
      options2.series[0].data[0].value = manNumber
      options2.series[0].data[1].value = womanNumber
      options.series[0].data[0].value = presidentNumber
      options.series[0].data[1].value = visitorNumber
      options.series[0].data[2].value = memberNumber
    }
    
  return (
    <div className='echarts-user'>
      <h1>用户统计</h1>
      <div className='echarts-box'>
        <div className = 'first'> <Chart options={options}  style ={{height:'300px',width:'80%'}}></Chart></div>
       <div className='second' >      <Chart  options={options2}  style ={{height:'400px',width:'80%'}} ></Chart></div>

      </div>
     
    </div>
  )
}
