from flask import Flask,request
from flask_cors import CORS
from application.configs import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, SQLALCHEMY_ECHO
from application.models.communityDB import db,create_db
from application.controllers import search_recommend
from application.models import( 
                add_user, 
                delete_user,
                search_user, 
                update_user,
                get_all_user)
from application.models import (add_community_info, 
                            delete_community_info, 
                            search_community_info, 
                            update_community_info,
                            search_community_info_by_name,
                            search_community_leader_by_user_id)
from application.models import (add_community_activity, 
                                delete_community_activity,
                                  search_community_activity, 
                                  search_community_activity_by_name,
                                  update_community_activity)
from application.models import (add_community_member, 
                              delete_community_member,
                                search_community_member,
                                search_community_activity_memberlist,
                                  update_community_member,
                                  search_community_member_by_user_id)
from application.models import (add_community_post,
                             delete_community_post,
                               search_community_post,
                                 update_community_post,
                                 search_community_post_by_title,
                                search_community_post_by_user_id,
                                 like_community_post)
from application.models import (add_comment,
                                delete_comment,
                                    search_comment,
                                    like_comment,
                                     unlike_comment,
                                     comment_user_post)
from application.models import (
    user_community_member,
    communityinfo_communitypost_communityactivity
)


from application.models import (add_community_activity_check,
                                              delete_community_activity_check,
                                              search_community_activity_check,
                                              update_community_activity_check)
from application.models import (add_community_activity_member,
                                                      delete_community_activity_member,
                                                      search_community_activity_member,
                                                      update_community_activity_member,
                                                      search_community_activity_member_by_user_id)
from application.models import (add_admin,
                          delete_admin,
                          search_admin,
                          update_admin,get_all_admin_and_user)
from application.models import (add_community_info_check,
                                              delete_community_info_check,
                                              search_community_info_check,
                                              update_community_info_check)
from application.models import (add_community_member_check,
                                                  delete_community_member_check,
                                                  search_community_member_check,
                                                  update_community_member_check)
from application.models import (add_community_post_check,
                                              delete_community_post_check,
                                              search_community_post_check,
                                              update_community_post_check)
from application.models import (add_user_collect,
                                  delete_user_collect,
                                  add_user_like,
                                  delete_user_like,
                                  user_like_post,
                                  user_collect_post,
                                  like_user_post,
                                  collect_user_post)
from application.models import (insertCarousel,deleteCarousel,searchCarousel)
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# 关闭动态追踪修改的警告信息
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
# 展示sql语句
app.config['SQLALCHEMY_ECHO'] = SQLALCHEMY_ECHO
# 关联app和sqlalchemy对象
db.init_app(app)

#路由视图
#初始化
@app.route('/initdb',methods=['GET'])
def initdb():
    res=create_db()
    return res

#检索推荐功能
@app.route('/search_recommend',methods=['POST'])
def recommend():
    human_input = request.form.get('text')
    res=search_recommend(human_input)
    return res

#所有用户
@app.route('/get_all_user',methods=['POST'])
def alluser():
    res=get_all_user()
    return res

#增加用户
@app.route('/add_user',methods=['POST'])
def adduser():
    text = request.form
    res=add_user(text)
    return res

#删除用户
@app.route('/delete_user',methods=['POST'])
def deleteuser():
    text = request.form
    res=delete_user(text)
    return res

#查询用户
@app.route('/search_user',methods=['POST'])
def searchuser():
    text = request.form
    res=search_user(text)
    return res
#更新用户
@app.route('/update_user',methods=['POST'])
def updateuser():
    text = request.form
    res=update_user(text)
    return res

#增加社团信息
@app.route('/add_community_info',methods=['POST'])
def addcommunityinfo():
    text = request.form
    res=add_community_info(text)
    return res

#删除社团信息
@app.route('/delete_community_info',methods=['POST'])
def deletecommunityinfo():
    text = request.form
    res=delete_community_info(text)
    return res

