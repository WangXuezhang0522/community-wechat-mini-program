import './index.scss'
import { Card, Form, Input, Button,message } from 'antd'
import {Link, useNavigate} from 'react-router-dom'
import { fetchLogin } from '@/store/modules/user'
import { useDispatch } from 'react-redux'
// 点击登录按钮时触发 参数values即是表单输入数据

const Login = () => {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const onFinish = async formValue => {
   const res =  await dispatch(fetchLogin(formValue))
   if(res.message === '登录成功'){
    navigate('/home')
    message.success('登录成功')
   }else{
    message.error(res.message)
   }
   console.log(res);
  }
  return (
    <div className="login">
      <Card className="login-container">
        <h1>社团live后台管理系统</h1>
        {/* 登录表单 */}
        <Form onFinish={ onFinish } validateTrigger={['onBlur']}>
          <Form.Item
                  name="account"
                  rules={[
                    { required: true, message: '请输入账号' },
                    {
                      pattern: /^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}$/,
                      message: '账号格式不对,应为手机号格式'
                    }
                  ]}
          >
            <Input size="large" placeholder="请输入账号" />
          </Form.Item>
          <Form.Item
                  name="password"
                  rules={[
                    { required: true, message: '请输入密码' },
                    {
                      pattern: /^(?=.*[a-zA-Z])(?=.*\d).{2,11}$/,
                      message: '密码至少由一个数字及一个字母组成且不超过11位'
                    }
                  ]}
          >
            <Input size="large" placeholder="请输入密码" />
          </Form.Item>
          <Form.Item>
            <Button  type="primary" htmlType="submit" size="large" block>
              登录
            </Button>
          </Form.Item>
        </Form>
        <Link exact to="/register" className='goRegister'>还没有账号?点击去注册</Link>
      </Card>

    </div>
  )
}

export default Login