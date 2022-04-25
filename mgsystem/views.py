from re import L
from tkinter.tix import Tree
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
from .models import Mgdata,Report,Contactus
from django.db.models import Q 

# Create your views here.

def index(request):
	return render(request,'index.html')


def adddata(request):
	user = request.user
	
	if user.is_authenticated:
		if request.method == "POST":
			
			fname = request.POST.get('fname')
			lname = request.POST.get('lname')
			father = request.POST.get('father')
			phone = request.POST.get('phone')
			email = request.POST.get('email')
			section = request.POST.get('section')
			stuclass = request.POST.get('stuclass')
			img = request.FILES['img']
			print(fname,lname,father,phone,email,img)
			if user !=  None:
				
				data=Mgdata(fname=fname,lname=lname,father=father,phone=phone,user=user,stuclass=stuclass,section=section,email=email,img=img)
				data.save()
				
				messages.success(request,'Data Is Saved')
				
			else:	
				messages.error(request,'Data Is not Saved')
				# return render(request,'adddata.html')

		return render(request,'adddata.html')

	else:
		return redirect('index')	

def signup(request):
	

	user=request.user
	if user.is_authenticated:
		return redirect('index')
	else:	
		if request.method == "POST":
			fname = request.POST.get('fname')
			lname = request.POST.get('lname')
			uname = request.POST.get('uname')
			phone = request.POST.get('phone')
			email = request.POST.get('email')
			pass1 = request.POST.get('pass1')
			pass2 = request.POST.get('pass2')
			# print(fname,lname,uname,phone,email,pass1,pass2)
			if pass1 != pass2 :
				messages.error(request,"Passwords Is Diffrent")
				return render(request,'signup.html')
		

			user = 	User.objects.create_user(uname,email,pass1)
			user.first_name = fname
			user.last_name = lname

			user.save()
			messages.success(request,"Your Account Is Created")
		# # login(request,user)


	return render(request,'signup.html')


def userlogin(request):
	user=request.user
	if user.is_authenticated:
		return redirect("index")
	# datasno = request.POST.get('datasno')
	# print(datasno)
	else:
		if request.method == "POST":
			uname=request.POST.get('uname')
			password=request.POST.get('password')
			user=authenticate(username= uname, password=password)
			print(uname,password)
			if user is not None:
				login(request, user)
				messages.success(request, "Successfully Logged In")
				dic={'user':request.user}
				return render(request,'index.html',dic)

			else:
				messages.error(request, "Invalid credentials! Please try again")
				# return redirect("home")

		return render(request,'login.html')
	

def userlogout(request):
	user=request.user
	if user.is_authenticated:
		logout(request)
		messages.success(request, "Successfully logged out")
		return render(request,"index.html")
	else:	
		return redirect('index')


def datalist(request):
	user=request.user
	if user.is_authenticated:
		if request.method == "GET":
			
			s = request.GET.get('search')
			
			
			if s:
				search = s.strip()
				data = Mgdata.objects.filter(Q(fname__icontains=search) | Q(lname__icontains=search))
				dic={'data':data}	
			
				return render(request,'datalist.html',dic)

			# else:
			# 	# If not searched, return default posts
			# 	messages.warning(request,"Fill Correct Search Field And Search Data")
			# 	print("dd")
				

		
	
		data=Mgdata.objects.filter(user=user).exclude(isdelete=True).order_by('-stuclass')
		
		dic={'data':data}	

		return render(request,'datalist.html',dic)
	else:
		return redirect('index')	



def student(request,sno):
	user=request.user
	if user.is_authenticated:
	
		data=Mgdata.objects.filter(user=user,sno=sno).exclude(isdelete=True)
		
		dic={'data':data}	

		return render(request,'data.html',dic)
	else:
		return redirect('index')	





def isdelete(request,sno):
	data = Mgdata.objects.get(sno=sno)
	data.isdelete = True
	data.save()
	sno=sno
	return redirect('datalist')


def report(request):
	# name = user.first_name
	if request.method == "POST":
		user = request.user
		if user.is_authenticated:
			name = user.username
			rep= request.POST.get("report")
			print(name)
			print(rep)
			report = Report(name=name,rep=rep)
			report.save()
			messages.success(request,'Your Report Is Send Thanks For Reporting')

		else:
			name= request.POST.get("name")
			rep= request.POST.get("report")
			report = Report(name=name,rep=rep)
			print("dosra",name,rep)

			report.save()
			messages.success(request,'Your Report Is Send Thanks For Reporting')
	return render(request,'report.html')

def contactus(request):
	if request.method == "POST":
		user = request.user
		if user.is_authenticated:
			name = user.username
			email = user.email
			desc= request.POST.get("desc")
			print(name)
			print(email)
			print(desc)
			contact = Contactus(name=name,email=email,desc=desc)
			contact.save()
			messages.success(request,'Your Message Is Send Thanks For Contact Us')

		else:
			name= request.POST.get("name")
			email= request.POST.get("email")
			desc= request.POST.get("desc")
		
			print("dosra",name,email,desc)

			contact = Contactus(name=name,email=email,desc=desc)
			contact.save()
			messages.success(request,'Your Message Is Send Thanks For Contact Us')
	return render(request,'contactus.html')

def about(request):
	return render(request,'about.html')




def editinfo(request):
	user = request.user
	
	if user.is_authenticated:
		if request.method == "POST":
			sno = request.POST.get("sno")
			fname = request.POST.get('fname')
			lname = request.POST.get('lname')
			father = request.POST.get('father')
			phone = request.POST.get('phone')
			email = request.POST.get('email')
			section = request.POST.get('section')
			stuclass = request.POST.get('stuclass')
			# img = request.FILES['img']
			

			# if img == "":
			Mgdata.objects.filter(sno = sno,user=user).update(fname=fname,lname=lname,father=father,phone=phone,user=user,stuclass=stuclass,section=section,email=email)
			# Mgdata.save(request)
			print("232dewd3d")
			# else:
			# 	data = Mgdata.objects.filter(id = sno).update(fname=fname,img=img,lname=lname,father=father,phone=phone,user=user,stuclass=stuclass,section=section,email=email)
			# 	data.save()

			messages.success(request,'Data Is Update')
			return redirect('student/'+sno)

				
		else:	
			messages.error(request,'Data Is not Saved')
			# return render(request,'adddata.html')

			return render(request,'data.html')

	else:
		return redirect('index')	