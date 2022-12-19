from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout,login
from .forms import TeacherForm,DesireForm, DesireFormUpdate, AddingCourseForm, AddingTomeForm, ModUserForm, AddingFileForm
from .models import Desires_model, Courses_model, DT_model,Days_model, User, Semester_files
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

def login_page(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.get_user()
            login(request, username)
            if request.user.is_superuser:
                return redirect("faculty_page")
            else:
                return redirect("teacher_page")
                
    context = {"form":form}
    return render(request, 'base/login_page.html', context)

def logout_page(request):
    logout(request)
    return redirect("login_page")

def signup_page(request):
    form = TeacherForm()
    if request.method == "POST":
        form = TeacherForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_page")
    context = {"form":form}
    return render(request, 'base/signup_page.html', context)


@login_required(login_url='login_page')
def teacher_page(request):
    courses = Courses_model.objects.all()
    form = DesireForm()

    if request.method == "POST":
        # d1......
        id_d1 = request.POST.get('d1')
        # id_d1t1 = request.POST.get('d1t1')
        # id_d1t2 = request.POST.get('d1t2')
        # id_d1t3 = request.POST.get('d1t3')
        id_day1 = request.POST.get('day1')

        d1 = Courses_model.objects.get(id = int(id_d1))
        # d1t1 = DT_model.objects.get(id = int(id_d1t1))
        # d1t2 = DT_model.objects.get(id = int(id_d1t2))
        # d1t3 = DT_model.objects.get(id = int(id_d1t3))
        day1 = Days_model.objects.get(id = int(id_day1))


        d1t1 = request.POST.get("d1t1")
        d1t2 = request.POST.get("d1t2")
        d1t3 = request.POST.get("d1t3")

        # d2......
        id_d2 = request.POST.get('d2')
        # id_d2t1 = request.POST.get('d2t1')
        # id_d2t2 = request.POST.get('d2t2')
        # id_d2t3 = request.POST.get('d2t3')
        id_day2 = request.POST.get('day2')


        d2 = Courses_model.objects.get(id = int(id_d2))
        # d2t1 = DT_model.objects.get(id = int(id_d2t1))
        # d2t2 = DT_model.objects.get(id = int(id_d2t2))
        # d2t3 = DT_model.objects.get(id = int(id_d2t3))
        day2 = Days_model.objects.get(id = int(id_day2))


        d2t1 = request.POST.get("d2t1")
        d2t2 = request.POST.get("d2t2")
        d2t3 = request.POST.get("d2t3")


        # d3......
        id_d3 = request.POST.get('d3')
        # id_d3t1 = request.POST.get('d3t1')
        # id_d3t2 = request.POST.get('d3t2')
        # id_d3t3 = request.POST.get('d3t3')
        id_day3 = request.POST.get('day3')


        d3 = Courses_model.objects.get(id = int(id_d3))
        # d3t1 = DT_model.objects.get(id = int(id_d3t1))
        # d3t2 = DT_model.objects.get(id = int(id_d3t2))
        # d3t3 = DT_model.objects.get(id = int(id_d3t3))
        day3 = Days_model.objects.get(id = int(id_day3))


        d3t1 = request.POST.get("d3t1")
        d3t2 = request.POST.get("d3t2")
        d3t3 = request.POST.get("d3t3")


        # d4......
        id_d4 = request.POST.get('d4')
        d4 = Courses_model.objects.get(id = int(id_d4))

        if request.POST.get('d4t1') != "":
            # id_d4 = request.POST.get('d4')
            # id_d4t1 = request.POST.get('d4t1')
            # id_d4t2 = request.POST.get('d4t2')
            # id_d4t3 = request.POST.get('d4t3')

            id_day4 = request.POST.get('day4')
            # print(id_day4)

            # d4 = Courses_model.objects.get(id = int(id_d4))
            # d4t1 = DT_model.objects.get(id = int(id_d4t1))
            # d4t2 = DT_model.objects.get(id = int(id_d4t2))
            # d4t3 = DT_model.objects.get(id = int(id_d4t3))
            day4 = Days_model.objects.get(id = int(id_day4))

            d4t1 = request.POST.get("d4t1")
            d4t2 = request.POST.get("d4t2")
            d4t3 = request.POST.get("d4t3")
            # day4 = request.POST.get("day4")

        else:
            d4t1 = None
            d4t2 = None
            d4t3 = None
            day4 = None
        
        if request.POST.get('d5').isdigit():
            id_d5 = request.POST.get('d5')
            # id_d5t1 = request.POST.get('d5t1')
            # id_d5t2 = request.POST.get('d5t2')
            # id_d5t3 = request.POST.get('d5t3')
            # id_day5 = request.POST.get('day5')

            d5 = Courses_model.objects.get(id = int(id_d5))
            # d5t1 = DT_model.objects.get(id = int(id_d5t1))
            # d5t2 = DT_model.objects.get(id = int(id_d5t2))
            # d5t3 = DT_model.objects.get(id = int(id_d5t3))
            # day5 = Days_model.objects.get(id = int(id_day5))
        else:
            d5 = None


        if day1 == day2 == day3:
            messages.error(request, "Days should not be same!!!")
            return redirect("teacher_page")
        
        if d1t1 == d1t2 == d1t3:
            messages.error(request, "1st Desire times should not be same!!!")
            return redirect("teacher_page")
        
        if d2t1 == d2t2 == d2t3:
            messages.error(request, "2nd Desire times should not be same!!!")
            return redirect("teacher_page")
        
        if d3t1 == d3t2 == d3t3:
            messages.error(request, "3rd Desire times should not be same!!!")
            return redirect("teacher_page")
        
        if d4t1 != None:
            if d4t1 == d4t2 == d4t3:
                messages.error(request, "4th Desire times should not be same!!!")
                return redirect("teacher_page")


        if Desires_model.objects.filter(user=request.user).exists() == False:
            model_is = Desires_model(user = request.user, d1 = d1, d1t1 = d1t1, d1t2 = d1t2, d1t3 = d1t3,day1 = day1,
                                                   d2 = d2, d2t1 = d2t1, d2t2 = d2t2, d2t3 = d2t3,day2 = day2,
                                                   d3 = d3, d3t1 = d3t1, d3t2 = d3t2, d3t3 = d3t3,day3 = day3,
                                                   d4 = d4, d4t1 = d4t1, d4t2 = d4t2, d4t3 = d4t3,day4 = day4,
                                                   d5 = d5, d5t1 = None, d5t2 = None, d5t3 = None,day5 = None,)
            model_is.save()
            return redirect("summary_page")
        else:
            messages.error(request, "Already Registered!!!")
            return redirect("teacher_page")
    
    context = {'form':form, 'courses':courses}
    return render(request, 'base/teacher_page.html', context)



@login_required(login_url='login_page')
def summary_page(request):

    model1 = Desires_model.objects.filter(user = request.user)
    user = request.user
    email = user.email

    if request.method == "POST":
        try:
            for item in model1:
                d1 = item.d1
                d1t1 = item.d1t1
                d1t2 = item.d1t2
                d1t3 = item.d1t3
                day1 = item.day1

                d2 = item.d2
                d2t1 = item.d2t1
                d2t2 = item.d2t2
                d2t3 = item.d2t3
                day2 = item.day2

                d3 = item.d3
                d3t1 = item.d3t1
                d3t2 = item.d3t2
                d3t3 = item.d3t3
                day3 = item.day3

                d4 = item.d4
                d4t1 = item.d4t1
                d4t2 = item.d4t2
                d4t3 = item.d4t3
                day4 = item.day4

                # d5 = item.d5
                # d5t1 = item.d5t1
                # d5t2 = item.d5t2
                # d5t3 = item.d5t3
                # day5 = item.day5

            subject = 'Course Regestiration Summary'
            message = f"1st Desire {d1} > Time1: {d1t1} - Time2: {d1t2} - Time3: {d1t3} - Days: {day1}\n2nd Desire {d2} > Time1: {d2t1} - Time2: {d2t2} - Time3: {d2t3} - Days: {day2}\n3rd Desire {d3} > Time1: {d3t1} - Time2: {d3t2} - Time3: {d3t3} - Days: {day3}\n4th Desire {d4} > Time1: {d4t1} - Time2: {d4t2} - Time3: {d4t3} - Days: {day4}"
                        
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list, fail_silently=False)
            return redirect("email_page")
        except:
            print("Error")
        
    context = {'model1':model1}
    return render(request, 'base/summary_page.html', context)


