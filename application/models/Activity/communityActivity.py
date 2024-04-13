from ..communityDB import db, CommunityActivity
from flask import request
import base64
from PIL import Image
from io import BytesIO
import datetime

#社团活动表crud

#社团活动表添加
def add_community_activity(text):
    image_data = request.files.get('image')
    if image_data:
        img = Image.open(image_data)
        img.thumbnail((600, 600))  # 设置图像的最大尺寸为300x300像素
        output = BytesIO()
        img.save(output, format='JPEG', quality=50)  # 通过quality参数控制图像质量
        image_bytes = output.getvalue()
    else:
        image_bytes = None
    data = CommunityActivity(
                            community_id=text['community_id'],#社团id
                            community_name=text['community_name'],#社团名称
                            leader_id=text['leader_id'],#社团负责人id
                            leader_name=text['leader_name'],#社团负责人姓名
                            name=text['name'],#活动名称
                            address=text['address'],#活动地点
                            number=text['number'],#参与人数
                            cost=text['cost'],#活动费用
                            content=text['content'],#活动内容
                            start_time=text['start_time'],#活动开始时间
                            end_time=text['end_time'],#活动结束时间
                            image=image_bytes#活动图片
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
    
#社团活动表删除
def delete_community_activity(text):
    data = CommunityActivity.query.filter_by(id=text['id']).first()
    try:
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
    
#社团活动表更新
def update_community_activity(text):
    data = CommunityActivity.query.filter_by(community_id=text['community_id'],name=text['name']).first()

    image_data = request.files.get('image')
    if image_data:
        image_bytes = image_data.read()
    else:
        image_bytes = data.image

    data.cost = text['cost']
    data.content = text['content']
    data.number = text['number']
    data.name = text['name']
    data.address = text['address']
    data.leader_id = text['leader_id']
    data.leader_name = text['leader_name']
    data.start_time = text['start_time']
    data.end_time = text['end_time']
    data.image = image_bytes
    try:
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
    
#社团活动表查询
def search_community_activity(page, per_page=5):
    data = CommunityActivity.query.order_by(CommunityActivity.start_time).paginate(page=page, 
                                                                                          per_page=per_page, 
                                                                                          error_out=False)
    result = []
    for i in data.items:
        if i.image is None:
            image = None
        else:
            image = base64.b64encode(i.image).decode('utf-8')
        item = {
            'id': i.id,
            'community_id': i.community_id,
            'community_name': i.community_name,
            'leader_id': i.leader_id,
            'leader_name': i.leader_name,
            'name': i.name,
            'address': i.address,
            'number': i.number,
            'cost': i.cost,
            'content': i.content,
            'start_time': i.start_time.strftime('%Y-%m-%d %H:%M:%S'),
            'end_time': i.end_time.strftime('%Y-%m-%d %H:%M:%S'),
            'image': image
        }
        result.append(item)
    # print(result[0])
    return result
#社团活动表查询所有,不带图片
def search_all_community_activity_noimage(text):
    data = CommunityActivity.query.all()
    

    list = []
    for i in data:
        #计算时间
        status = None
        if i.end_time < datetime.datetime.now() and i.start_time < datetime.datetime.now():
            status = '已结束'
        elif i.start_time < datetime.datetime.now() and i.end_time > datetime.datetime.now():
            status = '进行中'
        else:
            status = '未开始'
        list_dict={
            'id':i.id,
            'community_id':i.community_id,
            'community_name':i.community_name,
            'leader_id':i.leader_id,
            'leader_name':i.leader_name,
            'name':i.name,
            'address':i.address,
            'number':i.number,
            'cost':i.cost,
            'content':i.content,
            'start_time': i.start_time.strftime('%Y-%m-%d %H:%M:%S'),
            'end_time': i.end_time.strftime('%Y-%m-%d %H:%M:%S'),
            'status':status
        }
        list.append(list_dict)
    return list

#按活动名称查询社团活动
def search_community_activity_by_name(text):
    data = db.session.query(CommunityActivity).filter(CommunityActivity.name.like('%'+text['name']+'%')).first()
    list = []
    if data.image == None:
        image = None
    else:
        image = base64.b64encode(data.image).decode('utf-8')
    list_dict={
        'id':data.id,
        'community_id':data.community_id,
        'community_name':data.community_name,
        'leader_id':data.leader_id,
        'leader_name':data.leader_name,
        'name':data.name,
        'address':data.address,
        'number':data.number,
        'cost':data.cost,
        'content':data.content,
        'start_time': data.start_time.strftime('%Y-%m-%d %H:%M:%S'),
        'end_time': data.end_time.strftime('%Y-%m-%d %H:%M:%S'),
        'image':image
    }
    list.append(list_dict)
    return list

#按id查询社团活动
def search_community_activity_by_id(text):
    data = db.session.query(CommunityActivity).filter(CommunityActivity.id == text['id']).first()
    list = []
    if data.image == None:
        image = None
    else:
        image = base64.b64encode(data.image).decode('utf-8')
    list_dict={
        'id':data.id,
        'community_id':data.community_id,
        'community_name':data.community_name,
        'leader_id':data.leader_id,
        'leader_name':data.leader_name,
        'name':data.name,
        'address':data.address,
        'number':data.number,
        'cost':data.cost,
        'content':data.content,
        'start_time': data.start_time.strftime('%Y-%m-%d %H:%M:%S'),
        'end_time': data.end_time.strftime('%Y-%m-%d %H:%M:%S'),
        'image':image
    }
    list.append(list_dict)
    return list

#按id修改社团活动
def update_community_activity_by_id(text):
    data = db.session.query(CommunityActivity).filter(CommunityActivity.id == text['id']).first()
    image_data = request.files.get('image')
    if image_data:
        img = Image.open(image_data)
        img.thumbnail((600, 600))  # 设置图像的最大尺寸为300x300像素
        output = BytesIO()
        img.save(output, format='JPEG', quality=50)  # 通过quality参数控制图像质量
        image_bytes = output.getvalue()
    else:
        image_bytes = None
    data.cost = text['cost']
    data.content = text['content']
    data.number = text['number']
    data.name = text['name']
    data.address = text['address']
    data.leader_id = text['leader_id']
    data.leader_name = text['leader_name']
    data.start_time = text['start_time']
    data.end_time = text['end_time']
    data.image = image_bytes
    try:
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'

