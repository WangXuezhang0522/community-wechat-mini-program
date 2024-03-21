from ..communityDB import db, comment, CommunityPost, User
import base64

#评论表crud

#评论表添加
def add_comment(text):
    data =comment(
                    post_id=text['post_id'],
                    user_id=text['user_id'],
                    username=text['username'],
                    content=text['content'],
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
    
#评论表删除
def delete_comment(text):
    data = comment.query.filter_by(id=text['id']).first()
    try:
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
    
#评论表查询
def search_comment(text):
    data = comment.query.all()
    list=[]
    for i in data:
        list.append({
            'id':i.id,
            'post_id':i.post_id,
            'user_id':i.user_id,
            'content':i.content,
            'username':i.username,
            'like':i.like,
            'time':i.time
            })
    return list

#帖子被评论的用户
def comment_user_post(text):
    #我发的帖子
    data = CommunityPost.query.filter_by(user_id=text['user_id']).all()
    res = []
    for i in data:
        post = comment.query.filter_by(post_id=i.id).all()
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

#评论表点赞
def like_comment(text):
    data = comment.query.filter_by(id=text['id']).first()
    data.like += 1
    try:
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
    
#评论表取消点赞
def unlike_comment(text):
    data = comment.query.filter_by(id=text['id']).first()
    data.like -= 1
    try:
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
    
    