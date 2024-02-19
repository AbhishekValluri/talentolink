from django.shortcuts import render,redirect
from . models import contact,profile,PostJobs,employee


# importing the users from default models
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout 

# import authentication messages from default configrations
from django.contrib import messages


# Create your views here.
# views- creating with functions--functional based views
def Home(request):
    return render(request,'index.html') # render is used for dynamic displaying of the content.

def About(request):
    return render(request,'About.html')

def Service(request):
    return render(request,'sevices.html')

def Contact(request):
    if(request.method=='POST'):
        #Cname =variable name,cname=name_attribute value
        Cname=request.POST['cname']
        Cemail=request.POST['cemail']
        Cmobile=request.POST['cmobile']
        Cmessage=request.POST['cmessage']

        # creating the row/records in the table:Contact
        # objects.create method to create the store the data in table :Contact .
        # object.all() method to reterive the data from table: Contact 
        # record=Contact.objects.create(column_name of table=variable_name)
        record=contact.objects.create(name=Cname,email=Cemail,mobile=Cmobile,description=Cmessage)
        
        # saving the data to database
        record.save()
    else:
        return render(request,'contact us.html')
    
    return render(request,'contact us.html')
    

def Employee(request):
    if(request.method=='POST'):
        Euserid=request.POST['euserid']
        Ecompanyname=request.POST['ecompany']
        Epassword=request.POST['epassword']

        user=authenticate(request,Userid=Euserid,Companyname=Ecompanyname,password= Epassword)

        if user is not None:
            messages.info(request,f"you have logged in as {Euserid}")
            Employee(request,user)

        else:
            messages.info(request,'no employeer found')
            return redirect('Employee')

    return render(request,'employeelogin.html')

def Login(request):
    if(request.method=='POST'):
        #Cname =variable name,cname=name_attribute value
        Lusername=request.POST['lusername']
        Lpassword=request.POST['lpassword']
        # checking authentication
        user=authenticate(request,username=Lusername,password=Lpassword)
        

        if user is not None:
            messages.info(request,f"you have logged in as {Lusername}")
            login(request,user)    

        else:
            messages.info(request,'no user found')
            return redirect('Login')
    

    return render(request,'Login.html')

def Register(request):
    if(request.method=='POST'):
        #Cname =variable name,cname=name_attribute value
        Rusername=request.POST['rnewUsername']
        Remail=request.POST['rnewEmail']
        Rpassword=request.POST['rnewPassword']

        # conditions for checking the user exist
        if User.objects.filter(username=Rusername).exists():
            messages.info(request,'Username already exists')
            return redirect('Register')
        if User.objects.filter(email=Remail).exists():
            messages.info(request,'Username already exists')
            return redirect('Register')
        if User.objects.filter(password=Rpassword).exists():
            messages.info(request,'Username already exists')
            return redirect('Register')
        # if profile.objects.filter(mobile=Rmobile).exists():
        #     messages.info(request,'Username already exists')
        #     return redirect('Login')
        else:
            user=User.objects.create_user(username=Rusername,email=Remail,password=Rpassword)
        #  mobile=profile.objects.create(mobile=Rmobile,user=user)
            # profile.save()
            return redirect('Register')
          
        
        
    return render(request,'register.html')

def Job(request):
    if request.method=='POST':
        Jobtitle=request.POST['pjob_role']
        companyname=request.POST['pcompany_name']
        vacancies=request.POST['pvacancies']
        Location=request.POST['plocation']
        description=request.POST['psalary']
        salary=request.POST['pjob_description']
       # images=request.FILES.get('')
        
        # saving the data into database
        record=PostJobs.objects.create(jobtitle=Jobtitle, Companyname=companyname,Numofvacancies= vacancies,location= Location,Jobdescription= description,Salary=salary)
        record.save()

    else:
         return render(request,'Postajob.html')
    

    return render(request,'Postajob.html')

    
def Result(request):
    data=contact.objects.all()
    return render(request,'result.html',{'contactlist':data})
