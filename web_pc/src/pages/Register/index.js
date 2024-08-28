import './index.scss'
import {Link,useNavigate} from 'react-router-dom'
import { Card, Form, Input, Button,message } from 'antd'
import {fetchRegister} from '@/store/modules/user'
import {  useDispatch } from 'react-redux'
// 点击登录按钮时触发 参数values即是表单输入数据

const Register = () => {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const onFinish = async formValue => {
    const res = await dispatch(fetchRegister(formValue))
    if(res.message === 'success'){
      message.success('注册成功')
      navigate('/login')
    }else{
      message.error(res.message)
    }
  }
  return (
    <div className="login">
      <Card className="login-container">
        <h1>内部人员注册</h1>
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
          <Form.Item
                  name="code"
                  rules={[
                    { required: true, message: '请输入内部码' },
                    {
                      pattern: /^[a-zA-Z0-9]+$/,
                      message: '内部码只能由字母或数字组成'
                    }
                  ]}
          >
            <Input size="large" placeholder="请输入内部码" />
          </Form.Item>

          <Form.Item>
            <Button  style={{backgroundColor:'#eea909'}}   type="primary" htmlType="submit" size="large" block>
              注册
            </Button>
          </Form.Item>
        </Form>
        <Link exact to="/login" className='goLogin'>已有账号?点击去登录</Link>
      </Card>

    </div>
  )
}

export default Register