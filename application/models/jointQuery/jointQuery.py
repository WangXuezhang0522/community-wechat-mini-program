from ..communityDB import db,User,CommunityInfo,CommunityMember,CommunityActivity,CommunityPost,comment
import base64

#联合查询

#User表和CommunityMember表联合查询,用户表的所有信息与社团成员表的所有信息,通过用户的电话号码查询
def user_community_member(text):
    isUser = db.session.query(User).filter(User.tel == text['tel'],User.password == text['password']).first()
    
    if isUser == None:#用户不存在
        return '用户不存在'
    else:#用户存在
        data = db.session.query(
                                User,
                                CommunityMember
                                ).filter(
                                    User.id == CommunityMember.member_id
                                    ).filter(User.tel == text['tel'],User.password == text['password']).first()
        if data == None:#用户存在,但是没有加入社团
            userlist = []
            dict = {}
            dict['id'] = isUser.id
            dict['username'] = isUser.username
            dict['password'] = isUser.password
            dict['truename'] = isUser.truename
            dict['sex'] = isUser.sex
            dict['tel'] = isUser.tel
            if isUser.avatar == None:
                avatar_base64 = None
            else:
                avatar_base64 = base64.b64encode(isUser.avatar).decode('utf-8')
            dict['avatar'] = avatar_base64
            userlist.append(dict)
            return {'response':'没有加入社团','userlist':userlist}
        else:#用户存在,并且加入了社团
            user= data[0]
            communitymember = data[1]
            userlist = []
            dict = {}
            dict['id'] = user.id
            dict['username'] = user.username
            dict['password'] = user.password
            dict['truename'] = user.truename
            dict['sex'] = user.sex
            dict['tel'] = user.tel
            if user.avatar == None:
                avatar_base64 = None
            else:
                avatar_base64 = base64.b64encode(user.avatar).decode('utf-8')
            dict['avatar'] = avatar_base64
            dict['community_id'] = communitymember.community_id
            dict['community_name'] = communitymember.community_name
            dict['member_id'] = communitymember.member_id
            dict['member_name'] = communitymember.member_name
            dict['role'] = communitymember.role
            userlist.append(dict)
            return {'response':'用户已入社团','userlist':userlist}
        

#CommunityInfo和CommunityPost和CommunityActivity表联合查询,社团信息表的所有信息与社团帖子表与社团活动表的的所有信息
def communityinfo_communitypost_communityactivity(text):
    data = db.session.query(
                            CommunityInfo,
                            ).join(CommunityPost).join(CommunityActivity).all()
    list = []
    for i in data:
        communityinfo = i[0]
        communitypost = i[1]
        communityactivity = i[2]
        dict = {}
        dict['id'] = communityinfo.id
        dict['community_name'] = communityinfo.name
        dict['community_iamge'] = communityinfo.image
        dict['community_description'] = communityinfo.description
        dict['community_number'] = communityinfo.number
        dict['community_type'] = communityinfo.type
        dict['community_leader_id'] = communityinfo.leader_id
        dict['community_leader_name'] = communityinfo.leader_name

        dict['community_post_id'] = communitypost.id
        dict['community_post_userid'] = communitypost.user_id
        dict['community_post_username'] = communitypost.username
        dict['community_post_title'] = communitypost.title
        dict['community_post_content'] = communitypost.content
        dict['community_post_image'] = communitypost.image
        dict['community_post_like'] = communitypost.like
        dict['community_post_type'] = communitypost.type
        dict['community_post_time'] = communitypost.time

        dict['community_activity_id'] = communityactivity.id
        dict['community_activity_title'] = communityactivity.name
        dict['community_activity_content'] = communityactivity.content
        dict['community_activity_address'] = communityactivity.address
        dict['community_activity_number'] = communityactivity.number
        dict['community_activity_cost'] = communityactivity.cost
        dict['community_activity_image'] = communityactivity.image
        dict['community_activity_time'] = communityactivity.start_time
        dict['community_activity_end_time'] = communityactivity.end_time
        list.append(dict)
    return list 

#User,CommunityInfo,CommunityActivity,CommunityPost,comment分别查询所有数据,获取他们的id
def database_all_id():
    userdata = db.session.query(User).all()
    list = []
    for i in userdata:
        dict = {}
        dict['user_id'] = i.id
        list.append(dict)
    CommunityInfoData = db.session.query(CommunityInfo).all()
    for i in CommunityInfoData:
        dict = {}
        dict['community_id'] = i.id
        list.append(dict)
    CommunityActivityData = db.session.query(CommunityActivity).all()
    for i in CommunityActivityData:
        dict = {}
        dict['activity_id'] = i.id
        list.append(dict)
    CommunityPostData = db.session.query(CommunityPost).all()
    for i in CommunityPostData:
        dict = {}
        dict['post_id'] = i.id
        list.append(dict)
    commentData = db.session.query(comment).all()
    for i in commentData:
        dict = {}
        dict['comment_id'] = i.id
        list.append(dict)
    return list

#CommunityInfo和CommunityActivity和CommunityPost分别进行模糊查询
def communityinfo_activity_post_like_search(text):
    CommunityInfoData = db.session.query(CommunityInfo).filter(CommunityInfo.name.like('%'+text['text']+'%')).all()
    CommunityActivityData = db.session.query(CommunityActivity).filter(CommunityActivity.name.like('%'+text['text']+'%')).all()
    CommunityPostData = db.session.query(CommunityPost).filter(CommunityPost.title.like('%'+text['text']+'%')).all()
    CommunityInfoDataList = []
    CommunityActivityDataList = []
    CommunityPostDataList = []
    for i in CommunityInfoData:
        dict = {}
        dict['id'] = i.id
        dict['name'] = i.name
        dict['image'] = base64.b64encode(i.image).decode('utf-8')
        dict['description'] = i.description
        dict['number'] = i.number
        dict['type'] = i.type
        dict['leader_id'] = i.leader_id
        dict['leader_name'] = i.leader_name
        CommunityInfoDataList.append(dict)
    for i in CommunityActivityData:
        dict = {}
        dict['id'] = i.id
        dict['name'] = i.name
        dict['content'] = i.content
        dict['address'] = i.address
        dict['number'] = i.number
        dict['cost'] = i.cost
        dict['image'] = base64.b64encode(i.image).decode('utf-8')
        dict['start_time'] = i.start_time.strftime('%Y-%m-%d %H:%M:%S')
        dict['end_time'] = i.end_time.strftime('%Y-%m-%d %H:%M:%S')
        CommunityActivityDataList.append(dict)
    for i in CommunityPostData:
        dict = {}
        dict['id'] = i.id
        dict['userid'] = i.user_id
        dict['username'] = i.username
        dict['title'] = i.title
        dict['content'] = i.content
        dict['image'] = base64.b64encode(i.image).decode('utf-8')
        dict['like'] = i.like
        dict['type'] = i.type
        dict['time'] = i.time.strftime('%Y-%m-%d %H:%M:%S')
        CommunityPostDataList.append(dict)
    return {'CommunityInfoDataList':CommunityInfoDataList,'CommunityActivityDataList':CommunityActivityDataList,'CommunityPostDataList':CommunityPostDataList}