@login_required(login_url='login_page')
def email_page(request):
    context = {}
    return render(request, 'base/email_page.html', context)


@login_required(login_url='login_page')
def teacher_modify_page(request,pk):

    model_is = Desires_model.objects.get(id = pk)

    d1 = Courses_model.objects.get(title = model_is.d1)
    d2 = Courses_model.objects.get(title = model_is.d2)
    d3 = Courses_model.objects.get(title = model_is.d3)
    d4 = Courses_model.objects.get(title = model_is.d4)
    d5 = Courses_model.objects.get(title = model_is.d5)

    d1t1 = DT_model.objects.get(time_value = model_is.d1t1)
    d1t2 = DT_model.objects.get(time_value = model_is.d1t2)
    d1t3 = DT_model.objects.get(time_value = model_is.d1t3)

    d2t1 = DT_model.objects.get(time_value = model_is.d2t1)
    d2t2 = DT_model.objects.get(time_value = model_is.d2t2)
    d2t3 = DT_model.objects.get(time_value = model_is.d2t3)

    d3t1 = DT_model.objects.get(time_value = model_is.d3t1)
    d3t2 = DT_model.objects.get(time_value = model_is.d3t2)
    d3t3 = DT_model.objects.get(time_value = model_is.d3t3)


    day1 = Days_model.objects.get(title = model_is.day1)
    day2 = Days_model.objects.get(title = model_is.day2)
    day3 = Days_model.objects.get(title = model_is.day3)

    
    try:
        d4t1 = DT_model.objects.get(time_value = model_is.d4t1)
        d4t2 = DT_model.objects.get(time_value = model_is.d4t2)
        d4t3 = DT_model.objects.get(time_value = model_is.d4t3)
        day4 = Days_model.objects.get(title = model_is.day4)

        initial_fields = {

        'd1':d1.id,
        'd2':d2.id,
        'd3':d3.id,
        'd4':d4.id,
        'd5':d5.id,

        'd1t1':d1t1.id,
        'd1t2':d1t2.id,
        'd1t3':d1t3.id,

        'd2t1':d2t1.id,
        'd2t2':d2t2.id,
        'd2t3':d2t3.id,

        'd3t1':d3t1.id,
        'd3t2':d3t2.id,
        'd3t3':d3t3.id,

        'd4t1':d4t1.id,
        'd4t2':d4t2.id,
        'd4t3':d4t3.id,

        'day1': day1.id,
        'day2': day2.id,
        'day3': day3.id,
        'day4': day4.id,

    }

    except DT_model.DoesNotExist:
        d4t1 = None
        d4t2 = None
        d4t3 = None
        day4 = None

        initial_fields = {

        'd1':d1.id,
        'd2':d2.id,
        'd3':d3.id,
        'd4':d4.id,
        'd5':d5.id,

        'd1t1':d1t1.id,
        'd1t2':d1t2.id,
        'd1t3':d1t3.id,

        'd2t1':d2t1.id,
        'd2t2':d2t2.id,
        'd2t3':d2t3.id,

        'd3t1':d3t1.id,
        'd3t2':d3t2.id,
        'd3t3':d3t3.id,

        # 'd4t1':d4t1.id,
        # 'd4t2':d4t2.id,
        # 'd4t3':d4t3.id,

        'day1': day1.id,
        'day2': day2.id,
        'day3': day3.id,
        # 'day4': day4.id,

    }

    
    
    


    # initial_fields = {

    #     'd1':d1.id,
    #     'd2':d2.id,
    #     'd3':d3.id,
    #     'd4':d4.id,
    #     'd5':d5.id,

    #     'd1t1':d1t1.id,
    #     'd1t2':d1t2.id,
    #     'd1t3':d1t3.id,

    #     'd2t1':d2t1.id,
    #     'd2t2':d2t2.id,
    #     'd2t3':d2t3.id,

    #     'd3t1':d3t1.id,
    #     'd3t2':d3t2.id,
    #     'd3t3':d3t3.id,

    #     'd4t1':d4t1.id,
    #     'd4t2':d4t2.id,
    #     'd4t3':d4t3.id,

    #     'day1': day1.id,
    #     'day2': day2.id,
    #     'day3': day3.id,
    #     'day4': day4.id,

    # }


    form = DesireFormUpdate(initial = initial_fields, instance = model_is)
    
    if request.method == "POST":
        form = DesireFormUpdate(request.POST,instance=model_is)
        if form.is_valid():
            form.save()
            return redirect("summary_page")
        else:
            print(form.errors.as_data())
    
    # context = {'form':form, 'd4':d4}
    context = {'form':form, 'd4t1':d4t1}
    return render(request, 'base/teacher_modify_page.html', context)


