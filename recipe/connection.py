import pymysql
from flask import jsonify

class conn:

    def __init__(self):
        self.con = pymysql.connect(host="localhost", user="root", password="password", db="recipe", port=3306)
        self.cu = self.con.cursor()


    def nonreturn(self,a):
        self.cu.execute(a)
        id=self.cu.lastrowid
        self.con.commit()
        return id

    def mid(self,a):
        self.cu.execute(a)
        f=self.cu.fetchone()
        if f[0] is None:
            id=1
        else:
            id=f[0] + 1
        return (id)

    def selectone(self,a):
        self.cu.execute(a)
        self.res = self.cu.fetchone()
        return (self.res)

    def selectall(self,a):
        self.cu.execute(a)
        self.res=self.cu.fetchall()
        return(self.res)

    def jsonselectall(self, a):
        self.cu.execute(a)

        v = self.cu.fetchall()
        row_headers = [x[0] for x in self.cu.description]
        json_data = []
        for result in v:
            json_data.append(dict(zip(row_headers, result)))

        return json_data

