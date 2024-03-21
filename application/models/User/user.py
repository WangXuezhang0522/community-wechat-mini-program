from ..communityDB import db, User
from flask import request
import base64
from PIL import Image
from io import BytesIO

#用户表crud
#用户表添加
def add_user(text):
    #禁止重复username注册
    if User.query.filter_by(username=text['username']).first() is not None:
        return {'message':'用户名已存在'}
    elif User.query.filter_by(tel=text['tel']).first() is not None: 
        return {'message':'手机号已存在'}
    
    image_data = request.files.get('avatar')
    if image_data:
        img = Image.open(image_data)
        img.thumbnail((600, 600))  # 设置图像的最大尺寸为300x300像素
        output = BytesIO()
        img.convert('RGB').save(output, format='JPEG', quality=50)  # 转换图像格式为JPEG
        image_bytes = output.getvalue()     
    else:
        image_bytes = None
    
    data = User(
        username = text['username'],
        password = text['password'],
        truename = text['truename'],
        tel = text['tel'],
        avatar = image_bytes,
        sex = text['sex'],
        # role = "用户" if text['role'] is None else text['role'] 
    )
    try:
        db.session.add(data)
        db.session.commit()
        db.session.close()
        return {'message':'注册成功'}
    except Exception as e :
        #抛出错误信息
        print(e)
        db.session.rollback()
        db.session.close()
        return {'message':f'注册失败:{e}'}
#用户表删除
def delete_user(text):
    data = User.query.filter_by(username=text['username']).first()
    try:
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
#用户表更新
def update_user(text):
    data = User.query.filter_by(tel=text['tel'],password=text['password']).first()

    data.username = text['username']
    data.sex = text['sex']
    
    image_data = request.files.get('avatar')
    if image_data:
        image_bytes = image_data.read()
    else:
        image_bytes = data.avatar
    data.avatar = image_bytes
    try:
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
#用户表查询
def search_user(text):
    data = User.query.filter_by(tel=text['tel'],password=text['password']).first()
    
        
    # 将查询结果转换为json列表
    result_list = []
    
    if data:
        if text['password'] == data.password:
            user_dict = {
                'id': data.id,
                'username': data.username,
                'password': data.password,
                'truename': data.truename,
                'sex': data.sex,
                'tel': data.tel
            }
            if data.avatar:
                avatar_base64 = base64.b64encode(data.avatar).decode('utf-8')
                user_dict['avatar'] = avatar_base64
            
            result_list.append(user_dict)
    
    return result_list

#获取所有用户
def get_all_user():
    data = User.query.all()
    res = []
    for i in data:
        if i.avatar is not None:
            avatar = base64.b64encode(i.avatar).decode('utf-8')    
        else:
            avatar = None
        dict = {
            'id':i.id,
            'username':i.username,
            'password':i.password,
            'truename':i.truename,
            'sex':i.sex,
            'tel':i.tel,
            'avatar':avatar
        }
        res.append(dict)
    return res