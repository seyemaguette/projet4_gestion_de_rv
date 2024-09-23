from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login , authenticate, update_session_auth_hash,logout
from django.contrib.auth.decorators import login_required
from .forms import  (UserCreation, login_form, UserupdateForm, DoctorForm, UpdateDoctorForm, UpdateProfil,
CreatePatient, CreateRv)
from .models import Doctor, Patient, Profil, Rv,Personne
from django.contrib import messages
# from .decorators import doctor_required
from .decorators import doctor_required

# @api_view(['GET','POST','PUT'])
def api_view(request) :
    #request => HttpRequest
    serializer = PersonneSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    else :
        return Response({'details':'invalid data'})
#---------------------API------------------

# # Create your views here.
def index(request):


    return render(request,'pages/index.html')


 

def new_doctor(request):
    form=UserCreation()
    p_form=DoctorForm()
    if request.method == 'POST':
        form = UserCreation(request.POST or None)
        p_form=DoctorForm(request.POST or None)
        if form.is_valid() and p_form.is_valid() : 
            user=form.save() 
            doctor= user.doctor
            doctor.address= p_form.cleaned_data.get('address')
            doctor.phone= p_form.cleaned_data.get('phone')
            doctor.role= p_form.cleaned_data.get('role')
            doctor.save()

            
            messages.success(request,f'le compte a ete creer avec succes')
            
            return redirect('/login/') 


    return render(request,'rv/new_doctor.html',{'form':form, 'doctor':p_form})
@doctor_required
def update_doctor(request):
    
    
    if request.method == 'POST':
        u_form=UserupdateForm(request.POST,instance=request.user)
        p_form=UpdateDoctorForm(request.POST, instance=request.user.doctor)
        if u_form.is_valid() and p_form.is_valid(): 
            user=u_form.save() 
            doctor= user.doctor
            doctor.address= p_form.cleaned_data.get('address')
            doctor.phone= p_form.cleaned_data.get('phone')
            doctor.save()
            messages.success(request,f'Modifier avec succes')
        return redirect('/my_account/') 

    else:
        u_form=UserupdateForm(instance=request.user)
        p_form=UpdateDoctorForm(instance=request.user.doctor)
    return render(request,'rv/update_doctor.html',{'form':u_form, 'doctor':p_form})




@doctor_required
def update_profil(request):
    
    if request.method == 'POST':
        # u_form=UserupdateForm(request.POST,instance=request.user)
        p_form=UpdateProfil(request.FILES, instance=request.user.profil)
        if p_form.is_valid(): 
            user=request.user
            profil= user.profil
            if request.FILES.get("avatar"):
                profil.avatar = request.FILES['avatar']
            else:
                profil.avatar=user.profil.avatar
            profil.save()
            messages.success(request,f'Modifier avec succes')
            return redirect('/my_account/') 

    else:
        # u_form=UserupdateForm(instance=request.user)
        p_form=UpdateProfil(instance=request.user.profil)
    return render(request,'rv/update_profil.html',{'profil':p_form})



@doctor_required
def dashboard(request):
    


    return render(request,'rv/dashboard.html')



@doctor_required
def my_account(request):

    # user=Doctor.objects.get(id=request.id)
    doctor= Doctor.objects.get(pk=request.user.pk)
    profil=Profil.objects.get(pk=request.user.pk)


    return render(request,'rv/my_account.html',{'doctor':doctor,'profil':profil})


@doctor_required
def create_patient(request):

    if request.method=='POST':
        form = CreatePatient(request.POST or None)
        if form.is_valid():
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            phone=form.cleaned_data.get('phone')
            age=form.cleaned_data.get('age')
            address=form.cleaned_data.get('address')
            email=form.cleaned_data.get('email')
            doctor= request.user.doctor

            patient = Patient.objects.create(
                first_name = first_name,
                last_name = last_name,
                age = age,
                phone = phone,
                address = address,
                doctor = doctor,
                email = email,
                
                
            )
            patient.save()
            messages.success(request,f'creer avec succes')
            return redirect('/list_patients/')
    
    else:


        form = CreatePatient()
  


    return render(request,'rv/patients/create_patient.html',{'form':form})




@doctor_required
def update_patient(request,id):
    patients = get_object_or_404(Patient, id=id)
    if request.method=='POST':
        form = CreatePatient(request.POST , instance=patients)
        if form.is_valid():
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            phone=form.cleaned_data.get('phone')
            age=form.cleaned_data.get('age')
            address=form.cleaned_data.get('address')
            email=form.cleaned_data.get('email')
            doctor= request.user.doctor
            patients_to_update = Patient.objects.filter(pk=patients.id)
            patients_to_update.update(
                first_name = first_name,
                last_name = last_name,
                age = age,
                phone = phone,
                address = address,
                doctor = doctor,
                email = email,
                
                
            )
            patients.save()
            messages.success(request,f'modifier avec succes')
            return redirect('/list_patients/')
    
    else:

        form = CreatePatient(instance=patients)
  
    return render(request,'rv/patients/update_patient.html',{'form':form})





