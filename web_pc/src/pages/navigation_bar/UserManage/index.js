import React from 'react'
import { Outlet } from 'react-router-dom';
const UserManage = () => {
  return (
    <div>
      {/* 二级路由出口 */}
      <Outlet>

      </Outlet>
    </div>
  )
}
export default UserManage