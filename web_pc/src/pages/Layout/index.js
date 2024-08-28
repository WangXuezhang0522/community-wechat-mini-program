import "./index.scss";
// 导入路由依赖
import React from 'react'
import { useState} from "react";
import { Link, useNavigate } from "react-router-dom";
import { Button, Modal } from "antd";
// 导入图标资源
import indexIcon from "@/assets/layout/data.png";
import userIcon from "@/assets/layout/user_manage_icon.png";
import auditIcon from "@/assets/layout/audit_manage_icon.png";
import communityIcon from "@/assets/layout/community_manage.png";
import adsIcon from "@/assets/layout/ads_manage_icon.png";
import avatarIcon from "@/assets/layout/avatar.png";
import exit from "@/assets/layout/exit.png";
import Menu from "@/components/Menu";
import { useSelector } from "react-redux";
const Layout = (props) => {
  const navigate = useNavigate();
  const {userInfo} = useSelector((store) => store.user)
  let role = ''
  if(userInfo.auditCode == "superadmin"){
     role = '超级管理员'
  }else{
    role = '管理员'
  }
  let { name, navItemName } = props;
  const [isModalOpen, setIsModalOpen] = useState(false);
  const handleOk = (path) => {
    setIsModalOpen(false);
    navigate(path);
  };
  const handleCancel = () => {
    setIsModalOpen(false);
  };
  const navigateTo = () => {
    setIsModalOpen(true);
  };
  return (
    <div className="layout">
      <div className="header">
        <h1>社团live后台管理系统</h1>
        <div className="nav">
          <Link to="/home">
            <div
              className="nav-item"
              style={{
                backgroundColor: name === "首页" ? "rgb(23, 113, 240)" : "none",
              }}
            >
              <img src={indexIcon} />
              <p className="nav-name" alt="">
                数据可视化大屏
              </p>
            </div>
          </Link>
          <Link to="/user_manage">
            <div
              className="nav-item"
              style={{
                backgroundColor:
                  name === "用户管理" ? "rgb(23, 113, 240)" : "none",
              }}
            >
              <img src={userIcon} />
              <p className="nav-name" alt="">
                用户管理
              </p>
            </div>
          </Link>
          <Link to="/audit_center">
            <div
              className="nav-item"
              style={{
                backgroundColor:
                  name === "审核中心" ? "rgb(23, 113, 240)" : "none",
              }}
            >
              <img className="audit-img" src={auditIcon} alt="" />
              <p className="nav-name">社团/活动/帖子审核</p>
            </div>
          </Link>
          <Link to="/integrated_manage">
            <div
              className="nav-item"
              style={{
                backgroundColor:
                  name === "综合管理" ? "rgb(23, 113, 240)" : "none",
              }}
            >
              <img src={communityIcon} alt="" />
              <p className="nav-name">社团/活动/帖子管理</p>
            </div>
          </Link>
          {/* <Link to="/school_sponsor">
            <div
              className="nav-item"
              style={{
                backgroundColor:
                  name === "校园赞助" ? "rgb(23, 113, 240)" : "none",
              }}
            >
              <img src={adsIcon} alt="" />
              <p className="nav-name">校园赞助</p>
            </div>
          </Link> */}
        </div>
        {/* 搜索框 */}
        <div className="search">
          <input placeholder="Search..."></input>
        </div>
        {/* 用户 */}
        <div className="user-center">
          <img src={avatarIcon} alt=""></img>
          <div className="user-name">{role}</div>
          <img
            onClick={() => navigateTo()}
            id="exit"
            src={exit}
            alt=""
          ></img>
        </div>
      </div>
      <Menu navItemName={navItemName} name={name} />
      {/* 弹出对话框 */}
      <Modal
        title="退出登录"
        okText="确认"
        cancelText="取消"
        open={isModalOpen}
        onOk={() =>handleOk('/login')}
        onCancel={handleCancel}
      >
        <p>确认退出登录吗</p>
      </Modal>
    </div>
  );
};

export default React.memo(Layout);
