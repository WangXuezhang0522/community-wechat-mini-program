import React, { useEffect } from "react";
import { useState } from "react";
import Layout from "@/pages/Layout";
import { Space, Table, Tag,message, Input } from 'antd';
import {getAllUser} from '@/store/modules/home'
import { useDispatch, useSelector } from "react-redux";
import {http} from '@/utils/request'
import './index.scss'
const { Search } = Input;

// let data = [
// ];
let reduceData = []

// 重置用户密码的方法
const resetPassword = async(id) =>{
  const axiosData = {id}
  await http.post('/reset_password',axiosData)
 message.success('重置密码成功')
}
// 注销用户的方法
const logout = async(id) =>{
  const axiosData = {id}
  await http.post('/delete_user',axiosData)
 message.success('注销用户成功')
 setTimeout(()=>{
  window.location.reload()
 },100)
}
// 封禁用户的方法
const banned = async(id) =>{
  console.log(id);
  const axiosData = {id,role:'封禁'}
  await http.post('/update_user',axiosData)
 message.success('封禁用户成功')
 setTimeout(()=>{
  window.location.reload()
 },100)
}
const columns = [
  {
    title: '账号',
    dataIndex: 'tel',
    key: 'tel',
  },
  {
    title: '用户名',
    dataIndex: 'username',
    key: 'name',
    render: (text) => <a>{text}</a>,
  },
  {
    title: '真实名字',
    dataIndex: 'truename',
    key: 'truename',
    render:(text) => <p>{text}</p>
  },

  {  
    title: '身份',  
    key: 'role',  
    dataIndex: 'role',  
    render: (_, record) => {  
      // 移出JSX的变量声明  
      let color = record.role === '社长' ? 'geekblue' : 'green';  
      return (  
        // 不需要Fragment  
        <Tag color={color} key={record.tag}>  
          {record.role}  
        </Tag>  
      );  
    },  
  },
  {
    title: '账号状态',
    dataIndex: 'status',
    key: 'status',
    render:(text) => {
      let textColor = text === '封禁' ? 'red' : 'green'
    return  <p  style={{color:textColor}}>{text}</p>
  }

  },
  {
    title: 'Action',
    key: 'action',
    render: (record) => (
      <Space size="middle">
        <p onClick = {() =>{resetPassword(record.id)}} className="reset-password">重置密码</p>
        <p onClick={() => {logout(record.id)}} className="delete">注销</p>
        <p onClick={() => {banned(record.id)}} className="banned">封禁</p>
      </Space>
    ),
  },
];

const UtensilManage = () => {
  
  const [navName,setNavName] = useState('用户管理')
  const [navItemName, setNavItemName] = useState("用户列表");
  const [data,setData] = useState('')
  const dispatch = useDispatch()
  const getUser = async() =>{
    await  dispatch(getAllUser())
  }
  useEffect(()=>{
     getUser()
  },[])
  const res = useSelector((store) =>{
    return store.home
  })
  useEffect(()=>{
    setData(res.allUser.user)
  },[res.allUser.user])
  reduceData = res.allUser.user
  // 搜索
  const onSearch = (value, _e, info) =>{
    if(value === ''){
      
      setData(reduceData)
    }else{
      setData(data.filter((item) =>{
        return  item.tel.indexOf(value) > -1 ||
                item.username.indexOf(value) > -1 ||
                item.truename.indexOf(value) > -1
        }))  
    }
  
  } 

  return (
    <div>
      {/* 架构 */}
      <Layout name={navName} navItemName={navItemName}></Layout>
      <div className="user-list">
        <h1>用户管理 / <span>用户列表</span></h1>
        <div className="main">
        <Space style={{position:'absolute', right: '10%',top:'0%'}} direction="right">
        <Search placeholder="账号/用户名/真实姓名" onSearch={onSearch} enterButton />
        </Space>
        <Table columns={columns} dataSource={data} />
        </div>
      </div>
    </div>
  );
};
export default UtensilManage;
