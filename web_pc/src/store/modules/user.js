import { createSlice } from '@reduxjs/toolkit'
import { http } from '@/utils/request'
const userStore = createSlice({
  name: 'user',
  // 数据状态
  initialState: {
    userInfo:{}
  },
  // 同步修改方法
  reducers: {
    setUserInfo (state, action) {
      state.userInfo = action.payload
    }
  }
})

// 解构出actionCreater
const { setUserInfo } = userStore.actions

// 获取reducer函数
const userReducer = userStore.reducer

// 异步登录方法封装
const fetchLogin = (loginForm) => {
  return async (dispatch) => {
    const {account,password} = loginForm
    const data = {}
    data.username = account
    data.password = password
    const res = await http.post('/search_admin', data)
    if(res.message === '登录成功'){
      dispatch(setUserInfo(res.dict))
    }
   
    return res
  }
}
// 异步注册方法封装
const fetchRegister = (registerForm) =>{
  return async () =>{
    const {account,password,code} = registerForm
    const data = {}
    data.username = account
    data.password = password
    data.auditCode = code
    const res =  await http.post('/add_admin',data)
    return res
  }
}
export { fetchLogin,fetchRegister }

export default userReducer