from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import *
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="LOGIN.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")
class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homebg = HomeBG.objects.all()
        ideas = TourIdea.objects.all()
        mezhet = Mezhet.objects.all()
        apranqner = Apranqner.objects.all()
        amragir = Amragir.objects.all()
        champordvayr = ChampordVayr.objects.all()
        karciqner = Karciqner.objects.all()

        return render(request, self.template_name, {'homebg':homebg, 'ideas':ideas, 'mezhet':mezhet, 'apranqer':apranqner, 'amragir':amragir, 'champordvayr':champordvayr, 'karciqner':karciqner})

class AboutListView(ListView):
    template_name = 'aboutus.html'

    def get(self, request):
        abouts = About.objects.all()
        return render(request, self.template_name, {'abouts':abouts})


class StaysListView(ListView):
	template_name = 'stays.html'
	
	def get(self, request):
		staysmin = Staysmin.objects.all()
		staysmax = Staysmax.objects.all()
		propertyst = PropertyST.objects.all()
		propertytyp = PropertyTyp.objects.all()
		bhk = BHK.objects.all()
		aminit = Aminit.objects.all()
		bedroom = Bedroom.objects.all()
		bathroom = Bathroom.objects.all()
		services = Services.objects.all()
		stayshotel = StaysHotel.objects.all()
		return render(request, self.template_name, {'staysmin':staysmin, 'staysmax':staysmax, 'propertyst':propertyst, 'propertytyp':propertytyp,'bhk':bhk, 'aminit':aminit, 'bedroom':bedroom, 'bathroom':bathroom, 'services':services, 'stayshotel':stayshotel})



class BlogListView(ListView):
    template_name = 'blog.html'

    def get(self, request):
        blogbg = Blogbg.objects.all()
        hayvayr = Hayvayr.objects.all()
        return render(request, self.template_name, {'blogbg':blogbg, 'hayvayr':hayvayr} )

class FlightsListView(ListView):
	template_name = 'flights.html'
	
	def get(self, request):
		flights = Flights.objects.all()
		flightspay = Flightspay.objects.all()
		flightsrec = Flightsrec.objects.all()
		return render(request, self.template_name, {'flights':flights, 'flightspay':flightspay, 'flightsrec':flightsrec})
