import { createBrowserRouter} from 'react-router-dom'

import Login from '../pages/Login'
import Register from '../pages/Register'
import Home from '@/pages/navigation_bar/Home'
import SchoolSponsor from '@/pages/navigation_bar/SchoolSponsor'
import UserList from '@/pages/menu_item/UserList'
import UtensilManage from '@/pages/menu_item/UtensilManage'
import CommunityAudit from '@/pages/menu_item/Audit_Center/CommunityAudit'
import PostAudit from '@/pages/menu_item/Audit_Center/PostAudit'
import ActivityAudit from '@/pages/menu_item/Audit_Center/ActivityAudit'
import Activity from '@/pages/menu_item/Integrated_Manage/Activity'
import Community from '@/pages/menu_item/Integrated_Manage/Community'
import Post from '@/pages/menu_item/Integrated_Manage/Post'

const router = createBrowserRouter([
  // 默认
  {
    path: '/',
    element: < Login/> ,
  },
  // 登录页
  {
    path: '/login',
    element: < Login/> ,
  },
  // 注册页
  {
    path: '/register',
    element:<Register></Register>
  },
  // 首页
  {
    path: '/home',
    element: < Home/>,
  },
  // 用户管理
  {
      path: '/user_manage',
      children:[
        {
        index:true,
        element:<UserList/>
        },
        {
          path:'utensil_manage',
          element:<UtensilManage/>
        }
    ]
  },
  // 审核中心
  {
    path: '/audit_center',
    children:[
      {
        index:true,
        element:<CommunityAudit></CommunityAudit>
      },
      {
        path:'post_audit',
        element:<PostAudit></PostAudit>
      },
      {
        path:'activity_audit',
        element:<ActivityAudit></ActivityAudit>
      }

    ]
  },

  // 综合管理
  {
    path: '/integrated_manage',
    children:[
      {
        index:true,
        element:<Community></Community>
      },
      {
        path:'activity_manage',
        element:<Activity></Activity>
      },
      {
        path:'post_activity',
        element:<Post></Post>
      }
    ]
  },
  // 企业赞助
  {
    path: '/school_sponsor',
    element: < SchoolSponsor />,
  }
])

export default router