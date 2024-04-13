from ..communityDB import db,Admin,User,CommunityMember
import base64


#管理员表crud

#管理员表添加
def add_admin(text):
    audicodelist=['chongqing','sichuan','yunnan','superadmin']
    if text['auditCode'] not in audicodelist:
        return {'message':'auditCode error'}
    #重复判断
    data = Admin.query.filter_by(username=text['username']).first()
    if data:
        return {'message':'username repeat'}
    data = Admin(
                    username=text['username'],
                    password=text['password'],
                    auditCode=text['auditCode']
                    )
    try:
        db.session.add(data)
        db.session.commit()
        db.session.close()
        return {'message':'success'}
    except:
        db.session.rollback()
        db.session.close()
        return {'message':'errpr'}
    
#管理员表删除
def delete_admin(text):
    data = Admin.query.filter_by(username=text['username']).first()
    try:
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
    
#管理员表查询
def search_admin(text):
    data = Admin.query.filter_by(username=text['username'],password=text['password']).first()
    if data.status == '封禁':
        return {'message':'用户已被封禁'}
    if data:
        dict = {
            'username':data.username,
            'password':data.password,
            'auditCode':data.auditCode
        }
        return {'dict':dict,'message':"登录成功"}
    else:
        return {'message':"账号或密码错误"}
    

#管理员表更新
def update_admin(text):
    data = Admin.query.filter_by(id=text['id']).first()
    data.status = text['status']
    try:
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
    
#管理员表与用户表查询所有
def get_all_admin_and_user():
    data = Admin.query.all()
    list = []
    for i in data:
        dict = {
            'username':i.username,
            'password':i.password,
            'auditCode':i.auditCode
        }
        list.append(dict)

    userdata = User.query.all()
    userlist = []
    for i in userdata:
        
        communityMember = CommunityMember.query.filter_by(id=i.id).first()
        if communityMember:
            communityrole = communityMember.role
        else:
            communityrole = '游客'
        if i.role == '封禁':
            status = '封禁'
        else:
            status = '正常'
        dict = {
                'id':i.id,
                'username':i.username,
                'password':i.password,
                'truename':i.truename,
                'sex':i.sex,
                'tel':i.tel,
                'role':communityrole,
                'status':status,
        }
        userlist.append(dict)
    return {'admin':list,'user':userlist}

#重置密码
def reset_passwor_admin(text):
    data = Admin.query.filter_by(id=text['id']).first()
    data.password = 'q123456'
    try:
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'