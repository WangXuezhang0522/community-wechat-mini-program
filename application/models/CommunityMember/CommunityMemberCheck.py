from ..communityDB import db,CommunityMemberCheck,CommunityMember,User
from flask import request
import base64

#社团成员审核表crud

#社团成员审核表添加
def add_community_member_check(text):
    #判断是否已经存在CommunityMember
    data = CommunityMember.query.filter_by(community_id=text['community_id'],member_id=text['member_id']).first()
    if data:
        return {'status':'error','msg':'已经是社团成员'}
    data = CommunityMemberCheck(
                        community_id=text['community_id'],
                        community_name=text['community_name'],
                        member_id=text['member_id'],
                        member_name=text['member_name'],
                        role=text['role'],
                        status='待审核'
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
    
#社团成员审核表删除
def delete_community_member_check(text):
    data = CommunityMemberCheck.query.filter_by(community_id=text['community_id'],member_id=text['member_id']).first()
    try:
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
    
#社团成员审核表查询
def search_community_member_check(text):
    data = CommunityMemberCheck.query.filter_by(community_id=text['community_id']).order_by(CommunityMemberCheck.check_time.desc()).all()
    res = []
    for i in data:
        u = User.query.filter(User.id == i.member_id).first()
        UserAvatar = base64.b64encode(u.avatar).decode('utf-8')
        dict = {
            'community_id':i.community_id,
            'community_name':i.community_name,
            'member_id':i.member_id,
            'member_name':i.member_name,
            "avatar":UserAvatar,
            'role':i.role,
            'status':i.status,
            'check_time':i.check_time
            }
        res.append(dict)
    return res

#社团成员审核表更新
def update_community_member_check(text):
    data = CommunityMemberCheck.query.filter_by(community_id=text['community_id'],member_id=text['member_id']).first()
    data.status = text['status']
    if text['status'] == '审核通过':
        data_Member = CommunityMember(
                        community_id=data.community_id,
                        community_name=data.community_name,
                        member_id=data.member_id,
                        member_name=data.member_name,
                        role=data.role
                         )
        try:
            db.session.add(data_Member)
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
        
        