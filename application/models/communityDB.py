#models文件下的数据表映射对象
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from datetime import datetime
db = SQLAlchemy()

class User(db.Model):#用户表
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80),unique=True, nullable=False)
    password = db.Column(db.String(120),nullable=False)
    truename = db.Column(db.String(80),nullable=False)
    sex = db.Column(db.String(10),default='外星人')
    tel = db.Column(db.String(120), unique=True)
    role = db.Column(db.String(80),default='游客')
    avatar = db.Column(db.LargeBinary,nullable=True)

    def __repr__(self):
        return '<User id=%r, username=%r>' % (self.id, self.username)
    
class CommunityInfo(db.Model):#社团信息表
    __tablename__ = 'community_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True)#社团名称
    description = db.Column(db.String(300))#社团描述
    #社团人数
    number = db.Column(db.Integer)
    #社团类型
    type = db.Column(db.String(80))
    #社团负责人userid,级联删除
    leader_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'),unique=True)
    #社团负责人名称
    leader_name = db.Column(db.String(80))
    image = db.Column(db.LargeBinary,nullable=True)
    def __repr__(self):
        return '<CommunityInfo id=%r, name=%r>' % (self.id, self.name)

class CommunityMember(db.Model):#社团成员表
    __tablename__ = 'community_member'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #社团id
    community_id = db.Column(db.Integer, db.ForeignKey('community_info.id', ondelete='CASCADE'),nullable=False)
    #社团名称
    community_name = db.Column(db.String(80))
    #成员id
    member_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'),unique=False)
    #用户名
    member_name = db.Column(db.String(80))
    #成员角色
    role = db.Column(db.String(80))
    def __repr__(self):
        return '<CommunityMember id=%r, community_id=%r, member_id=%r>' % (self.id, self.community_id, self.member_id)
    
class CommunityActivity(db.Model):#社团活动表
    __tablename__ = 'community_activity'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #社团id
    community_id = db.Column(db.Integer, db.ForeignKey('community_info.id', ondelete='CASCADE'),nullable=False)
    #社团名称
    community_name = db.Column(db.String(80))
    #负责人id
    leader_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    #负责人名称
    leader_name = db.Column(db.String(80))
    #活动名称
    name = db.Column(db.String(80))
    #活动地点
    address = db.Column(db.String(80))
    #参与人数
    number = db.Column(db.Integer)
    #活动经费
    cost = db.Column(db.Float)
    #活动内容
    content = db.Column(db.String(300))
    #开始时间
    start_time = db.Column(db.DateTime, default=datetime.now())
    #结束时间
    end_time = db.Column(db.DateTime,nullable=False)
    #图片
    image = db.Column(db.LargeBinary,nullable=True)
    def __repr__(self):
        return '<CommunityActivity id=%r, community_id=%r, name=%r>' % (self.id, self.community_id, self.name)

#社团活动参与表
class CommunityActivityMember(db.Model):
    __tablename__ = 'community_activity_member'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #社团id
    community_id = db.Column(db.Integer, db.ForeignKey('community_info.id', ondelete='CASCADE'),nullable=False)
    #活动id
    activity_id = db.Column(db.Integer, db.ForeignKey('community_activity.id', ondelete='CASCADE'),nullable=False)
    #用户id
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'),nullable=False)
    #用户名
    username = db.Column(db.String(80))
    def __repr__(self):
        return '<CommunityActivityMember id=%r, community_id=%r, activity_id=%r>' % (self.id, self.community_id, self.activity_id)

#交流贴表
class CommunityPost(db.Model):
    __tablename__ = 'community_post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #社团id
    community_id = db.Column(db.Integer, db.ForeignKey('community_info.id', ondelete='CASCADE'),nullable=False,
                             default=1)
    #用户id
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'),nullable=False)
    #用户名
    username = db.Column(db.String(80))
    #标题
    title = db.Column(db.String(120))
    #内容
    content = db.Column(db.String(300))
    #时间
    time = db.Column(db.DateTime, default=datetime.now())
    #点赞数
    like = db.Column(db.Integer, default=0)
    #图片
    image = db.Column(db.LargeBinary,nullable=True)
    #类型
    type = db.Column(db.String(80))
    #成员类型
    role = db.Column(db.String(80))
    def __repr__(self):
        return '<CommunityPost id=%r, community_id=%r>' % (self.id, self.community_id)
    
class comment(db.Model):
    #评论id | 交流贴id | 用户id | 内容 | 时间
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #交流贴id
    post_id = db.Column(db.Integer, db.ForeignKey('community_post.id', ondelete='CASCADE'),nullable=False)
    #用户id
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'),nullable=False)
    #用户名
    username = db.Column(db.String(80))
    #内容
    content = db.Column(db.String(120))
    #点赞
    like = db.Column(db.Integer, default=0)
    #时间
    time = db.Column(db.DateTime, default=datetime.now())
    def __repr__(self):
        return '<comment id=%r, post_id=%r>' % (self.id, self.post_id)


#个人喜欢的交流贴
class UserLike(db.Model):
    __tablename__ = 'user_like'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #交流贴id
    post_id = db.Column(db.Integer, db.ForeignKey('community_post.id', ondelete='CASCADE'),nullable=False,unique=True)
    #用户id
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'),nullable=False)
    def __repr__(self):
        return '<like id=%r, post_id=%r>' % (self.id, self.post_id)

