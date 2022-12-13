# id_d2 = request.POST.get('d2')
        # id_d2t1 = request.POST.get('d2t1')
        # id_d2t2 = request.POST.get('d2t2')
        # id_d2t3 = request.POST.get('d2t3')

        # id_d3 = request.POST.get('d3')
        # id_d3t1 = request.POST.get('d3t1')
        # id_d3t2 = request.POST.get('d3t2')
        # id_d3t3 = request.POST.get('d3t3')



#d3 =id_d3, d3t1 = id_d3t1, d3t2 = id_d3t2, d3t3 = id_d3t3
        #d2 =id_d2, d2t1 = id_d2t1, d2t2 = id_d2t2, d2t3 = id_d2t3
    
    # if request.method == "POST":
        
    #     id_d1 = request.POST.get('d1')
    #     id_d1t1 = request.POST.get('d1t1')
    #     id_d1t2 = request.POST.get('d1t2')
    #     id_d1t3 = request.POST.get('d1t3')

    #     d1 = Courses_model.objects.get(id = int(id_d1))
    #     d1t1 = DT_model_1.objects.get(id = int(id_d1t1))
    #     d1t2 = DT_model_2.objects.get(id = int(id_d1t2))
    #     d1t3 = DT_model_3.objects.get(id = int(id_d1t3))


        # id_d2 = request.POST.get('d2')
        # id_d2t1 = request.POST.get('d2t1')
        # id_d2t2 = request.POST.get('d2t2')
        # id_d2t3 = request.POST.get('d2t3')

        # d2 = Courses_model.objects.get(id = int(id_d2))
        # d2t1 = DT_model.objects.get(id = int(id_d2t1))
        # d2t2 = DT_model.objects.get(id = int(id_d2t2))
        # d2t3 = DT_model.objects.get(id = int(id_d2t3))


        # id_d3 = request.POST.get('d3')
        # id_d3t1 = request.POST.get('d3t1')
        # id_d3t2 = request.POST.get('d3t2')
        # id_d3t3 = request.POST.get('d3t3')

        # d3 = Courses_model.objects.get(id = int(id_d3))
        # d3t1 = DT_model.objects.get(id = int(id_d3t1))
        # d3t2 = DT_model.objects.get(id = int(id_d3t2))
        # d3t3 = DT_model.objects.get(id = int(id_d3t3))
        
        
        # model = Desires_model(user = user, d1 =d1, d1t1 = d1t1.date_value, d1t2 = d1t2.date_value, d1t3 = d1t3.date_value,
        #                       d2 =d2, d2t1 = d2t1.date_value, d2t2 = d2t2.date_value, d2t3 = d2t3.date_value,
        #                       d3 =d3, d3t1 = d3t1.date_value, d3t2 = d3t2.date_value, d3t3 = d3t3.date_value)
        
        # model = Desires_model_1(user = request.user, d1 =d1, d1t1 = d1t1, d1t2 = d1t2, d1t3 = d1t3)           
        # model.save()
        # return redirect("summary_page")






# d2 = models.CharField(max_length=2, choices=COURSE_CHOICES, null=True)
    # d2t1 = models.CharField(max_length=2, choices=TIME_CHOICES, null=True)
    # d2t2 = models.CharField(max_length=2, choices=TIME_CHOICES, null=True)
    # d2t3 = models.CharField(max_length=2, choices=TIME_CHOICES, null=True)

    # d3 = models.CharField(max_length=2, choices=COURSE_CHOICES, null=True)
    # d3t1 = models.CharField(max_length=2, choices=TIME_CHOICES, null=True)
    # d3t2 = models.CharField(max_length=2, choices=TIME_CHOICES, null=True)
    # d3t3 = models.CharField(max_length=2, choices=TIME_CHOICES, null=True)

    

    # d2 = models.CharField(max_length=100, null= True, blank=True)
    # d2t1 = models.DateField(null = True, blank=True)
    # d2t2 = models.DateField(null = True, blank=True)
    # d2t3 = models.DateField(null = True, blank=True)


    # d3 = models.CharField(max_length=100, null= True, blank=True)
    # d3t1 = models.DateField(null = True, blank=True)
    # d3t2 = models.DateField(null = True, blank=True)
    # d3t3 = models.DateField(null = True, blank=True)





    # def __init__(self,*args, **kwargs):
    #     super(DesireForm, self).__init__(*args, **kwargs)
    #     for fieldname in ['d1','d1t1','d1t1','d1t3']:
    #         self.fields[fieldname].help_text = None
    #         self.fields['d1'].label = 'Course'
    #         self.fields['d1t1'].label = 'Time1'
    #         self.fields['d1t2'].label = 'Time2'
    #         self.fields['d1t3'].label = 'Time3'
        
    #     for fieldname in ['d1t1', 'd1t2','d1t3', 'd2t1', 'd2t2', 'd2t3', 'd3t1', 'd3t2' , 'd3t3']:
    #         self.fields[fieldname].help_text = None
    #         self.fields['d1t1'].label = 'Date1'
    #         self.fields['d1t2'].label = 'Date2'
    #         self.fields['d1t3'].label = 'Date3'

    #         self.fields['d2t1'].label = 'Date1'
    #         self.fields['d2t2'].label = 'Date2'
    #         self.fields['d2t3'].label = 'Date3'

    #         self.fields['d3t1'].label = 'Date1'
    #         self.fields['d3t2'].label = 'Date2'
    #         self.fields['d3t3'].label = 'Date3'



    # class DT_form(forms.ModelForm):
