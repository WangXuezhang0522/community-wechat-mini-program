from ..communityDB import db, CommunityActivityMember, CommunityActivity
from flask import request
import base64

#社团活动成员表crud

#社团活动成员表添加
def add_community_activity_member(text):
    data = CommunityActivityMember(
                                community_id=text['community_id'],#社团id
                                activity_id=text['activity_id'],#活动名称
                                user_id=text['user_id'],#用户id
                                username=text['username'],#用户姓名
                                )
    data_Activity = CommunityActivity.query.filter_by(community_id=text['community_id'],id=text['activity_id']).first()
    data_Activity.number += 1
    try:
        db.session.add(data)
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
    
#社团活动成员表删除
def delete_community_activity_member(text):
    data = CommunityActivityMember.query.filter_by(community_id=text['community_id'],activity_id=text['activity_id'],user_id=text['user_id']).first()
    data_Activity = CommunityActivity.query.filter_by(community_id=text['community_id'],id=text['activity_id']).first()
    data_Activity.number -= 1
    try:
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
    
#社团活动成员表更新
def update_community_activity_member(text):
    data = CommunityActivityMember.query.filter_by(community_id=text['community_id'],activity_name=text['activity_name'],user_id=text['user_id']).first()
    data.user_name = text['user_name']
    try:
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'

#社团活动成员表查询
def search_community_activity_member(text):
    data = CommunityActivityMember.query.filter_by(community_id=text['community_id'],activity_id=text['activity_id']).all()
    
    list = []
    for i in data:
        list.append({
            'community_id':i.community_id,
            'activity_id':i.activity_id,
            'user_id':i.user_id,
            'username':i.username
            })
    return list
    

#社团活动成员表与社团活动表联合查询活动成员信息包括活动名称,社团名称,社团id,活动id,用户id,用户姓名
def search_community_activity_memberlist(text):
    data = db.session.query(
                            CommunityActivityMember,
                            CommunityActivity
                            ).filter(
                                CommunityActivityMember.community_id == CommunityActivity.community_id,
                                CommunityActivityMember.activity_id == CommunityActivity.id,
                                ).all()
    list = []
    for i in data:
        list.append({
            'community_id':i[0].community_id,
            'activity_id':i[0].activity_id,
            'user_id':i[0].user_id,
            'username':i[0].username,
            'activity_name':i[1].name,
            'community_name':i[1].community_name
            })
    return list
    
    
#指定user_id查询我参与的活动
def search_community_activity_member_by_user_id(text):
    data = db.session.query(
                            CommunityActivityMember,
                            CommunityActivity
                            ).filter(
                                CommunityActivityMember.community_id == CommunityActivity.community_id,
                                CommunityActivityMember.activity_id == CommunityActivity.id,
                                CommunityActivityMember.user_id == text['user_id'],
                                ).all()
    list = []
    image = ''
    for i in data:
        if i[1].image:
            image = base64.b64encode(i[1].image).decode('utf-8')
        else:
            image = None
        list.append({
            'community_id':i[0].community_id,
            'activity_id':i[0].activity_id,
            'user_id':i[0].user_id,
            'username':i[0].username,
            'activity_name':i[1].name,
            'community_name':i[1].community_name,
            'address':i[1].address,
            'number':i[1].number,
            'cost':i[1].cost,
            'content':i[1].content,
            'image':image,
            'start_time':i[1].start_time,
            'end_time':i[1].end_time,
            })

    return list