from ..communityDB import db, CommunityInfo, CommunityMember
from flask import request
import base64
from PIL import Image
from io import BytesIO

#社团信息表crud
#社团信息表添加
def add_community_info(text):
    image_data = request.files.get('image')
    if image_data:
        img = Image.open(image_data)
        img.thumbnail((600, 600))  # 设置图像的最大尺寸为300x300像素
        output = BytesIO()
        img.save(output, format='JPEG', quality=50)  # 通过quality参数控制图像质量
        image_bytes = output.getvalue()
    else:
        image_bytes = None
    data = CommunityInfo(
                        name=text['name'],
                         description=text['description'],
                         image=image_bytes,
                         number=text['number'],
                         leader_name=text['leader_name'],
                         type=text['type'],
                         leader_id=text['leader_id']
                         )
    data_member = CommunityMember(
                            community_id=text['community_id'],
                            community_name=text['community_name'],
                            member_id=text['leader_id'],
                            member_name=text['leader_name'],
                            role='社团负责人'
    )
    try:
        db.session.add(data)
        db.session.add(data_member)
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
#社团信息表删除
def delete_community_info(text):
    data = CommunityInfo.query.filter_by(name=text['name']).first()
    try:
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
#社团信息表更新
def update_community_info(text):
    data = CommunityInfo.query.filter_by(name=text['name']).first()
    #图片处理
    image_data = request.files.get('image')
    if image_data:
        image_bytes = image_data.read()
    else:
        image_bytes = data.image

    data.description = text['description']
    data.image = image_bytes
    data.number = text['number']
    data.type = text['type']
    data.leader_id = text['leader_id']
    data.leader_name = text['leader_name']
    try:
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
#社团信息表查询
def search_community_info():
    data = CommunityInfo.query.all()
    list = []
    for i in data:
        if i.image == None:
            image = None
        else:
            image = base64.b64encode(i.image).decode('utf-8')
        list_dict={
            'id':i.id,
            'name':i.name,
            'introduction':i.description,
            'number':i.number,
            'type':i.type,
            'leader_id':i.leader_id,
            'leader_name':i.leader_name,
            'image':image
        }
        list.append(list_dict)
    return list

#社团信息表按名称查询
def search_community_info_by_name(text):
    data = CommunityInfo.query.filter_by(name=text['name']).first()
    if data == None:
        return "没有这个社团,尝试换一个社团名字吧"
    if data is not None:
        if data.image == None:
            image = None
        else:
            image = base64.b64encode(data.image).decode('utf-8')
    list_dict={
        'id':data.id,
        'name':data.name,
        'introduction':data.description,
        'number':data.number,
        'type':data.type,
        'leader':data.leader_id,
        'leader_name':data.leader_name,
        'image':image
    }
    return list_dict

#指定user_id查询社团负责人
def search_community_leader_by_user_id(text):
    data = CommunityInfo.query.filter_by(leader_id=text['user_id']).all()
    list = []
    for i in data:
        list_dict = {
            'id':i.id,
            'name':i.name,
            'introduction':i.description,
            'number':i.number,
            'type':i.type,
            'leader_id':i.leader_id,
            'leader_name':i.leader_name
        }
        list.append(list_dict)
    return list
