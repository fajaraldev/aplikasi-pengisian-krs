import hashlib
from config.db import DBConnection as mydb

userInfo=[]

class Users:
    def __init__(self):

        self.__user_id=None
        self.__username=None
        self.__password=None
        self.__role_name=None
        self.__info =None
        self.__loginvalid=None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def user_id(self):
        return self.__user_id

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def role_name(self):
        return self.__role_name

    @role_name.setter
    def role_name(self, value):
        self.__role_name = value

    @property
    def loginvalid(self):
        return self.__loginvalid

    @loginvalid.setter
    def loginvalid(self, value):
        self.__loginvalid = value

    def setUserInfo(self,loginvalid,username,rolename):
        val=(loginvalid,username,rolename)
        for x in val:
          userInfo.append(x)

    def validate(self, username, password):
        # a=str(username)
        # b=a.strip()
        # pwd=str(password).strip().encode()
        # c = hashlib.md5(pwd)
        # c2=c.hexdigest()

        a=str(username)
        b=a.strip()
        c=str(password)
        d=c.strip()

        self.conn = mydb()
        sql="SELECT u.username,r.role_name FROM users AS u, roles AS r WHERE u.username='" + b + "' AND u.password='" + d + "' AND u.role_id=r.role_id"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__username = self.result[0]
            self.__role_name = self.result[1]
            self.affected = self.conn.cursor.rowcount
            self.__loginvalid = True
        else:
            self.__username = ''
            self.__password = ''
            self.__role_name = ''
            self.affected = 0
            self.__loginvalid = False
        self.conn.disconnect

        self.setUserInfo(self.__loginvalid,self.__username,self.__role_name)
