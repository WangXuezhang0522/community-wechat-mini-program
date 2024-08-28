import React, { useEffect } from "react";
import { useState } from "react";
import Layout from "@/pages/Layout";
import { Space, Table, Tag,message } from 'antd';
import {  useSelector,useDispatch } from "react-redux";
import {http} from '@/utils/request'
import {getAllCommunity} from '@/store/modules/home'
import './index.scss'

// 初始化表格数据
let  data = [
 {id:1,name:'11',leader_name:'负责人',number:'人数',type:'欸写'}
];
// 根据id解散社团
const deleteCommunityById = async(id)=>{
  console.log(id);
  const idData = {id}
  const res =  await http.post('/delete_community_info',idData)
  console.log(res);
  if(res == 'success'){
    message.success('解散社团成功')
   let newData =  await  http.post('/search_all_community_info_noimage')
   data = newData.slice(1)
  }else{
    message.error('解散社团失败')
  }
  
 }
const columns = [
  {
    title: '社团名',
    dataIndex: 'name',
    key: 'name',
    render: (text) => <a>{text}</a>,
  },
  {
    title: '负责人',
    dataIndex: 'leader_name',
    key: 'leader_name',
  },
  {
    title: '人数',
    dataIndex: 'number',
    key: 'number',
  },
  {
    title: '类型',
    key: 'type',
    dataIndex: 'type'
  },
  {
    title: 'Action',
    key: 'action',
    render: (record) => (
      <Space size="middle">
        <p onClick={async()=> deleteCommunityById(record.id)} className="banned">解散社团</p>
      </Space>
    ),
  },
];

const CommunityManage = ()=> {
  const dispatch = useDispatch()
  const [navName,setNavName] = useState('综合管理')
  const [navItemName, setNavItemName] = useState("社团管理");
  const getCommunity = async() =>{
    await  dispatch(getAllCommunity())
}
  useEffect(()=>{
      getCommunity()
  },[])
 const {allCommunity} = useSelector((store) => store.home)
 data = allCommunity
  return (
    <div>
      {/* 架构 */}
      <Layout name={navName} navItemName={navItemName}></Layout>
      <div className="user-list">
        <h1>综合管理 / <span>社团管理</span></h1>
        <div className="main">

        <Table columns={columns} dataSource={data} />
        </div>
      </div>
    </div>
  );
};
export default CommunityManage;
