# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# 这一部分用来创建连接，连接数据库
def dbHandle():
    conn = pymysql.connect(
    host = "127.0.0.1",
    user = "root",
    passwd = "",
    charset = "utf8",
    use_unicode = False
    )
    return conn
# 这一部分用来向数据库传入数据
class DoubanPipeline(object):
    def process_item(self,item,spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        # 定义cursor后，可以类似与在cmd中一样操作数据库
        cursor.execute("USE doubancomics")
        sql = "INSERT INTO comics (title,link,info,abst) VALUES(%s,%s,%s,%s)"
        try:
            cursor.execute(sql,(item['title'],item['link'],item['info'],item['desc']))
            cursor.connection.commit()
        except BaseException as e:
            print("错误在这里>>>>>>>>>>>>>",e,"<<<<<<<<<<<<<错误在这里")
            dbObject.rollback()
        return item

    