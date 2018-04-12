# -*- coding: utf-8 -*-
import MySQLdb


class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn

    def check_account_available(self, id):
        cursor = conn.cursor()
        try:
            sql = "select * from bank where account=%s" % id
            print "check_account_available:" + sql
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("帐号%s不存在" % id)
        finally:
            cursor.close()

    def has_enough_money(self, id, money):
        cursor = conn.cursor()
        try:
            sql = "select * from bank where account=%s and money>=%s" % (id, money)
            print "has_enough_money:" + sql
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("帐号%s金额不足%s" % (id, money))
        finally:
            cursor.close()

    def reduce_money(self, id, money):
        cursor = conn.cursor()
        try:
            sql = "update bank set money=money-%s where account=%s" % (money, id)
            print "reduce_money:" + sql
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("帐号%s扣款%s失败" % (id, money))
        finally:
            cursor.close()

    def add_money(self, id, money):
        cursor = conn.cursor()
        try:
            sql = "update bank set money=money+%s where account=%s" % (money, id)
            print "add_money:" + sql
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("帐号%s收款%s失败" % (id, money))
        finally:
            cursor.close()

    def transfer(self, source_id, target_id, money):
        try:
            self.check_account_available(source_id)
            self.check_account_available(target_id)
            self.has_enough_money(source_id, money)
            self.reduce_money(source_id, money)
            self.add_money(target_id, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e


if __name__ == "__main__":
    source_id = 3
    target_id = 7
    money = 100

    conn = MySQLdb.Connection(  # 创建连接
        host='127.0.0.1',  #
        port=3306,  # 端口
        user='root',  # 用户
        passwd='123456',  # 密码
        db='studyPy',  # 数据库
        charset='utf8'  # 编码
    )
    tr_money = TransferMoney(conn)

    try:
        tr_money.transfer(source_id, target_id, money)
        print "From账户:%s\nTo账户:%s\n转账:%s\n成功!!!" % (source_id, target_id, money)
    except Exception as e:
        print "转账失败：" + str(e)
    finally:
        conn.close()
