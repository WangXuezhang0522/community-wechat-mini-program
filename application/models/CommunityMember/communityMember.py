from ..communityDB import db, CommunityMember,CommunityMemberCheck

#社团成员表crud

#社团成员表添加
def add_community_member(text):
    data = CommunityMember(
                        community_id=text['community_id'],
                        community_name=text['community_name'],
                        member_id=text['member_id'],
                        member_name=text['member_name'],
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
    
#社团成员表删除
def delete_community_member(text):
    data = CommunityMember.query.filter_by(community_id=text['community_id'],member_id=text['member_id']).first()
    dataCheck = CommunityMemberCheck.query.filter_by(community_id=text['community_id'],member_id=text['member_id']).first()
    try:
        db.session.delete(data)
        db.session.delete(dataCheck)
        db.session.commit()
        db.session.close()
        return 'success'
    except Exception as e:
        db.session.rollback()
        db.session.close()
        return f'error:{e}'
    
#社团成员表更新
def update_community_member(text):
    data = CommunityMember.query.filter_by(community_id=text['community_id'],member_id=text['member_id']).first()
    data.role = text['role']
    data.member_name = text['member_name']
    try:
        db.session.commit()
        db.session.close()
        return 'success'
    except:
        db.session.rollback()
        db.session.close()
        return 'error'
    
#社团成员表查询
def search_community_member(text):
    data = CommunityMember.query.filter_by(community_id=text['community_id']).all()
    list = []
    for i in data:
        list_dict = {
            'id':i.id,
            'community_id':i.community_id,
            'community_name':i.community_name,
            'member_id':i.member_id,
            'member_name':i.member_name,
            'role':i.role
        }
        list.append(list_dict)
    return list


#指定user_id查询我加入的社团
def search_community_member_by_user_id(text):
    data = CommunityMember.query.filter_by(member_id=text['member_id']).all()
    list = []
    for i in data:
        list_dict = {
            'id':i.id,
            'community_id':i.community_id,
            'community_name':i.community_name,
            'member_id':i.member_id,
            'member_name':i.member_name,
            'role':i.role
        }
        list.append(list_dict)
    return list