#个人收藏的交流贴
class UserCollect(db.Model):
    __tablename__ = 'user_collect'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #交流贴id
    post_id = db.Column(db.Integer, db.ForeignKey('community_post.id', ondelete='CASCADE'),nullable=False,unique=True)
    #用户id
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'),nullable=False)
    def __repr__(self):
        return '<collect id=%r, post_id=%r>' % (self.id, self.post_id)
    
#管理员表
class Admin(db.Model):
    __tablename__ = 'admin'
    #管理员id | 用户名 | 密码 | 审核码 |status
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80),unique=True, nullable=False)
    password = db.Column(db.String(120),nullable=False)
    auditCode = db.Column(db.String(80),nullable=False)
    status = db.Column(db.String(80),default='正常')

    def __repr__(self):
        return '<Admin id=%r, username=%r>' % (self.id, self.username)
    
#社团信息审核表
class CommunityInfoCheck(db.Model):
    __tablename__ = 'community_info_check'
    #社团id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #社团名称
    name = db.Column(db.String(80), unique=True)
    #社团描述
    description = db.Column(db.String(300))
    #社团人数
    number = db.Column(db.Integer)
    #社团类型
    type = db.Column(db.String(80))
    #社团负责人userid,级联删除
    leader_id = db.Column(db.Integer, db.ForeignKey('users.id'),unique=True)
    #社团负责人名称
    leader_name = db.Column(db.String(80))
    #社团图片
    image = db.Column(db.LargeBinary,nullable=True)
    #审核状态
    status = db.Column(db.String(80))
    #审核时间
    check_time = db.Column(db.DateTime, default=datetime.now())
    def __repr__(self):
        return '<CommunityInfoCheck id=%r, community_id=%r>' % (self.id, self.community_id)
    
#社团活动审核表
class CommunityActivityCheck(db.Model):
    __tablename__ = 'community_Activity_check'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #社团id
    community_id = db.Column(db.Integer, db.ForeignKey('community_info.id', ondelete='CASCADE'),nullable=False)
    #社团名称
    community_name = db.Column(db.String(80))
    #负责人id
    leader_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    #负责人名称
    leader_name = db.Column(db.String(80))
    #活动名称
    name = db.Column(db.String(80))
    #活动地点
    address = db.Column(db.String(80))
    #参与人数
    number = db.Column(db.Integer)
    #活动经费
    cost = db.Column(db.Float)
    #活动内容
    content = db.Column(db.String(300))
    #开始时间
    start_time = db.Column(db.DateTime, default=datetime.now())
    #结束时间
    end_time = db.Column(db.DateTime,nullable=False)
    #图片
    image = db.Column(db.LargeBinary,nullable=True)
    #审核状态
    status = db.Column(db.String(80))
    #审核时间
    check_time = db.Column(db.DateTime, default=datetime.now())
    def __repr__(self):
        return '<CommunityActivityCheck id=%r, community_id=%r, name=%r>' % (self.id, self.community_id, self.name)
    
    #社团成员审核表
class CommunityMemberCheck(db.Model):
    __tablename__ = 'community_member_check'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #社团id
    community_id = db.Column(db.Integer, db.ForeignKey('community_info.id', ondelete='CASCADE'),nullable=False)
    #社团名称
    community_name = db.Column(db.String(80))
    #成员id
    member_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'),unique=True)
    #用户名
    member_name = db.Column(db.String(80))
    #成员角色
    role = db.Column(db.String(80))
    #审核状态
    status = db.Column(db.String(80))
    #审核时间
    check_time = db.Column(db.DateTime, default=datetime.now())
    def __repr__(self):
        return '<CommunityMemberCheck id=%r, community_id=%r, member_id=%r>' % (self.id, self.community_id, self.member_id)
    
#社团交流贴审核表
class CommunityPostCheck(db.Model):
    __tablename__ = 'community_post_check'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #社团id
    community_id = db.Column(db.Integer, db.ForeignKey('community_info.id', ondelete='CASCADE'),nullable=False)
    #用户id
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'),nullable=False)
    #用户名
    username = db.Column(db.String(80))
    #标题
    title = db.Column(db.String(120))
    #内容
    content = db.Column(db.String(300))
    #时间
    time = db.Column(db.DateTime, default=datetime.now())
    #点赞数
    like = db.Column(db.Integer, default=0)
    #图片
    image = db.Column(db.LargeBinary,nullable=True)
    #类型
    type = db.Column(db.String(80))
    #成员类型
    role = db.Column(db.String(80))
    #审核状态
    status = db.Column(db.String(80))
    #审核时间
    check_time = db.Column(db.DateTime, default=datetime.now())
    def __repr__(self):
        return '<CommunityPostCheck id=%r, community_id=%r>' % (self.id, self.community_id)
    
    #轮播图表 id | 图片 |类型 |
class Carousel(db.Model):
    __tablename__ = 'carousel'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #图片
    image = db.Column(db.LargeBinary,nullable=False)
    #类型
    type = db.Column(db.String(80))
    def __repr__(self):
        return '<Carousel id=%r>' % (self.id)

#创建数据库


def create_db():
    from app import app

    with app.app_context():
        meta = MetaData()
        meta.reflect(bind=db.engine)

        existing_tables = meta.tables.keys()

        if not existing_tables:
            db.create_all()
            return '初始化成功'
        else:
            return '已初始化'