#查询社团信息
@app.route('/search_community_info',methods=['POST'])
def searchcommunityinfo():
    text = request.form
    res=search_community_info()
    return res

#按名称查询社团信息
@app.route('/search_info_by_name',methods=['POST'])
def searchcommunityinfobyname():
    text = request.form
    res=search_community_info_by_name(text)
    return res

#更新社团信息
@app.route('/update_community_info',methods=['POST'])
def updatecommunityinfo():
    text = request.form
    res=update_community_info(text)
    return res

#增加社团活动
@app.route('/add_community_activity',methods=['POST'])
def addcommunityactivity():
    text = request.form
    res=add_community_activity(text)
    return res

#删除社团活动
@app.route('/delete_community_activity',methods=['POST'])
def deletecommunityactivity():
    text = request.form
    res=delete_community_activity(text)
    return res

#查询社团活动
@app.route('/search_community_activity',methods=['POST'])
def searchcommunityactivity():
    text = request.form
    res=search_community_activity()
    return res

#按名称查询社团活动
@app.route('/search_activity_by_name',methods=['POST'])
def searchcommunityactivitybyname():
    text = request.form
    res=search_community_activity_by_name(text)
    return res

#更新社团活动
@app.route('/update_community_activity',methods=['POST'])
def updatecommunityactivity():
    text = request.form
    res=update_community_activity(text)
    return res

#增加社团成员
@app.route('/add_community_member',methods=['POST'])
def addcommunitymember():
    text = request.form
    res=add_community_member(text)
    return res

#删除社团成员
@app.route('/delete_community_member',methods=['POST'])
def deletecommunitymember():
    text = request.form
    res=delete_community_member(text)
    return res

#查询社团成员
@app.route('/search_community_member',methods=['POST'])
def searchcommunitymember():
    text = request.form
    res=search_community_member(text)
    return res

#更新社团成员
@app.route('/update_community_member',methods=['POST'])
def updatecommunitymember():
    text = request.form
    res=update_community_member(text)
    return res

#增加社团帖子
@app.route('/add_community_post',methods=['POST'])
def addcommunitypost():
    text = request.form
    res=add_community_post(text)
    return res

#删除社团帖子
@app.route('/delete_community_post',methods=['POST'])
def deletecommunitypost():
    text = request.form
    res=delete_community_post(text)
    return res

#查询社团帖子
@app.route('/search_community_post',methods=['POST'])
def searchcommunitypost():
    text = request.form
    res=search_community_post(text)
    return res

#更新社团帖子
@app.route('/update_community_post',methods=['POST'])
def updatecommunitypost():
    text = request.form
    res=update_community_post(text)
    return res

#按标题查询社团帖子
@app.route('/search_post_by_title',methods=['POST'])
def searchcommunitypostbytitle():
    text = request.form
    res=search_community_post_by_title(text)
    return res

#点赞社团帖子
@app.route('/like_community_post',methods=['POST'])
def likecommunitypost():
    text = request.form
    res=like_community_post(text)
    return res

#增加评论
@app.route('/add_comment',methods=['POST'])
def addcomment():
    text = request.form
    res=add_comment(text)
    return res

#删除评论
@app.route('/delete_comment',methods=['POST'])
def deletecomment():
    text = request.form
    res=delete_comment(text)
    return res

#查询评论
@app.route('/search_comment',methods=['POST'])
def searchcomment():
    text = request.form
    res=search_comment(text)
    return res

#点赞评论
@app.route('/like_comment',methods=['POST'])
def likecomment():
    text = request.form
    res=like_comment(text)
    return res

#取消点赞评论
@app.route('/unlike_comment',methods=['POST'])
def unlikecomment():
    text = request.form
    res=unlike_comment(text)
    return res

#联合查询用户信息与社团成员信息
@app.route('/isLogin',methods=['POST'])
def usercommunitymember():
    text = request.form
    
    res=user_community_member(text)
    return res

