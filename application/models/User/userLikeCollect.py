from ..communityDB import db,UserLike,UserCollect,CommunityPost,User
import base64   

#用户喜欢表添加
def add_user_like(text):
    data = UserLike(
        user_id = text['user_id'],
        post_id = text['post_id']
    )
    like_data = CommunityPost.query.filter_by(id=text['post_id']).first()
    like_data.like = like_data.like+1
    try:
        db.session.add(data)
        db.session.commit()
        db.session.close()
        return 'success'
    except Exception as e :
        #抛出错误信息
        print(e)
        db.session.rollback()
        db.session.close()
        return 'error'
    
#用户喜欢表删除
def delete_user_like(text):
    data = UserLike.query.filter_by(user_id=text['user_id'],post_id=text['post_id']).first()
    like_data = CommunityPost.query.filter_by(id=text['post_id']).first()
    like_data.like = like_data.like-1
    try:
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
    
#用户喜欢表与交流贴表联合查询
def user_like_post(text):
    data = UserLike.query.filter_by(user_id=text['user_id']).all()
    res = []
    for i in data:
        post = CommunityPost.query.filter_by(id=i.post_id).order_by(CommunityPost.time.desc()).first()
        if  post is not None:
            if post.image == None:
                image = None
            else:
                image = base64.b64encode(post.image).decode('utf-8')
            user = User.query.filter_by(id=post.user_id).first()
            if user.avatar == None:
                avatar = None
            else:
                avatar = base64.b64encode(user.avatar).decode('utf-8')
            dict = {
                'id':post.id,
                'community_id':post.community_id,
                'user_id':post.user_id,
                'username':post.username,
                'avatar':avatar,
                'title':post.title,
                'content':post.content,
                'like':post.like,
                'image':image,
                'type':post.type,
                'role':post.role
            }
            res.append(dict)
    return res

#被喜欢的帖子的用户
def like_user_post(text):
   #我发的帖子
    data = CommunityPost.query.filter_by(user_id=text['user_id']).all()
    res = []
    for i in data:
        post = UserLike.query.filter_by(post_id=i.id).all()
        for j in post:
            user = User.query.filter_by(id=j.user_id).first()
            if user.avatar == None:
                avatar = None
            else:
                avatar = base64.b64encode(user.avatar).decode('utf-8')
            dict = {
                'id':user.id,
                'post_id':i.id,
                'username':user.username,
                'avatar':avatar,
            }
            res.append(dict)
    return res


#用户收藏表添加
def add_user_collect(text):
    data = UserCollect(
        user_id = text['user_id'],
        post_id = text['post_id']
    )
    try:
        db.session.add(data)
        db.session.commit()
        db.session.close()
        return 'success'
    except Exception as e :
        #抛出错误信息
        print(e)
        db.session.rollback()
        db.session.close()
        return 'error'
    
#用户收藏表删除
def delete_user_collect(text):
    data = UserCollect.query.filter_by(user_id=text['user_id'],post_id=text['post_id']).first()
    try:
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
    
#用户收藏表与交流贴表联合查询
def user_collect_post(text):
    data = UserCollect.query.filter_by(user_id=text['user_id']).all()
    res = []
    for i in data:
        post = CommunityPost.query.filter_by(id=i.post_id).order_by(CommunityPost.time.desc()).first()
        if  post is not None:
            if post.image == None:
                image = None
            else:
                image = base64.b64encode(post.image).decode('utf-8')
            user = User.query.filter_by(id=post.user_id).first()
            if user.avatar == None:
                avatar = None
            else:
                avatar = base64.b64encode(user.avatar).decode('utf-8')
            dict = {
                'id':post.id,
                'community_id':post.community_id,
                'user_id':post.user_id,
                'username':post.username,
                'avatar':avatar,
                'title':post.title,
                'content':post.content,
                'like':post.like,
                'image':image,
                'type':post.type,
                'role':post.role
            }
            res.append(dict)
    return res

#被收藏的帖子的用户
def collect_user_post(text):
   #我发的帖子
    data = CommunityPost.query.filter_by(user_id=text['user_id']).all()
    res = []
    for i in data:
        post = UserCollect.query.filter_by(post_id=i.id).all()
        for j in post:
            user = User.query.filter_by(id=j.user_id).first()
            if user.avatar == None:
                avatar = None
            else:
                avatar = base64.b64encode(user.avatar).decode('utf-8')
            dict = {
                'id':user.id,
                'post_id':i.id,
                'username':user.username,
                'avatar':avatar,
            }
            res.append(dict)
    return res