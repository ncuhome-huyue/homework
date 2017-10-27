import sqlite3


class sql:
	def __init__(self,dir):
		self.cx = sqlite3.connect(dir)
		self.cu = self.cx.cursor()

	def createtable(self,tablename,values):
		self.cu.execute(r'create table ' + tablename + '(' +values +');')

	def settable(self,tablename):
		self.tablename=tablename

	def select(self,values,b,a):
		self.cu.execute(r'select ' + values + r' from ' + self.tablename+'where'+ b +"="+ a + ';')
		print(self.cu.fetchall())

	def insert(self,key,value):
		self.cu.execute(r'insert into ' + self.tablename + '(' + key + ')'+r' values '+'(' + value + ');')
		self.cx.commit()

	def delete(self,key,value):
		self.cu.execute(r'delete from ' + self.tablename +r' where '+key+'='+ value+';')
		self.cx.commit()
