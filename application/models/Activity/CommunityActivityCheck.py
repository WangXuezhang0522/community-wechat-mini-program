from ..communityDB import db, CommunityActivityCheck,CommunityActivity
from ..ActivityMember.CommunityActivityMember import CommunityActivityMember
from flask import request
import base64
from PIL import Image
from io import BytesIO

#社团活动审核表crud
#社团活动审核表添加
def add_community_activity_check(text):
    image_data = request.files.get('image')
    if image_data:
        img = Image.open(image_data)
        img.thumbnail((600, 600))  # 设置图像的最大尺寸为300x300像素
        output = BytesIO()
        img.convert('RGB').save(output, format='JPEG', quality=50)  # 转换图像格式为JPEG
        image_bytes = output.getvalue()
    else:
        image_bytes = None
    data = CommunityActivityCheck(
                        community_id=text['community_id'],#社团id
                        community_name=text['community_name'],#社团名称
                        leader_id=text['leader_id'],#社团负责人id
                        leader_name=text['leader_name'],#社团负责人姓名
                        name=text['name'],#活动名称
                        address=text['address'],#活动地点
                        number=0,#参与人数
                        cost=text['cost'],#活动费用
                        content=text['content'],#活动内容
                        start_time=text['start_time'],#活动开始时间
                        end_time=text['end_time'],#活动结束时间
                        image=image_bytes,#活动图片
                        status='待审核'
                        )
    try:
        db.session.add(data)
        db.session.commit()
        db.session.close()
        return 'success'
    except Exception as e:
        db.session.rollback()
        db.session.close()
        return f'error: {str(e)}'
    
#社团活动审核表删除
def delete_community_activity_check(text):
    data = CommunityActivityCheck.query.filter_by(community_id=text['community_id'],name=text['name']).first()
    try:
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'  
#社团活动审核表查询
def search_community_activity_check(text):
    data = CommunityActivityCheck.query.filter_by(community_id=text['community_id']).order_by(CommunityActivityCheck.check_time.desc()).all()
    res = []
    for i in data:
        if i.image is not None:
            image = base64.b64encode(i.image).decode('utf-8')    
        else:
            image = None
        dict = {
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
            'start_time':i.start_time,
            'end_time':i.end_time,
            'image':image,
            'status':i.status
        }
        res.append(dict)
    return res
#社团活动审核表更新
def update_community_activity_check(text):
    data = CommunityActivityCheck.query.filter_by(id=text['id']).first()
    data.status = text['status']
    if text['status'] == '审核通过':
        data_Activity = CommunityActivity(
                        community_id=data.community_id,#社团id
                        community_name=data.community_name,#社团名称
                        leader_id=data.leader_id,#社团负责人id
                        leader_name=data.leader_name,#社团负责人姓名
                        address=data.address,#活动地点
                        name=data.name,#活动名称
                        number=data.number,#参与人数
                        cost=data.cost,#活动费用
                        content=data.content,#活动内容
                        start_time=data.start_time,#活动开始时间
                        end_time=data.end_time,#活动结束时间
                        image=data.image,#活动图片
                        )
        data_Activity_Member = CommunityActivityMember(
                                community_id=data.community_id,#社团id
                                user_id=data.leader_id,#用户id
                                username=data.leader_name,#用户姓名
                                    )
        try: 
            db.session.add(data_Activity)
            data_Activity = CommunityActivity.query.filter_by(community_id=data.community_id,name=data.name).first()
            data_Activity.number += 1
            data_Activity_Member.activity_id = data_Activity.id
            db.session.add(data_Activity_Member)
            db.session.commit()
            db.session.close()
            return 'success'
        except Exception as e:
            db.session.rollback()
            return f'error: {str(e)}'
        finally:
            db.session.close()
    else:
        try:
            db.session.commit()
            db.session.close()
            return 'success'
        except Exception as e:
            db.session.rollback()
            return f'error: {str(e)}'
        finally:
            db.session.close()