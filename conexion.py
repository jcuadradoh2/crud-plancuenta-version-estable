import sys
import pymysql

class conexion:
    def __init__(self,host='localhost',user='root',password='',database='bdcuentas'):
        self.__host=host
        self.__user=user
        self.__password=password
        self.__database=database
        self.__conn=''
        self.__conector=''

    def conectabd(self):
        try:
            self.__conn=pymysql.connect(host=self.__host,user=self.__user,
            password=self.__password,database=self.__database)
            self.__conector=self.__conn.cursor()
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print('error en la conexion: {}'.format(e))
            sys.exit(1)

    def close(self):
        self.__conn.close()
        self.__conector.close()

    @property
    def conn(self):
        return self.__conn
    @property
    def conector(self):
        return self.__conector
