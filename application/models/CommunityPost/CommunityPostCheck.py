from ..communityDB import db,CommunityPostCheck, CommunityPost, CommunityInfo
from ...controllers import agent_invoke
from flask import request
import base64
from PIL import Image
from io import BytesIO

#社团帖子审核表crud


#社团帖子审核表添加
def add_community_post_check(text):
    image_data = request.files.get('image')
    if image_data:
        img = Image.open(image_data)
        img.thumbnail((600, 600))  # 设置图像的最大尺寸为300x300像素
        output = BytesIO()
        img.convert('RGB').save(output, format='JPEG', quality=50)  # 转换图像格式为JPEG
        image_bytes = output.getvalue()
    else:
        image_bytes = None
    data = CommunityPostCheck(
                        community_id=text['community_id'],
                        user_id=text['user_id'],
                        username=text['username'],
                        title=text['title'],
                        content=text['content'],
                        image=image_bytes,
                        type=text['type'],
                        role=text['role'],
                        status='待审核'
                        )
    try:
        db.session.add(data)
        db.session.commit()
        agent_post_check(text['community_id'],text['title'])
        return 'success'
    except Exception as e:
        db.session.rollback()
        db.session.close()
        return f'error: {e}'
    finally:
        db.session.close()

    
#社团帖子审核表删除
def delete_community_post_check(text):
    data = CommunityPostCheck.query.filter_by(community_id=text['community_id'],title=text['title']).first()
    try:
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
    
#社团帖子审核表查询-管理员
def search_community_post_check(text):
    data = CommunityPostCheck.query.all()
    res = []
    for i in data:
        CommunityInfo_data = CommunityInfo.query.filter_by(id=i.community_id).first()
        if i.status != '审核通过':
            dict = {
                'id':i.id,
                'community_id':i.community_id,
                'community_name':CommunityInfo_data.name,
                'user_id':i.user_id,
                'username':i.username,
                'title':i.title,
                'content':i.content,
                'like':i.like,
                'type':i.type,
                'role':i.role,
                'status':i.status
                }
            res.append(dict)
    return res

#社团帖子审核表查询-用户
def search_community_post_check_mini(text):
    data = CommunityPostCheck.query.filter_by(
        community_id=text['community_id']).all()
    res = []
    for i in data:
        if i.image is not None:
            image = base64.b64encode(i.image).decode('utf-8')    
        else:
            image = None
        dict = {
            'community_id':i.community_id,
            'user_id':i.user_id,
            'username':i.username,
            'title':i.title,
            'content':i.content,
            'like':i.like,
            'image':image,
            'type':i.type,
            'role':i.role,
            'status':i.status
        }
        res.append(dict)
    return res


#社团帖子审核表更新
def agent_post_check(community_id,title):
    data = CommunityPostCheck.query.filter_by(community_id=community_id,title=title).first()
    res = agent_invoke(data.content)
    print(res)
    data.status = res
    if data.status == '审核通过':
        data_Post = CommunityPost(
                        community_id=data.community_id,
                        user_id=data.user_id,
                        username=data.username,
                        title=data.title,
                        content=data.content,
                        like=data.like,
                        image=data.image,
                        type=data.type,
                        role=data.role
                        )
        try:
            db.session.add(data_Post)
            db.session.commit()
            db.session.close()
            return 'success'
        except:
            db.session.rollback()
            db.session.close()
            return 'error'
    else:
        try:
            db.session.commit()
            db.session.close()
            return 'success'
        except:
            db.session.rollback()
            db.session.close()
            return 'error'
        
def update_community_post_check(text):
    data = CommunityPostCheck.query.filter_by(id=text['id']).first()
    data.status = text['status']
    if data.status == '审核通过':
        data_Post = CommunityPost(
                        community_id=data.community_id,
                        user_id=data.user_id,
                        username=data.username,
                        title=data.title,
                        content=data.content,
                        like=data.like,
                        image=data.image,
                        type=data.type,
                        role=data.role
                        )
        try:
            db.session.add(data_Post)
            db.session.commit()
            db.session.close()
            return 'success'
        except:
            db.session.rollback()
            db.session.close()
            return 'error'
    else:
        if data.status == '审核不通过':
            #删除社团帖子
            data_Post = CommunityPost.query.filter_by(community_id=data.community_id,title=data.title).first()
            if data_Post:
               db.session.delete(data_Post)
        try:
            db.session.commit()
            db.session.close()
            return 'success'
        except:
            db.session.rollback()
            db.session.close()
            return 'error'