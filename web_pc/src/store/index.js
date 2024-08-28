import { configureStore } from '@reduxjs/toolkit'

import userReducer from './modules/user'
import homeReducer from './modules/home'
import auditReducer from './modules/auditCenter'
export default configureStore({
  reducer: {
    // 注册子模块
    user: userReducer,
    home: homeReducer,
    audit:auditReducer
  }
})