@login_required(login_url='login_page')
def faculty_page(request):
    context = {}
    return render(request, 'base/faculty_page.html', context)
    
###########################################################################

# course pages

@login_required(login_url='login_page')
def course_page(request):
    courses = Courses_model.objects.all()
    context = {"courses":courses}
    return render(request, 'base/course_page.html', context)


@login_required(login_url='login_page')
def add_course_page(request):
    form = AddingCourseForm()
    if request.method == "POST":
        form = AddingCourseForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect("course_page")
    context ={'form':form}
    return render(request, 'base/add_course_page.html', context)


@login_required(login_url='login_page')
def modify_course_page(request, pk):
    course_is = Courses_model.objects.get(id = pk)
    form = AddingCourseForm(instance = course_is)
    if request.method == "POST":
        form = AddingCourseForm(instance = course_is, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect("course_page")
    
    context ={'form':form}
    return render(request, 'base/modify_course_page.html', context)


@login_required(login_url='login_page')
def delete_course_page(request, pk):
    course_is = Courses_model.objects.get(id = pk)
    if request.method == "POST":
        course_is.delete()
        return redirect("course_page")
        
    context ={'course_is':course_is}
    return render(request, 'base/delete_course_page.html', context)



###########################################################################

# time pages


@login_required(login_url='login_page')
def time_page(request):
    users = User.objects.all()
    
    context = {'users':users}
    return render(request, 'base/time_page.html', context)


@login_required(login_url='login_page')
def summary_page_for_admin(request, pk):
    
    model1 = Desires_model.objects.filter(user = pk)

    # model1_username = Desires_model.objects.get(user = pk)
    try:
        model1_username = Desires_model.objects.get(user = pk)
    except Desires_model.DoesNotExist:
        model1_username = None
    

    context = {'model1':model1, 'model1_username':model1_username}
    return render(request, 'base/summary_page_for_admin.html', context)



@login_required(login_url='login_page')
def teacher_modify_page_for_admin(request,pk):

    model_is = Desires_model.objects.get(id = pk)

    form = DesireFormUpdate(initial = {"d1":model_is.d1},model_is = model_is, instance = model_is)
    # form.fields['user'].widget = forms.HiddenInput()
    if request.method == "POST":
        print("true")
        form = DesireFormUpdate(model_is = model_is, data = request.POST,instance=model_is)
        print(form.is_valid())
        if form.is_valid():
            print("ok")
            form.save()
            return redirect("time_page")
        else:
            print(form.errors.as_data())
    
    context = {'form':form , 'model_is':model_is}
    return render(request, 'base/teacher_modify_page_for_admin.html', context)



@login_required(login_url='login_page')
def schedual_time_page(request):
    times = DT_model.objects.all()
    
    context = {'times':times}
    return render(request, 'base/schedual_time_page.html', context)



@login_required(login_url='login_page')
def add_schedual_time_page(request):
    form = AddingTomeForm()
    if request.method == "POST":
        form = AddingTomeForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect("schedual_time_page")
    context ={'form':form}
    return render(request, 'base/add_schedual_time_page.html', context)


@login_required(login_url='login_page')
def modify_schedual_time_page(request, pk):
    time_is = DT_model.objects.get(id = pk)
    form = AddingTomeForm(instance = time_is)
    if request.method == "POST":
        form = AddingTomeForm(instance = time_is, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect("schedual_time_page")
    
    context ={'form':form}
    return render(request, 'base/modify_schedual_time_page.html', context)


@login_required(login_url='login_page')
def delete_schedual_time_page(request, pk):
    time_is = DT_model.objects.get(id = pk)
    if request.method == "POST":
        time_is.delete()
        return redirect("schedual_time_page")
        
    context ={'time_is':time_is}
    return render(request, 'base/delete_schedual_time_page.html', context)


###########################################################################

# faculty pages


@login_required(login_url='login_page')
def faculty_page_detail(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'base/faculty_page_detail.html', context)


@login_required(login_url='login_page')
def faculty_page_modify(request, pk):
    user_is = User.objects.get(id = pk)
    form = ModUserForm(instance = user_is)
    if request.method == "POST":
        form = ModUserForm(instance = user_is, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect("faculty_page_detail")
    
    context ={'form':form}
    return render(request, 'base/faculty_page_modify.html', context)

@login_required(login_url='login_page')
def delete_faculty_page(request, pk):
    user_is = User.objects.get(id = pk)
    if request.method == "POST":
        user_is.delete()
        return redirect("faculty_page_detail")
        
    context ={'user_is':user_is}
    return render(request, 'base/delete_faculty_page.html', context)


###########################################################################

# schedule pages

@login_required(login_url='login_page')
def schedule_course_page(request):
    courses = Courses_model.objects.all()
    d1_user = {}
    for course in courses:
        model = Desires_model.objects.filter(d1 = course)
        d1_user[course] = model
    
    d2_user = {}
    for course in courses:
        model = Desires_model.objects.filter(d2 = course)
        d2_user[course] = model
   
    d3_user = {}
    for course in courses:
        model = Desires_model.objects.filter(d3 = course)
        d3_user[course] = model

    context = {'courses':courses, 'd1_user':d1_user , 'd2_user':d2_user, 'd3_user':d3_user}
    return render(request, 'base/schedule_course_page.html', context)


@login_required(login_url='login_page')
def schedule_time_page_(request):
    times = DT_model.objects.all()

    d1t1_user = []
    for time in times:
        d1t1_user.append(Desires_model.objects.filter(d1t1 = time))
    

    d2t1_user = []
    for time in times:
        d2t1_user.append(Desires_model.objects.filter(d2t1 = time))
    
    d3t1_user = []
    for time in times:
        d3t1_user.append(Desires_model.objects.filter(d3t1 = time))
    

    final_dic = {}

    for index in range(len(times)):
        final_list = []
        final_list.append(d1t1_user[index])
        final_list.append(d2t1_user[index])
        final_list.append(d3t1_user[index])

        final_dic[times[index]] = final_list
    
    context = {'final_dic':final_dic}
    return render(request, 'base/schedule_time_page_.html', context)



@login_required(login_url='login_page')
def schedule_time_page_1(request):
    times = DT_model.objects.all()

    d1t1_user = []
    for time in times:
        d1t1_user.append(Desires_model.objects.filter(d1t1 = time))
    
    d2t1_user = []
    for time in times:
        d2t1_user.append(Desires_model.objects.filter(d2t1 = time))
    
    d3t1_user = []
    for time in times:
        d3t1_user.append(Desires_model.objects.filter(d3t1 = time))

    final_dic = {}

    for index in range(len(times)):
        final_list = []
        final_list.append(d1t1_user[index])
        final_list.append(d2t1_user[index])
        final_list.append(d3t1_user[index])

        final_dic[times[index]] = final_list
    
    context = {'final_dic':final_dic}
    return render(request, 'base/schedule_time_page_1.html', context)


@login_required(login_url='login_page')
def schedule_time_page_2(request):
    times = DT_model.objects.all()

    d1t1_user = []
    for time in times:
        d1t1_user.append(Desires_model.objects.filter(d1t1 = time))
    

    d2t1_user = []
    for time in times:
        d2t1_user.append(Desires_model.objects.filter(d2t1 = time))
    
    d3t1_user = []
    for time in times:
        d3t1_user.append(Desires_model.objects.filter(d3t1 = time))
    

    final_dic = {}

    for index in range(len(times)):
        final_list = []
        final_list.append(d1t1_user[index])
        final_list.append(d2t1_user[index])
        final_list.append(d3t1_user[index])

        final_dic[times[index]] = final_list
    
    
    context = {'final_dic':final_dic}
    return render(request, 'base/schedule_time_page_2.html', context)



@login_required(login_url='login_page')
def schedule_time_page_3(request):
    times = DT_model.objects.all()

    d1t1_user = []
    for time in times:
        d1t1_user.append(Desires_model.objects.filter(d1t1 = time))
    

    d2t1_user = []
    for time in times:
        d2t1_user.append(Desires_model.objects.filter(d2t1 = time))
    
    d3t1_user = []
    for time in times:
        d3t1_user.append(Desires_model.objects.filter(d3t1 = time))
    

    final_dic = {}

    for index in range(len(times)):
        final_list = []
        final_list.append(d1t1_user[index])
        final_list.append(d2t1_user[index])
        final_list.append(d3t1_user[index])

        final_dic[times[index]] = final_list
    

    context = {'final_dic':final_dic}
    return render(request, 'base/schedule_time_page_3.html', context)



###########################################################################

# archive pages

@login_required(login_url='login_page')
def archive_page(request):
    context = {}
    return render(request, 'base/archive_page.html', context)


@login_required(login_url='login_page')
def archive_user_page(request):

    files = Semester_files.objects.all()
    context = {"files":files}
    return render(request, 'base/archive_user_page.html', context)


@login_required(login_url='login_page')
def add_file_page(request):
    form = AddingFileForm()
    if request.method == "POST":
        form = AddingFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("archive_user_page")
    context ={'form':form}
    return render(request, 'base/add_file_page.html', context)

@login_required(login_url='login_page')
def delete_file(request,pk):
    file = Semester_files.objects.get(id = pk)
    if request.method == "POST":
        file.delete()
        return redirect("archive_user_page")
    context = {'file':file}
    return render(request, 'base/delete_file_page.html', context)


@login_required(login_url='login_page')
def archive_user_summary_page(request, pk):
    
    model1 = Desires_model.objects.filter(user = pk)

    # model1_username = Desires_model.objects.get(user = pk)
    try:
        model1_username = Desires_model.objects.get(user = pk)
    except Desires_model.DoesNotExist:
        model1_username = None
    

    context = {'model1':model1, 'model1_username':model1_username}
    return render(request, 'base/archive_user_summary_page.html', context)



def test_page(request):
    context = {}
    return render(request, 'base/test_page.html', context)



def done_page(request):
    dayOne_selection = request.GET.get("dayOne_selection")
    times = DT_model.objects.filter(group = dayOne_selection)

    time_list = []
    for time in times:
        time_list.append(time.time_value)

    return JsonResponse({"times":time_list},status = 200)