#     date = forms.ModelChoiceField(queryset=DT_model.objects.all().order_by('date'))
#     class Meta:
#         model = DT_model
#         fields = ['date'] 
#         widgets = {
#             'date': AdminDateWidget(),
#             'time': AdminTimeWidget(),
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['date'].queryset = DT_model.objects.none()


# class Courses_form(forms.ModelForm):
#     title1 = forms.ModelChoiceField(queryset=Courses_model.objects.all())
#     title2 = forms.ModelChoiceField(queryset=Courses_model.objects.all())
#     class Meta:
#         model = Courses_model
#         fields = ['title1','title2']

# DEMO_CHOICES =[
#     ("1", "Naveen"),
#     ("2", "Pranav"),
#     ("3", "Isha"),
#     ("4", "Saloni"),
# ]

# class Courses_from(forms.Form):
  

#     title = forms.CharField(label="To", widget=forms.Select(choices=DEMO_CHOICES))
#     # title = forms.CharField(queryset=DT_model.objects.all(), label="To")

# form.fields['user'].widget = forms.HiddenInput()






# class Desires_model_1(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     d1 = models.ForeignKey(Courses_model, on_delete=models.CASCADE, null=True)
#     d1t1 = models.ForeignKey(DT_model_1, on_delete=models.CASCADE, null=True)
#     d1t2 = models.ForeignKey(DT_model_2, on_delete=models.CASCADE, null=True)
#     d1t3 = models.ForeignKey(DT_model_3, on_delete=models.CASCADE, null=True)



# <div class = "sdetail">
# <span class="second">2nd desire</span>
# <span>{{item.get_d2_display}}</span>
# <span>{{item.get_d2t1_display}}</span>
# <span>{{item.get_d2t2_display}}</span>
# <span>{{item.get_d2t3_display}}</span>

# </div>



 # d2 = models.CharField(max_length=2, choices=COURSE_CHOICES, null=True)
    # d2t1 = models.CharField(max_length=2, choices=TIME_CHOICES, null=True)
    # d2t2 = models.CharField(max_length=2, choices=TIME_CHOICES, null=True)
    # d2t3 = models.CharField(max_length=2, choices=TIME_CHOICES, null=True)

    # d3 = models.CharField(max_length=2, choices=COURSE_CHOICES, null=True)
    # d3t1 = models.CharField(max_length=2, choices=TIME_CHOICES, null=True)
    # d3t2 = models.CharField(max_length=2, choices=TIME_CHOICES, null=True)
    # d3t3 = models.CharField(max_length=2, choices=TIME_CHOICES, null=True)

    # d4 = models.CharField(max_length=2, choices=COURSE_CHOICES, null=True)
    # d4t1 = models.CharField(max_length=2, choices=TIME_CHOICES, null=True)
    # d4t2 = models.CharField(max_length=2, choices=TIME_CHOICES, null=True)
    # d4t3 = models.CharField(max_length=2, choices=TIME_CHOICES, null=True)

    # d5 = models.CharField(max_length=2, choices=COURSE_CHOICES, null=True)
    # d5t1 = models.CharField(max_length=2, choices=TIME_CHOICES, null=True)
    # d5t2 = models.CharField(max_length=2, choices=TIME_CHOICES, null=True)
    # d5t3 = models.CharField(max_length=2, choices=TIME_CHOICES, null=True)


    # COURSE_CHOICES = [
    #     ("1", 'C1'),
    #     ("2", 'C2'),
    #     ("3", 'C3'),
    #     ("4", 'C4'),
    # ]

    # TIME_CHOICES = [
    #     ("1", 'T1'),
    #     ("2", 'T2'),
    #     ("3", 'T3'),
    #     ("4", 'T4'),
    # ]


    # def teacher_page(request):
