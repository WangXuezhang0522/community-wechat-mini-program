import React from 'react'
import { useState } from 'react';
import Layout  from '@/pages/Layout'
const IntegratedManage = () => {
  const [navName,setNavName] = useState('综合管理')

  return (
    <div>
      <Layout name = {navName} ></Layout>
    </div>
  )
}
export default IntegratedManage