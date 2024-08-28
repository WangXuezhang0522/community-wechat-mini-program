import React from "react";
import { useState,useEffect } from "react";
import Layout from "@/pages/Layout";
import { Space, Table, message } from 'antd';
import {getCommunityAudit} from '@/store/modules/auditCenter'
import {  useDispatch,useSelector } from "react-redux";
import {http} from '@/utils/request'
import './index.scss'
// 同意社团申请
const agree = async (id)=>{
  const axiosData = {id,status:'审核通过'}
  console.log(axiosData);
 const res = await http.post('/update_community_info_check',axiosData)
 message.success('同意申请成功')
 console.log(res);
 data = await http.post('/search_community_info_check')
 window.location.reload()
}
// 拒绝社团申请
const reject = async (id)=>{
  const axiosData = {id,status:'审核不通过'}
const res = await  http.post('/update_community_info_check',axiosData)
message.success('驳回申请成功')
data = await http.post('/search_community_info_check')
window.location.reload()
}
const columns = [
  {
    title: '社团名称',
    dataIndex: 'name',
    key: 'name',
    render: (text) => <a>{text}</a>,
  },
  {
    title: '社团人数',
    dataIndex: 'number',
    key: 'number',
  },
  {
    title: '社团类型',
    dataIndex: 'type',
    key: 'type',
  },
  {
    title: '社团负责人',
    key: 'leader_name',
    dataIndex: 'leader_name',
  },
  {
    title: 'Action',
    key: 'action',
    render: (record) => (
      <Space size="middle">
        <p onClick = {() =>agree(record.id)} className="reset-password">通过</p>
        <p onClick = {() =>reject(record.id)} className="banned">驳回</p>
      </Space>
    ),
  },
];
let data = [
  {
    key: '1',
    name: '开心社',
    number: 32,
    type: '学习交流',
    leader_name: '王磊',
  },
];


const CommunityAudit = () => {
  const dispatch = useDispatch()
  // 获得待审核社团数据
  const {communityAudit} = useSelector(store => store.audit)
  const getCommunity = async() =>{await dispatch(getCommunityAudit())}
  useEffect(() =>{
    getCommunity()
  },[])

  
  console.log(communityAudit);
  const [navName,setNavName] = useState('审核中心')
  const [navItemName, setNavItemName] = useState("社团审核");
  data = communityAudit
  return (
    <div>
      {/* 架构 */}
      <Layout name={navName} navItemName={navItemName}></Layout>
      <div className="user-list">
        <h1>审核中心 / <span>社团审核</span></h1>
        <div className="main">

        <Table columns={columns} dataSource={data} />
        </div>
      </div>
    </div>
  );
};
export default CommunityAudit;
