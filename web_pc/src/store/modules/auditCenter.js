import { createSlice } from '@reduxjs/toolkit'
import { http } from '@/utils/request'
const auditStore = createSlice({
  name: 'auditCenter',
  // 数据状态
  initialState: {
    communityAudit:[],
    activityAudit:[],
    postAudit:[]

  },
  // 同步修改方法
  reducers: {
   setCommunityAudit(state,action){
    state.communityAudit = action.payload
   },
   setActivityAudit(state,action){
    state.activityAudit = action.payload
   },
   setPostAudit(state,action){
    state.postAudit = action.payload
   }
  }
})

// 解构出actionCreater
const { setCommunityAudit,setActivityAudit,setPostAudit } = auditStore.actions

// 获取reducer函数
const auditReducer = auditStore.reducer

// 异步获取待审核社团列表
const getCommunityAudit = () =>{
  return async (dispatch) =>{
    const res = await http.post('/search_community_info_check')
    dispatch(setCommunityAudit(res))
  }
}
// 异步获取待审核活动列表
const getActivityAudit = () =>{
  return async (dispatch) =>{
    const res = await http.post('/search_community_activity_check')
    dispatch(setActivityAudit(res))
  }
}
// 异步获取待审核帖子列表
const getPostAudit = () =>{
  return async (dispatch) =>{
    const res = await http.post('/search_community_post_check')
    dispatch(setPostAudit(res))
    console.log(res);
  }
}
export {  getCommunityAudit,getActivityAudit,getPostAudit}

export default auditReducer