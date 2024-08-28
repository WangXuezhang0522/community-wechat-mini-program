import axios from 'axios'

const http = axios.create({
  baseURL: 'https://w836w32324.goho.co',
  timeout: 5000,
  headers:{
    'Content-Type': 'multipart/form-data; boundary=xxxx'
  }
})

// 添加请求拦截器
http.interceptors.request.use((config)=> {
    return config
  }, (error)=> {
    return Promise.reject(error)
})

// 添加响应拦截器
http.interceptors.response.use((response)=> {
    // 2xx 范围内的状态码都会触发该函数。
    // 对响应数据做点什么
    return response.data
  }, (error)=> {
    // 超出 2xx 范围的状态码都会触发该函数。
    // 对响应错误做点什么
    return Promise.reject(error)
})

export { http }