@app.route('/Login',methods=['POST'])
def login():
    text = request.args
    print(text['tel']) 
    res=user_community_member(text)
    return res
#联合查询社团信息与社团帖子信息与社团活动信息
@app.route('/communityinfo_post_activity',methods=['POST'])
def communityinfocommunitypostcommunityactivity():
    text = request.form
    res=communityinfo_communitypost_communityactivity(text)
    return res

#指定user_id查询帖子
@app.route('/search_community_post_by_user_id',methods=['POST'])
def searchcommunitypostbyuserid():
    text = request.form
    res=search_community_post_by_user_id(text)
    return res

#指定user_id查询社团成员
@app.route('/search_community_member_by_user_id',methods=['POST'])
def searchcommunitymemberbyuserid():
    text = request.form
    res=search_community_member_by_user_id(text)
    return res

#指定user_id查询我管理的社团
@app.route('/search_community_leader_by_user_id',methods=['POST'])
def searchcommunityactivitybyuserid():
    text = request.form
    res=search_community_leader_by_user_id(text)
    return res

#增加社团活动审核
@app.route('/add_community_activity_check',methods=['POST'])
def addcommunityactivitycheck():
    text = request.form
    res=add_community_activity_check(text)
    return res

#删除社团活动审核
@app.route('/delete_community_activity_check',methods=['POST'])
def deletecommunityactivitycheck():
    text = request.form
    res=delete_community_activity_check(text)
    return res

#查询社团活动审核
@app.route('/search_community_activity_check',methods=['POST'])
def searchcommunityactivitycheck():
    text = request.form
    res=search_community_activity_check(text)
    return res

#更新社团活动审核
@app.route('/update_community_activity_check',methods=['POST'])
def updatecommunityactivitycheck():
    text = request.form
    res=update_community_activity_check(text)
    return res

#增加社团活动成员
@app.route('/add_community_activity_member',methods=['POST'])
def addcommunityactivitymember():
    text = request.form
    res=add_community_activity_member(text)
    return res

#删除社团活动成员
@app.route('/delete_community_activity_member',methods=['POST'])
def deletecommunityactivitymember():
    text = request.form
    res=delete_community_activity_member(text)
    return res

#审核社团活动成员
@app.route('/search_community_activity_member',methods=['POST'])
def searchcommunityactivitymember():
    text = request.form
    res=search_community_activity_member(text)
    return res

#查询社团活动成员
@app.route('/search_community_activity_memberlist',methods=['POST'])
def searchcommunityactivitymemberlist():
    text = request.form
    res=search_community_activity_memberlist(text)
    return res


#更新社团活动成员
@app.route('/update_community_activity_member',methods=['POST'])
def updatecommunityactivitymember():
    text = request.form
    res=update_community_activity_member(text)
    return res

#按用户id查询社团活动成员
@app.route('/search_activity_member_by_user_id',methods=['POST'])
def searchactivitymemberbyuserid():
    text = request.form
    res=search_community_activity_member_by_user_id(text)
    return res

#增加管理员
@app.route('/add_admin',methods=['POST'])
def addadmin():
    text = request.form
    res=add_admin(text)
    return res

#删除管理员
@app.route('/delete_admin',methods=['POST'])
def deleteadmin():
    text = request.form
    res=delete_admin(text)
    return res

#查询管理员
@app.route('/search_admin',methods=['POST'])
def searchadmin():
    text = request.form
    res=search_admin(text)
    return res

#更新管理员
@app.route('/update_admin',methods=['POST'])
def updateadmin():
    text = request.form
    res=update_admin(text)
    return res

#增加社团信息审核
@app.route('/add_community_info_check',methods=['POST'])
def addcommunityinfocheck():
    text = request.form
    res=add_community_info_check(text)
    return res

#删除社团信息审核
@app.route('/delete_community_info_check',methods=['POST'])
def deletecommunityinfocheck():
    text = request.form
    res=delete_community_info_check(text)
    return res

