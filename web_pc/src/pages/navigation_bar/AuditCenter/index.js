import React from 'react'
import { useState } from 'react';
import Layout  from '@/pages/Layout'
const AuditCenter = () => {
  const [navName,setNavName] = useState('审核中心')
  return (
    <div>
      <Layout name = {navName}></Layout>
    </div>
  )
}
export default AuditCenter