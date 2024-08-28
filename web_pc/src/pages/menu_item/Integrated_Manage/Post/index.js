import React, { useEffect } from "react";
import { useState } from "react";
import Layout from "@/pages/Layout";
import { Space, Table, Tag,Tooltip,message } from 'antd';
import {getAllPost} from '@/store/modules/home'
import {http} from '@/utils/request'
import { useDispatch, useSelector } from "react-redux";
import './index.scss'
let data = [
  {
    key: '1',
    title:'我要结婚了',
    content:'新郎不是我',
    type:'学习专题',
    community:'开心社'
  },
];
// 封禁社团帖子
const bannedPost = async (id) =>{
  const axiosData = {id}
  const res = await http.post('/delete_community_post',axiosData)
 message.success('封禁该帖子成功')
 data = await  http.post('/search_all_community_post_noimage')
 window.location.reload()
}
const columns = [
  {
    title: '发帖人',
    dataIndex: 'username',
    key: 'username',
  },
  {
    title: '标题',
    dataIndex: 'title',
    key: 'title',
    render: (text) => <a>{text}</a>,
    render: (text)=><a><Tooltip placement="topLeft" title={text}>{text}</Tooltip></a>,
    // 超出显示省略号
    onCell: ()=>{
      return {
        style:{
          maxWidth: 200,
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
          maxWidth: 300,
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
    title: 'Action',
    key: 'action',
    render: (record) => (
      <Space size="middle">
        <p className="banned" onClick = {() =>{bannedPost(record.id)}}>封禁</p>
      </Space>
    ),
  },
];

const PostManage = () => {
  const dispatch = useDispatch()
  const [navName,setNavName] = useState('综合管理')
  const [navItemName, setNavItemName] = useState("帖子管理");
  const getPost = async() =>{
    await dispatch(getAllPost())
  }
  useEffect(()=>{
    getPost()
  },[])
  const {allPost} = useSelector((store) => store.home)
  console.log(allPost);
  data = allPost
  return (
    <div>
      {/* 架构 */}
      <Layout name={navName} navItemName={navItemName}></Layout>
      <div className="user-list">
        <h1>综合管理 / <span>帖子管理</span></h1>
        <div className="main">

        <Table columns={columns} dataSource={data} />
        </div>
      </div>
    </div>
  );
};
export default PostManage;