#查询社团信息审核
@app.route('/search_community_info_check',methods=['POST'])
def searchcommunityinfocheck():
    text = request.form
    res=search_community_info_check(text)
    return res

#更新社团信息审核
@app.route('/update_community_info_check',methods=['POST'])
def updatecommunityinfocheck():
    text = request.form
    res=update_community_info_check(text)
    return res

#增加社团成员审核
@app.route('/add_community_member_check',methods=['POST'])
def addcommunitymembercheck():
    text = request.form
    res=add_community_member_check(text)
    return res

#删除社团成员审核
@app.route('/delete_community_member_check',methods=['POST'])
def deletecommunitymembercheck():
    text = request.form
    res=delete_community_member_check(text)
    return res

#查询社团成员审核
@app.route('/search_community_member_check',methods=['POST'])
def searchcommunitymembercheck():
    text = request.form
    res=search_community_member_check(text)
    return res

#更新社团成员审核
@app.route('/update_community_member_check',methods=['POST'])
def updatecommunitymembercheck():
    text = request.form
    res=update_community_member_check(text)
    return res

#增加社团帖子审核
@app.route('/add_community_post_check',methods=['POST'])
def addcommunitypostcheck():
    text = request.form
    res=add_community_post_check(text)
    return res

#删除社团帖子审核
@app.route('/delete_community_post_check',methods=['POST'])
def deletecommunitypostcheck():
    text = request.form
    res=delete_community_post_check(text)
    return res

#查询社团帖子审核
@app.route('/search_community_post_check',methods=['POST'])
def searchcommunitypostcheck():
    text = request.form
    res=search_community_post_check(text)
    return res

#更新社团帖子审核
@app.route('/update_community_post_check',methods=['POST'])
def updatecommunitypostcheck():
    text = request.form
    res=update_community_post_check(text)
    return res

#增加用户收藏
@app.route('/add_user_collect',methods=['POST'])
def addusercollect():
    text = request.form
    res=add_user_collect(text)
    return res

#删除用户收藏
@app.route('/delete_user_collect',methods=['POST'])
def deleteusercollect():
    text = request.form
    res=delete_user_collect(text)
    return res

#查询用户收藏
@app.route('/user_collect_post',methods=['POST'])
def usercollectpost():
    text = request.form
    res=user_collect_post(text)
    return res

#增加用户喜欢
@app.route('/add_user_like',methods=['POST'])
def adduserlike():
    text = request.form
    res=add_user_like(text)
    return res

#删除用户喜欢
@app.route('/delete_user_like',methods=['POST'])
def deleteuserlike():
    text = request.form
    res=delete_user_like(text)
    return res

#查询用户喜欢
@app.route('/user_like_post',methods=['POST'])
def userlikepost():
    text = request.form
    res=user_like_post(text)
    return res

#查询被喜欢的用户
@app.route('/like_user_post',methods=['POST'])
def likeuserpost():
    text = request.form
    res=like_user_post(text)
    return res

#查询被收藏的用户
@app.route('/collect_user_post',methods=['POST'])
def collectuserpost():
    text = request.form
    res=collect_user_post(text)
    return res

#查询被评论的用户
@app.route('/comment_user_post',methods=['POST'])
def commentuserpost():
    text = request.form
    res=comment_user_post(text)
    return res

#插入一条轮播图
@app.route('/insertCarousel',methods=['POST'])
def insertcarousel():
    text = request.form
    res=insertCarousel(text)
    return res

#删除一条轮播图
@app.route('/deleteCarousel',methods=['POST'])
def deletecarousel():
    text = request.form
    res=deleteCarousel(text)
    return res

#查询轮播图
@app.route('/searchCarousel',methods=['POST'])
def searchcarousel():
    text = request.form
    res=searchCarousel(text)
    return res


#获取所有管理员和用户
@app.route('/get_all_admin_and_user',methods=['POST'])
def alladminanduser():
    res=get_all_admin_and_user()
    return res

if __name__ == '__main__':
    app.run(debug=True)