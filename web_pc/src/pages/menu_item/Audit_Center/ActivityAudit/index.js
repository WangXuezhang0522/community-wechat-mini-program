import React, { useEffect } from "react";
import { useState } from "react";
import Layout from "@/pages/Layout";
import { Space, Table, message} from 'antd';
import { useSelector,useDispatch } from "react-redux";
import {getActivityAudit} from '@/store/modules/auditCenter'
import {http } from '@/utils/request'
import './index.scss'
// 同意活动申请
const agree = async (id) =>{
  const axiosData = {id,status:'审核通过'}
 const res = await http.post('/update_community_activity_check',axiosData)
 message.success('同意申请成功')
 console.log(res);
 data = await http.post('/search_community_activity_check')
 window.location.reload()
}
// 拒绝活动申请
const reject = async  (id) =>{
  const axiosData = {id,status:'审核不通过'}
 const res = await http.post('/update_community_activity_check',axiosData)
 message.success('驳回申请成功')
 console.log(res);
 data = await http.post('/search_community_activity_check')
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
  },
  {
    title: 'Action',
    key: 'action',
    render: (record) => (
      <Space size="middle">
        <p onClick={() => agree(record.id)} className="reset-password">通过</p>
        <p onClick={() => reject(record.id)} className="banned">驳回</p>
      </Space>
    ),
  },
];
let data = [
  {
  },
];
const ActivityAudit = () => {
  const dispatch = useDispatch()
  const getActivity = async() =>{await dispatch(getActivityAudit()) }
  useEffect(()=>{
      getActivity()
  },[])
  const [navName,setNavName] = useState('审核中心')
  const [navItemName, setNavItemName] = useState("活动审核");
  const {activityAudit}  =  useSelector(store => store.audit)
  data = activityAudit
  console.log(data);
  return (
    <div>
      {/* 架构 */}
      <Layout name={navName} navItemName={navItemName}></Layout>
      <div className="user-list">
        <h1>审核中心 / <span>活动审核</span></h1>
        <div className="main">

        <Table columns={columns} dataSource={data} />
        </div>
      </div>
    </div>
  );
};
export default ActivityAudit;
