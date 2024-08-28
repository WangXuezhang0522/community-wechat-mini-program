import React from "react";
import { useState,useEffect } from "react";
import Layout from "@/pages/Layout";
import { Space, Table, Tag,message} from 'antd';
import {getAllUser} from '@/store/modules/home'
import { useDispatch, useSelector } from "react-redux";
import {http} from '@/utils/request'
import './index.scss'
let data = [

];
// 重置管理员密码的方法
const resetPassword = async(id) =>{
  const axiosData = {id}
  await http.post('/reset_password_admin',axiosData)
 message.success('重置密码成功')
 setTimeout(()=>{
  window.location.reload()
 },100)
 
}
// 注销管理员的方法
const logout = async(id) =>{
  const axiosData = {id}
  await http.post('/delete_admin',axiosData)
 message.success('注销管理员成功')
 setTimeout(()=>{
  window.location.reload()
 },100)
}
// 封禁管理员的方法
const banned = async(id) =>{
  const axiosData = {id,status:'封禁'}
  await http.post('/update_admin',axiosData)
 message.success('封禁管理员成功')
 setTimeout(()=>{
  window.location.reload()
 },100)
}
const columns = [
  {
    title: '账号',
    dataIndex: 'username',
    key: 'username',
  },
  {
    title: '密码',
    dataIndex: 'password',
    key: 'password',
    render: (text) => <a>{text}</a>,
  },
  {
    title: '内部码',
    dataIndex: 'auditCode',
    key: 'auditCode',
  },

  {
    title: 'Action',
    key: 'action',
    render: (record) => (
      <Space size="middle">
        <p onClick = {() =>{resetPassword(record.id)}} className="reset-password">重置密码</p>
        <p onClick={() => {logout(record.id)}} className="delete">注销</p>
        <p nClick={() => {banned(record.id)}} className="banned">封禁</p>
      </Space>
    ),
  },
];

const UtensilManage = () => {
  const [navName,setNavName] = useState('用户管理')
  const [navItemName, setNavItemName] = useState("管理员列表");
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
  data = res.allUser.admin
  console.log(data);
  return (
    <div>
      {/* 架构 */}
      <Layout name={navName} navItemName={navItemName}></Layout>
      <div className="user-list">
        <h1>用户管理 / <span>管理员列表</span></h1>
        <div className="main">

        <Table columns={columns} dataSource={data} />
        </div>
      </div>
    </div>
  );
};
export default UtensilManage;
