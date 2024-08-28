import { createSlice } from "@reduxjs/toolkit";
import { http } from "@/utils/request";
const homeStore = createSlice({
  name: "home",
  // 数据状态
  initialState: {
    allUser: [],
    allCommunity: [],
    allActivity: [],
    allPost: [],
  },
  // 同步修改方法
  reducers: {
    setAllUser(state, action) {
      state.allUser = action.payload;
    },
    setAllCommunity(state, action) {
      state.allCommunity = action.payload;
    },
    setAllActivity(state, action) {
      state.allActivity = action.payload;
    },
    setAllPost(state, action) {
      state.allPost = action.payload;
    },
  },
});

// 解构出actionCreater
const { setAllUser,setAllCommunity,setAllActivity,setAllPost} = homeStore.actions;

// 获取reducer函数
const homeReducer = homeStore.reducer;

// 异步获取所有用户信息
const getAllUser = () =>{
    return async (dispatch)=>{
      const res =   await  http.post('/get_all_admin_and_user')
      dispatch(setAllUser(res))
      
    }
}
// 异步获取所有社团信息
const getAllCommunity = () =>{
    return async (dispatch)=>{
      let res =   await  http.post('/search_all_community_info_noimage')
      const newData = res.slice(1)
      dispatch(setAllCommunity(newData))
    }
}
// 异步获取所有活动信息
const getAllActivity = () =>{
    return async (dispatch)=>{
      const res =   await  http.post('/search_all_community_activity_noimage')
      dispatch(setAllActivity(res))
    }
}
// 异步获取所有帖子信息
const getAllPost = () =>{
    return async (dispatch)=>{
      const res =   await  http.post('/search_all_community_post_noimage')
      dispatch(setAllPost(res))
      console.log(res);
    }
}
export { getAllUser,getAllCommunity,getAllActivity,getAllPost };

export default homeReducer;