#     courses = Courses_model.objects.all()
#     form = DesireForm()
    

#     if request.method == "POST":
#         id_d1 = request.POST.get('d1')
#         id_d1t1 = request.POST.get('d1t1')
#         id_d1t2 = request.POST.get('d1t2')
#         id_d1t3 = request.POST.get('d1t3')

#         id_d2 = request.POST.get('d2')
#         id_d2t1 = request.POST.get('d2t1')
#         id_d2t2 = request.POST.get('d2t2')
#         id_d2t3 = request.POST.get('d2t3')

#         id_d3 = request.POST.get('d3')
#         id_d3t1 = request.POST.get('d3t1')
#         id_d3t2 = request.POST.get('d3t2')
#         id_d3t3 = request.POST.get('d3t3')

#         id_d4 = request.POST.get('d4')
#         id_d4t1 = request.POST.get('d4t1')
#         id_d4t2 = request.POST.get('d4t2')
#         id_d4t3 = request.POST.get('d4t3')

#         id_d5 = request.POST.get('d5')
#         id_d5t1 = request.POST.get('d5t1')
#         id_d5t2 = request.POST.get('d5t2')
#         id_d5t3 = request.POST.get('d5t3')
    
    
    
#         model = Desires_model(user = request.user, d1 =id_d1, d1t1 = id_d1t1, d1t2 = id_d1t2, d1t3 = id_d1t3,
#                                                    d2 =id_d2, d2t1 = id_d2t1, d2t2 = id_d2t2, d2t3 = id_d2t3,
#                                                    d3 =id_d3, d3t1 = id_d3t1, d3t2 = id_d3t2, d3t3 = id_d3t3,
#                                                    d4 =id_d4, d4t1 = id_d4t1, d4t2 = id_d4t2, d4t3 = id_d4t3,
#                                                    d5 =id_d5, d5t1 = id_d5t1, d5t2 = id_d5t2, d5t3 = id_d5t3)
#         model.save()
#         return redirect("summary_page")
    

#     context = {'form':form, 'courses':courses}
#     return render(request, 'base/teacher_page.html', context)


# {% comment %} <div class = "form-contnet">
#                     <span class = 'first'>1st desire:{{form.d1}}</span>
#                     <span>time1:{{form.d1t1}}</span>
#                     <span>time2:{{form.d1t2}}</span>
#                     <span>time3:{{form.d1t3}}</span>
#                 </div>

#                 <div class = "form-contnet">
#                     <span class = "second">2nd desire:{{form.d2}}</span>
#                     <span>time1:{{form.d2t1}}</span>
#                     <span>time2:{{form.d2t2}}</span>
#                     <span>time3:{{form.d2t3}}</span>
#                 </div>

#                 <div class = "form-contnet">
#                     <span class = "third">3rd desire:{{form.d3}}</span>
#                     <span>time1:{{form.d3t1}}</span>
#                     <span>time2:{{form.d3t2}}</span>
#                     <span>time3:{{form.d3t3}}</span>
#                 </div>
                
#                 <div class = "form-contnet">
#                     <span class = "fourth">4th desire:{{form.d4}}</span>
#                     <span>time1:{{form.d4t1}}</span>
#                     <span>time2:{{form.d4t2}}</span>
#                     <span>time3:{{form.d4t3}}</span>
#                 </div>

#                 <div class = "form-contnet">
#                     <span class = "fifth">5th desire:{{form.d5}}</span>
#                     <span>time1:{{form.d5t1}}</span>
#                     <span>time2:{{form.d5t2}}</span>
#                     <span>time3:{{form.d5t3}}</span>
#                 </div> {% endcomment %}