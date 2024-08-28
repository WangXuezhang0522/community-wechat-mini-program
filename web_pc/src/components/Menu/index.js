import React from "react";
import { useState, useEffect } from "react";  
import {Link, useNavigate} from 'react-router-dom'
// 导入图片素材
import { message } from "antd";
import user_list from '@/assets/menu/user_list.png'
import utensil from '@/assets/menu/utensil.png'
import community_audit from '@/assets/menu/community_audit.png'
import post_audit from '@/assets/menu/post_audit.png'
import activity_audit from '@/assets/menu/activity_audit.png'
import community_manage from '@/assets/menu/community_manage.png'
import activity_manage from '@/assets/menu/activity_manage.png'
import post_manage from '@/assets/menu/post_manage.png'
import { useSelector } from "react-redux";
import './index.scss'
const Menu = (props) => {  
  const navigate = useNavigate()
  const {userInfo} = useSelector((store) => store.user)
  const [isActiveUserList, setIsActiveUserList] = useState(false);  
  const [isActiveUtensilList, setIsActiveUtensilList] = useState(false);  
  const [isActiveCommunityAudit, setIsActiveCommunityAudit] = useState(false);  
  const [isActivePostAudit, setIsActivePostAudit] = useState(false);  
  const [isActiveCommunity, setIsActiveCommunity] = useState(false);  
  const [isActiveActivityAudit, setIsActiveActivityAudit] = useState(false);  
  const [isActivePost, setIsActivePost] = useState(false);  
  const [isActiveActivity, setIsActiveActivity] = useState(false);  
  const { navItemName, name } = props;  
  const changeActiveLocation = (name) =>{
        switch(name){
          case '用户列表':setIsActiveUserList(true); break;
          case '管理员列表':setIsActiveUtensilList(true);break;
          case '社团审核':setIsActiveCommunityAudit(true);break;
          case '帖子审核':setIsActivePostAudit(true);break;
          case '活动审核':setIsActiveActivityAudit(true);break;
          case '社团管理':setIsActiveCommunity(true);break;
          case '帖子管理':setIsActivePost(true);break;
          case '活动管理':setIsActiveActivity(true);break;
        }
  } 
  useEffect(() => {  
    changeActiveLocation(navItemName)
  }, [navItemName]); // 当navItemName变化时，重新计算状态  
const   toUtensilManage = () =>{
  if(userInfo.auditCode == "superadmin"){
    navigate('/user_manage/utensil_manage')
  }else{
   message.error('没有权限操作')
  }
    
  }
  if (name === '用户管理') {  
    return (  
      <div className="menu">  
        <div className="sub-nav">  
          {/* 用户管理 */}  
          <Link exact  to="/user_manage">  
            <div
              className={`sub-nav-item ${isActiveUserList ? 'active' : ''}`}  
            >  
              <img src={user_list} alt="404" />  
              <div className="item-name">用户列表</div>  
            </div>  
          </Link>  
          <a>  
            <div 
              onClick = {() => toUtensilManage()} 
              className={`sub-nav-item ${isActiveUtensilList ? 'active' : ''}`}  
            >  
              <img src={utensil} alt="404" />  
              <div className="item-name">管理员列表</div>  
            </div>  
          </a>  
        </div>  
      </div>  
    ); 

  }
  if(name === '审核中心') {
    return (  
      <div className="menu">  
        <div className="sub-nav">  
          {/* 社团审核 */}  
          <Link exact  to="/audit_center">  
            <div
              className={`sub-nav-item ${isActiveCommunityAudit ? 'active' : ''}`}  
            >  
              <img src={community_audit} alt="404" />  
              <div className="item-name">社团审核</div>  
            </div>  
          </Link>
          <Link exact  to="/audit_center/activity_audit">  
            <div
              className={`sub-nav-item ${isActiveActivityAudit ? 'active' : ''}`}  
            >  
              <img src={activity_audit} alt="404" />  
              <div className="item-name">活动审核</div>  
            </div>  
          </Link>  
          <Link exact  to="/audit_center/post_audit">  
            <div  
              className={`sub-nav-item ${isActivePostAudit ? 'active' : ''}`}  
            >  
              <img src={post_audit} alt="404" />  
              <div className="item-name">帖子审核</div>  
            </div>  
          </Link>  
        </div>  
      </div>  
    ); 
  }  
  if(name === '综合管理') {
    return (  
      <div className="menu">  
        <div className="sub-nav">  
          {/* 社团 */}  
          <Link exact  to="/integrated_manage">  
            <div
              className={`sub-nav-item ${isActiveCommunity ? 'active' : ''}`}  
            >  
              <img src={community_manage} alt="404" />  
              <div className="item-name">社团管理</div>  
            </div>  
          </Link>  
          <Link exact  to="/integrated_manage/activity_manage">  
            <div  
              className={`sub-nav-item ${isActiveActivity ? 'active' : ''}`}  
            >  
              <img src={activity_manage} alt="404" />  
              <div className="item-name">活动管理</div>  
            </div>  
          </Link>  
          <Link exact  to="/integrated_manage/post_activity">  
            <div  
              className={`sub-nav-item ${isActivePost ? 'active' : ''}`}  
            >  
              <img src={post_manage} alt="404" />  
              <div className="item-name">帖子管理</div>  
            </div>  
          </Link>  
        </div>  
      </div>  
    ); 
  }  
  return null;  
};  

export default Menu
