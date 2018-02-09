'''
Created on 2018-02-07
@author: mk
class db_mongoimg
'''

import os
from pymongo.database import Database
import time
import gridfs

class mongoImg(object):
    def __init__(self, database, dir):
        if not isinstance(database, Database):
            raise TypeError("database must be an instance of Database")
        if len(dir) < 1:
            raise TypeError("dir must be an string of directory")

        self.__imgdb = database
        self.__imgfs = gridfs.GridFS(self.__imgdb)
        self.__dir = dir
        self.__filelist = []

    def __dirwalk(self, topdown=True):
        sum=0
        self.__filelist.clear()

        for root,dirs,files in os.walk(self.__dir,topdown):
            for name in files:
                sum+=1
                temp=os.path.join(root,name)
                self.__filelist.append(temp)
        print(sum)

    def insert(self):
        self.__dirwalk()
        tStart = time.time()
        for fi in self.__filelist:
            with open(fi,'rb') as myimage:
                data = myimage
                print("putting "+os.path.basename(fi)+" ...")
                self.__imgfs.put(data,content_type="png",filename=os.path.basename(fi))

        tEnd=time.time()
        print("It cost %f sec" % (tEnd - tStart))

    def getbyname(self,filename,savepath):
        if len(savepath) < 1:
            raise TypeError("dir must be an string of directory")
        dataout=self.__imgfs.get_version(filename)
        try:
            imgout=open(savepath,'wb')
            data=dataout.read()
            imgout.write(data)
        finally:
            imgout.close()

    def list(self):
        return self.__imgfs.list()

    def deleteAll(self):
        for td in self.__imgfs.find():
            self.__imgfs.delete(td._id)

