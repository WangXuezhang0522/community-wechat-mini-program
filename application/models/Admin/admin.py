from ..communityDB import db,Admin,User
import base64


#管理员表crud

#管理员表添加
def add_admin(text):
    audicodelist=['chongqing','sichuan','yunnan']
    if text['auditCode'] not in audicodelist:
        return 'auditCode error'
    data = Admin(
                    username=text['username'],
                    password=text['password'],
                    auditCode=text['auditCode']
                    )
    try:
        db.session.add(data)
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
    
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
    data = Admin.query.filter_by(username=text['username']).first()
    if data:
        dict = {
            'username':data.username,
            'password':data.password,
            'auditCode':data.auditCode
        }
        return dict
    else:
        return {'message':"没有该管理员"}
    

    
#管理员表更新
def update_admin(text):
    data = Admin.query.filter_by(username=text['username']).first()
    data.password = text['password']
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
        dict = {
            'id':i.id,
            'username':i.username,
            'password':i.password,
            'truename':i.truename,
            'sex':i.sex,
            'tel':i.tel
        }
        userlist.append(dict)
    return {'admin':list,'user':userlist}