import React, { useEffect } from "react";
import { useState } from "react";
import Layout from "@/pages/Layout";
import { Space, Table, Tag,Tooltip,message } from 'antd';
import { UseSelector,useDispatch, useSelector } from "react-redux";
import {getPostAudit} from '@/store/modules/auditCenter'
import {http} from '@/utils/request'
import './index.scss'
// 帖子审核通过
const agree = async (id) =>{
  const axiosData = {id,status:'审核通过'}
  const res =  await http.post('/update_community_post_check',axiosData)
  data = await http.post('/search_community_post_check')
  message.success('审核通过')
  window.location.reload()

}
// 帖子审核不通过
const reject = async (id) =>{
  const axiosData = {id,status:'审核不通过'}
  const res =  await http.post('/update_community_post_check',axiosData)
  data = await http.post('/search_community_post_check')
  message.error('审核拒绝')
  window.location.reload()
}
const columns = [
  {
    title: '标题',
    dataIndex: 'title',
    key: 'title',
    render: (text)=><a><Tooltip  placement="topLeft" title={text}>{text}</Tooltip></a>,
    onCell: ()=>{
      return {
        style:{
          maxWidth: 100,
          overflow: 'hidden',
          whiteSpace: 'nowrap',
          textOverflow: 'ellipsis',
          cursor: 'pointer'
        }
      }
    },
  },
  {
    title: '内容',
    dataIndex: 'content',
    key: 'content',
    render: (text)=><Tooltip placement="topLeft" title={text}>{text}</Tooltip>,
    // 超出显示省略号
    onCell: ()=>{
      return {
        style:{
          maxWidth: 160,
          overflow: 'hidden',
          whiteSpace: 'nowrap',
          textOverflow: 'ellipsis',
          cursor: 'pointer'
        }
      }
    },
  },
  {
    title: '类型',
    dataIndex: 'type',
    key: 'type',
  },
  {
    title: '社团所属',
    key: 'community_name',
    dataIndex: 'community_name',
  },
  {
    title: '状态',
    dataIndex: 'status',
    key: 'status',
  
  },
  {
    title: 'Action',
    key: 'action',
    render: (record) => (
      <Space size="middle">
        <p onClick = {() => agree(record.id)} className="reset-password">通过</p>
        <p onClick =  {() => reject(record.id)} className="banned">驳回</p>
      </Space>
    ),
  },
];
let data = [
 
];
const PostAudit = () => {
  const dispatch = useDispatch()
  const [navName,setNavName] = useState('审核中心')
  const [navItemName, setNavItemName] = useState("帖子审核");
  const {postAudit} = useSelector(store => store.audit)
  const getPost = async ()=>{await dispatch(getPostAudit())}
  useEffect(() =>{
     getPost()
  },[])
  data = postAudit
  return (
    <div>
      {/* 架构 */}
      <Layout name={navName} navItemName={navItemName}></Layout>
      <div className="user-list">
        <h1>审核中心 / <span>帖子审核</span></h1>
        <div className="main">

        <Table    columns={columns} dataSource={data} />
        </div>
      </div>
    </div>
  );
};
export default PostAudit;
