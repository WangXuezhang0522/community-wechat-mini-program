from ..communityDB import db,Carousel
from flask import request
import base64
from PIL import Image
from io import BytesIO

#Carousel表操作


#插入一条轮播图
def insertCarousel(text):

    try:
        image_data = request.files.get('image')
        if image_data:
            img = Image.open(image_data)
            img.thumbnail((600, 600))  # 设置图像的最大尺寸为300x300像素
            output = BytesIO()
            img.save(output, format='JPEG', quality=50)  # 通过quality参数控制图像质量
            image_bytes = output.getvalue()
        else:
            image_bytes = None
        if image_bytes:
            data = Carousel(
                image = image_bytes,
                type = text['type'],
            )
        else:
            return {'message':'图片不能为空'}
        db.session.add(data)
        db.session.commit()
        db.session.close()
        return {'message':'插入成功'}
    except Exception as e :
        #抛出错误信息
        print(e)
        db.session.rollback()
        db.session.close()
        return {'message':f'插入失败:{e}'}
#删除一条轮播图
def deleteCarousel(text):
    data = Carousel.query.filter_by(id=text['id']).first()
    try:
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        return 'success'
    except Exception as e:
        db.session.rollback()
        db.session.close()
        return f'error:{e}'
    
#查询轮播图
def searchCarousel(text):
    data = Carousel.query.all()
    list = []
    for i in data:
        if i.image == None:
            image = None
        else:
            image = base64.b64encode(i.image).decode('utf-8')
        list.append({
            'id':i.id,
            'image':image,
            'type':i.type
        })
    return list


