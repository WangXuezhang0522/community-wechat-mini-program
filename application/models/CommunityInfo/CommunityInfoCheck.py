from ..communityDB import db,CommunityInfoCheck,CommunityInfo,CommunityMember
from flask import request
import base64
from PIL import Image
from io import BytesIO
#社团信息审核表crud

#社团信息审核表添加
def add_community_info_check(text):
    image_data = request.files.get('image')
    if image_data:
        img = Image.open(image_data)
        img.thumbnail((600, 600))  # 设置图像的最大尺寸为300x300像素
        output = BytesIO()
        img.convert('RGB').save(output, format='JPEG', quality=50)  # 转换图像格式为JPEG
        image_bytes = output.getvalue()
    else:
        image_bytes = None
    status = '待审核'
    data = CommunityInfoCheck(
                         name=text['name'],
                         description=text['description'],
                         image=image_bytes,
                         number=text['number'],
                         leader_name=text['leader_name'],
                         type=text['type'],
                         leader_id=text['leader_id'],
                         status=status
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
    
#社团信息审核表删除
def delete_community_info_check(text):
    data = CommunityInfoCheck.query.filter_by(name=text['name']).first()
    try:
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
    
#社团信息审核表查询
def search_community_info_check(text):
    data = CommunityInfoCheck.query.filter_by().order_by(CommunityInfoCheck.check_time.desc()).all()
    res = []
    for i in data:
        # if i.image is not None:
        #     image = base64.b64encode(i.image).decode('utf-8')    
        # else:
        #     image = None
        if i.status != '审核通过':
            dict = {
                'name':i.name,
                'description':i.description,
                # 'image':image,
                'number':i.number,
                'leader_name':i.leader_name,
                'type':i.type,
                'leader_id':i.leader_id,
                'status':i.status
            }
            res.append(dict)
    return res
    
#社团信息审核表更新
def update_community_info_check(text):
    data = CommunityInfoCheck.query.filter_by(id=text['id']).first()
    data.status = text['status']
    if text['status'] == '审核通过':
        data_Info = CommunityInfo(
                         name=data.name,
                         description=data.description,
                         image=data.image,
                         number=data.number,
                         leader_name=data.leader_name,
                         type=data.type,
                         leader_id=data.leader_id
                         )
        data_member = CommunityMember(
                            community_name=data.name,
                            member_id=data.leader_id,
                            member_name=data.leader_name,
                            role='社长'
    )
        try:
            db.session.add(data_Info)
            data_Info = CommunityInfo.query.filter_by(name=data.name).first()
            data_member.community_id = data_Info.id
            db.session.add(data_member)
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