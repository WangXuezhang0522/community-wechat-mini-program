import React from 'react'
import { useState } from 'react';
import Layout  from '@/pages/Layout'
const SchoolSponsor = () => {
  const [navName,setNavName] = useState('校园赞助')
  return (
    <div>
      <Layout name = {navName}></Layout>
    </div>
  )
}
export default SchoolSponsor