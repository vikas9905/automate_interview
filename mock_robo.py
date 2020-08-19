import random
import time

def read_file(path):
	try:
		data=open(path,'r')
	except FileNotFoundError as msg:
		print(msg)

	q={}
	ans={}
	num=0
	while True:
	    t=data.readline()
	    flag=1
	    if len(t)==0:
	        break
	    #print(t)
	    if t[0].isdigit() or t[:2].isdigit():
	        num1=int(t[:2]) if t[:2].isdigit() else int(t[0])
	        if num>num1:
	            continue
	        else:
	            num=num1
	        if q.get(num,0)==0:
	            q[num]=t
	        #print(num)
	    else:
	        if ans.get(num,0)!=0 and flag==1:
	            ans[num]+=t
	        else:
	            ans[num]=t
	data.close()
	return q,ans
def prepare_question(path):
	try:
		data=open(path,'r',encoding='utf-8')
	except FileNotFoundError as msg:
		print(msg)

	q={}
	ans={}
	num=0
	while True:
	    t=data.readline()
	    flag=1
	    if len(t)==0:
	        break
	    #print(t)
	    if t[0].isdigit() or t[:2].isdigit():
	        num1=int(t[:2]) if t[:2].isdigit() else int(t[0])
	        if num>num1:
	            continue
	        else:
	            num=num1
	        if q.get(num,0)==0:
	            q[num]=t
	        #print(num)
	    else:
	        if ans.get(num,0)!=0 and flag==1:
	            ans[num]+=t
	        else:
	            ans[num]=t
	data.close()
	return q,ans

def AWS_mock():
	path='papers\\AWS.txt'
	q,ans=prepare_question(path)
	n=int(input("Enter Number of question you want to ask"))
	for i in range(n):
		ind=random.randrange(len(q))
		print(q[ind])
		print("------------------------------------------------------------------------------------------------")
		time.sleep(5)
		print(ans[ind])
		print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
		s=''
		while(s!='m'):
			s=input("Enter m to Move Forward\n")

def cn_mock():
	path='papers\\test.txt'
	q,ans=prepare_question(path)
	n=int(input("Enter Number of question you want to ask"))
	for i in range(n):
		ind=random.randrange(len(q))
		print(q[ind])
		print("------------------------------------------------------------------------------------------------")
		time.sleep(5)
		print(ans[ind])
		print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
		s=''
		while(s!='m'):
			s=input("Enter m to Move Forward\n")

def DOCKER_mock():
	path='papers\\docker2.txt'
	q,ans=prepare_question(path)
	n=int(input("Enter Number of question you want to ask"))
	for i in range(n):
		ind=random.randrange(len(q))
		print(q[ind])
		print("------------------------------------------------------------------------------------------------")
		time.sleep(5)
		print(ans[ind])
		print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
		s=''
		while(s!='m'):
			s=input("Enter m to Move Forward\n")

def datascience_mock():
	path='papers\\datascience.txt'
	q,ans=prepare_question(path)
	n=int(input("Enter Number of question you want to ask"))
	for i in range(n):
		ind=random.randrange(len(q))
		print(q[ind])
		print("------------------------------------------------------------------------------------------------")
		time.sleep(5)
		print(ans[ind])
		print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
		s=''
		while(s!='m'):
			s=input("Enter m to Move Forward\n")

def AI_mock():
	path='papers\\AI.txt'
	q,ans=prepare_question(path)
	n=int(input("Enter Number of question you want to ask"))
	for i in range(n):
		ind=random.randrange(len(q))
		print(q[ind])
		print("------------------------------------------------------------------------------------------------")
		time.sleep(5)
		print(ans[ind])
		print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
		s=''
		while(s!='m'):
			s=input("Enter m to Move Forward\n")

def hr():
	path='papers\\hr.txt'
	q,ans=read_file(path)
	print(len(q),len(ans))
	n=int(input("Enter Number of question you want to ask"))
	for i in range(n):
		ind=random.randrange(len(q))
		print(q[ind])
		print("------------------------------------------------------------------------------------------------")
		time.sleep(5)
		print(ans[ind])
		print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
		s=''
		while(s!='m'):
			s=input("Enter m to Move Forward\n")


def main():
	print("1.DOCKER\t                2.AMAZON WEB SERVICES\n")
	print("3.Computer Network\t        4.Data Science\n")
	print("5.Artificial Intelligence\t 6.HR\n")
	while(1):
		print("Enter 0 to Exit")
		n=int(input("enter your choice\n"))
		if n==3:
			cn_mock()
		elif n==2:
			AWS_mock()
		elif n==1:
			DOCKER_mock()
		elif n==4:
			datascience_mock()
		elif n==5:
			AI_mock()
		elif n==6:
			hr()
		else:
			break
main()



