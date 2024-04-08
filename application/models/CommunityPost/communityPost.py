from ..communityDB import db, CommunityPost,User,UserCollect,comment
from flask import request
import base64
from PIL import Image
from io import BytesIO

#交流贴表crud

#交流贴表添加
def add_community_post(text):
    image_data = request.files.get('image')
    if image_data:
        img = Image.open(image_data)
        img.thumbnail((600, 600))  # 设置图像的最大尺寸为300x300像素
        output = BytesIO()
        img.save(output, format='JPEG', quality=50)  # 通过quality参数控制图像质量
        image_bytes = output.getvalue()
    else:
        image_bytes = None
    data = CommunityPost(
                        community_id=text['community_id'],
                        user_id=text['user_id'],
                        username=text['username'],
                        title=text['title'],
                        content=text['content'],
                        like=text['like'],
                        image=image_bytes,
                        type=text['type'],
                        role=text['role']
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
    
#交流贴表删除
def delete_community_post(text):
    data = CommunityPost.query.filter_by(title=text['title']).first()
    try:
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
    
#交流贴表更新
def update_community_post(text):
    data = CommunityPost.query.filter_by(id=text['id'],title=text['title']).first()
    image_data = request.files.get('image')
    if image_data:
        image_bytes = image_data.read()
    else:
        image_bytes = data.image
    data.title = text['title']
    data.content = text['content']
    data.image = image_bytes
    data.type = text['type']
    data.role = text['role']
    try:
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
    
#交流贴表查询
def search_community_post(text,page=1,per_page=10):
    data = CommunityPost.query.filter_by(community_id=text['community_id']).order_by(CommunityPost.time.desc()).paginate(page=page, 
                                                                            per_page=per_page,
                                                                            error_out=False)
    list = []
    for i in data.items:
        if i.image == None:
            image = None
        else:
            image = base64.b64encode(i.image).decode('utf-8')
        user = User.query.filter_by(id=i.user_id).first()
        if user.avatar == None:
            avatar = None
        else:
            avatar = base64.b64encode(user.avatar).decode('utf-8')
        #获取评论数
        commentCount = comment.query.filter_by(post_id=i.id).count()
        #获取收藏数
        collectCount = UserCollect.query.filter_by(post_id=i.id).count()
        list_dict = {
            'id':i.id,
            'community_id':i.community_id,
            'user_id':i.user_id,
            'username':i.username,
            'avatar':avatar,
            'title':i.title,
            'content':i.content,
            'like':i.like,
            'image':image,
            'type':i.type,
            'role':i.role,
            'time':i.time.strftime('%Y-%m-%d %H:%M:%S'),
            'commentCount':commentCount,
            'collectCount':collectCount
        }
        list.append(list_dict)
    return list


#交流贴表id查询
def search_community_post_by_title(text):
    try:
        data = CommunityPost.query.filter_by(id=text['id']).first()
        user = User.query.filter_by(id=data.user_id).first()
        if user.avatar == None:
            avatar = None
        else:
            avatar = base64.b64encode(user.avatar).decode('utf-8')
        if data.image == None:
            image = None
        else:
            image = base64.b64encode(data.image).decode('utf-8')

        list_dict = {
            'id':data.id,
            'community_id':data.community_id,
            'user_id':data.user_id,
            'username':data.username,
            'avatar':avatar,
            'title':data.title,
            'content':data.content,
            'like':data.like,
            'image':image,
            'type':data.type,
            'role':data.role,
            'time':data.time.strftime('%Y-%m-%d %H:%M:%S')
        }
        #获取评论
        comment_data = comment.query.filter_by(post_id=data.id).all()
        comment_list = []
        for i in comment_data:
            user = User.query.filter_by(id=i.user_id).all()
            for j in user:
                if j.avatar == None:
                    avatar = None
                else:
                    avatar = base64.b64encode(j.avatar).decode('utf-8')
                dict = {
                    'id':i.id,
                    'user_id':i.user_id,
                    'username':i.username,
                    'avatar':avatar,
                    'content':i.content,
                    'time':i.time.strftime('%Y-%m-%d %H:%M:%S')
                }
                comment_list.append(dict)
        list_dict['comment'] = comment_list
        return list_dict
    except Exception as e:
        return f'error:{e}'

#根据社区id查询
def search_community_post_by_community_id(text, page, per_page=5):
    data = CommunityPost.query.filter_by(community_id=text['community_id']).order_by(
        CommunityPost.time.desc()).paginate(
            page=page, per_page=per_page,error_out = False)
    list = []
    for i in data.items:
        if i.image == None:
            image = None
        else:
            image = base64.b64encode(i.image).decode('utf-8')
        user = User.query.filter_by(id=i.user_id).first()
        if user.avatar == None:
            avatar = None
        else:
            avatar = base64.b64encode(user.avatar).decode('utf-8')
        list_dict = {
            'id':i.id,
            'community_id':i.community_id,
            'user_id':i.user_id,
            'username':i.username,
            'avatar':avatar,
            'title':i.title,
            'content':i.content,
            'like':i.like,
            'image':image,
            'type':i.type,
            'role':i.role,
            'time':i.time.strftime('%Y-%m-%d %H:%M:%S')
        }
        list.append(list_dict)
    return list


#指定user_id查询
def search_community_post_by_user_id(text):
    data = CommunityPost.query.filter_by(user_id=text['user_id']).order_by(CommunityPost.time.desc()).all()
    list = []
    for i in data:
        if i.image == None:
            image = None
        else:
            image = base64.b64encode(i.image).decode('utf-8')
        user = User.query.filter_by(id=i.user_id).first()
        if user.avatar == None:
            avatar = None
        else:
            avatar = base64.b64encode(user.avatar).decode('utf-8')
        list_dict = {
            'id':i.id,
            'community_id':i.community_id,
            'user_id':i.user_id,
            'username':i.username,
            'avatar':avatar,
            'title':i.title,
            'content':i.content,
            'like':i.like,
            'image':image,
            'type':i.type,
            'role':i.role,
            'time':i.time.strftime('%Y-%m-%d %H:%M:%S')
        }
        list.append(list_dict)
    return list

#交流表点赞
def like_community_post(text):
    data = CommunityPost.query.filter_by(id=text['id']).first()
    data.like = data.like+1
    try:
        db.session.commit()
        db.session.close()
        return 'success'                                                                         
    except:
        db.session.rollback()
        db.session.close()
        return 'error'