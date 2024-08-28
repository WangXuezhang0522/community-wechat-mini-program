import React, { useEffect } from "react";
import { useState } from "react";
import Layout from "@/pages/Layout";
import { Space, Table, Tag,Tooltip,message } from 'antd';
import {http} from '@/utils/request'
import './index.scss'
import { getAllActivity } from "@/store/modules/home";
import Activity from "../../Home/Activity";
import { useDispatch, useSelector } from "react-redux";
let data = [
  {
    key: '1',
    name: '开心社',
    activity_name:'吃饭睡觉打豆豆',
    activity_place: '家里',
    money: 1555,
    startTime: '2024-05-07',
    endTime:'2024-05-08'
  },
];
// 停止社团活动
const deleteActivity = async(id) =>{
  const axiosData = {id}
   const res = await http.post('/delete_community_activity',axiosData)
  message.success('删除该活动成功')
  data =  await  http.post('/search_all_community_activity_noimage')
  window.location.reload()
}
const columns = [
  {
    title: '社团名称',
    dataIndex: 'community_name',
    key: 'community_name',
    render: (text) => <a>{text}</a>,
  },
  {
    title: '活动名称',
    dataIndex: 'name',
    key: 'name',
  },
  {
    title: '活动地点',
    dataIndex: 'address',
    key: 'address',
  },
  {
    title: '活动经费',
    key: 'cost',
    dataIndex: 'cost',
  },
  {
    title: '开始时间',
    key: 'start_time',
    dataIndex: 'start_time',
    render: (text)=><Tooltip placement="topLeft" title={text}>{text}</Tooltip>,
    // 超出显示省略号
    onCell: ()=>{
      return {
        style:{
          maxWidth: 40,
          overflow: 'hidden',
          whiteSpace: 'nowrap',
          textOverflow: 'ellipsis',
          cursor: 'pointer'
        }
      }
    },
  },
  {
    title: '结束时间',
    key: 'end_time',
    dataIndex: 'end_time',
    render: (text)=><Tooltip placement="topLeft" title={text}>{text}</Tooltip>,
    // 超出显示省略号
    onCell: ()=>{
      return {
        style:{
          maxWidth: 60,
          overflow: 'hidden',
          whiteSpace: 'nowrap',
          textOverflow: 'ellipsis',
          cursor: 'pointer'
        }
      }
    },
  },
  {
    title: 'Action',
    key: 'action',
    render: (record) => (
      <Space size="middle">
        {/* <p className="reset-password">延长一天</p> */}
        <p onClick={() =>{deleteActivity(record.id)}} className="banned">删除活动</p>
      </Space>
    ),
  },
];

const ActivityManage = () => {
  const dispatch = useDispatch()
  const [navName,setNavName] = useState('综合管理')
  const [navItemName, setNavItemName] = useState("活动管理");
  const getActivity = async() => { await dispatch(getAllActivity()) }
  useEffect(()=>{
    getActivity()
  },[])
  const {allActivity} = useSelector(store=>store.home)
  console.log(allActivity);
  data = allActivity
  return (
    <div>
      {/* 架构 */}
      <Layout name={navName} navItemName={navItemName}></Layout>
      <div className="user-list">
        <h1>综合管理 / <span>活动管理</span></h1>
        <div className="main">

        <Table columns={columns} dataSource={data} />
        </div>
      </div>
    </div>
  );
};
export default ActivityManage;
