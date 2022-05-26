from django.shortcuts import redirect, render
from .forms import ResumeForm
from .models import Resume
from django.views import View
from django.contrib import messages
# Create your views here.
class HomeView(View):
    def get(self,request):
        form=ResumeForm()
        return render(request,'app/home.html',{'form':form})

    def post(self,request):
        form=ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Succefullay')
            return redirect('/')
