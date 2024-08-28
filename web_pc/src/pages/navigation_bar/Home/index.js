import React from 'react'
import './index.scss'
import { useState,useEffect } from 'react';
import Layout  from '@/pages/Layout'
import Activity from '@/pages/menu_item/Home/Activity';
import User from '@/pages/menu_item/Home/User';
import Community from '@/pages/menu_item/Home/Community';
import Post from '@/pages/menu_item/Home/Post';
import { useDispatch,useSelector } from 'react-redux';
import {getAllUser,getAllCommunity,getAllActivity,getAllPost} from '@/store/modules/home'
// import PostHot from '@/pages/menu_item/Home/PostHot';
const Home = () => {
  const dispatch = useDispatch()
  // 设置导航栏
  const [navName,setNavName] = useState('首页')
  // 初始化数据
  useEffect(()=>{
      // 获取所有用户与管理员信息
  const getUser = async ()=>{
    await dispatch(getAllUser())
  }
  // 获取所有社团信息
  const getCommunity= async ()=>{
    await dispatch(getAllCommunity())
  }
  // 获取所有活动信息
  const getActivity = async ()=>{
    await dispatch(getAllActivity())
  }
  // 获取所有帖子信息
  const getPost = async ()=>{
    await dispatch(getAllPost())
  }
    getUser();
    getCommunity();
    getActivity();
    getPost()
  },[])
  const {allUser,allCommunity,allActivity,allPost}  = useSelector(store => store.home)

  // console.log(allUser);
  // console.log(allCommunity);
  // console.log(allActivity);
  // console.log(allPost);
  return (
    <div>
      <Layout name = {navName} ></Layout>
      <div  className='home'>
    
      <div className='user-community'>
      <User allUser = {allUser}></User>
      <Community allCommunity = {allCommunity}></Community>
      </div>
      <div className='activity-post'>
       <Activity allActivity = {allActivity}></Activity>
      <Post allPost = {allPost}></Post>
      </div> 
      {/* <div className='post-hot'>      <PostHot></PostHot></div>         */}

      </div>
    </div>
  )
}
export default Home