@doctor_required
def list_patients(request):
    user = request.user.doctor
    patients = Patient.objects.filter(doctor=user,archive=False)
    

    return render(request, 'rv/patients/list_patients.html', {'patients': patients})

@doctor_required
def details_patients(request,id):
    patients = get_object_or_404(Patient, id=id)

    

    return render(request, 'rv/patients/details_patients.html', {'patients': patients})



@doctor_required
def delete_patient(request, id):
    patients =get_object_or_404(Patient, id=id)
    if request.method == 'POST':
        patients_to_delete = Patient.objects.filter(pk=patients.id)
        patients_to_delete.update(
            archive =True
        )            
        messages.success(request,f'supprimer avec succes')

        return redirect('/list_patients/')
    return render(request, 'rv/patients/delete_patient.html', {'patient': patients})



@doctor_required
def create_rv(request):
    if request.method=='POST':
        form = CreateRv(request.POST or None)
        if form.is_valid():
            title=form.cleaned_data.get('title')
            patient=form.cleaned_data.get('patient')
            email=form.cleaned_data.get('email')
            date=form.cleaned_data.get('date')
            hours=form.cleaned_data.get('hours')
            place=form.cleaned_data.get('place')
            doctor = request.user.doctor
            rv = Rv.objects.create(
                title = title,
                patient = patient,
                date = date,
                hours = hours,
                place = place,
                email = patient.email,
                doctor = doctor,
            )
            rv.save()
            messages.success(request,f'creer avec succes')
            return redirect('/list_rv/')
    
    else:
        form = CreateRv()

    return render(request,'rv/rv/create_rv.html',{'form':form})



@doctor_required
def list_rv(request):
    user = request.user.doctor
    rv = Rv.objects.filter(doctor=user,archive=False)
    

    return render(request, 'rv/rv/list_rv.html', {'rvs': rv})



@doctor_required
def details_rv(request,id):
    rvs = get_object_or_404(Rv, id=id)

    

    return render(request, 'rv/rv/details_rv.html', {'rvs': rvs})



@doctor_required
def delete_rv(request, id):
    rvs =get_object_or_404(Rv, id=id)
    if request.method == 'POST':
        rv_to_delete = Rv.objects.filter(pk=rvs.id)
        rv_to_delete.update(
            archive =True
        )            
        messages.success(request,f'supprimer avec succes')

        return redirect('/list_rv/')
    return render(request, 'rv/rv/delete_rv.html', {'rv': rvs})



@doctor_required
def update_rv(request,id):
    rv = get_object_or_404(Rv, id=id)
    if request.method=='POST':
        form = CreateRv(request.POST , instance=rv)
        if form.is_valid():
            title=form.cleaned_data.get('title')
            patient=form.cleaned_data.get('patient')
            email=form.cleaned_data.get('email')
            date=form.cleaned_data.get('date')
            hours=form.cleaned_data.get('hours')
            place=form.cleaned_data.get('place')
            doctor = request.user.doctor
            rv_to_update = Rv.objects.filter(pk=rv.id)
            rv_to_update.update(
                title = title,
                patient = patient,
                date = date,
                hours = hours,
                place = place,
                email = email,
                doctor = doctor,
                
                
            )
            rv.save()
            messages.success(request,f'modifier avec succes')
            return redirect('/list_rv/')
    
    else:

        form = CreateRv(instance=rv)
  
    return render(request,'rv/rv/update_rv.html',{'form':form})



@doctor_required
def update_password(request):
    user= Doctor.objects.get(pk=request.user.pk)
    form = DoctorForm(user=request.user)
    if request.method == 'POST':
        form = DoctorForm(user=request.user ,  data=request.POST)
        if form.is_valid():
            form.save()

            update_session_auth_hash(request, user=request.user)
        # Then finally you save the object with the updated fields
        

        return redirect('/my_account/')
    return render(request,"rv/update_password.html", {'form':form, 'user':user})






@doctor_required
def logout_doctor(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request,f'Deconnexion avec succes')
        return redirect('/')
    return render(request,'rv/logout.html')

def login_view(request):
    form = login_form(request.POST or None)
    if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user) 
                return redirect('/dashboard/') 
    
    return render(request, 'rv/login.html', {'form':form})




