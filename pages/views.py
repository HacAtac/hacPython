from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-listDate').filter(isPublished=True)[:3]
    context = {
        'listings': listings
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hireDate')
    # Get MVP reltor (realtor that bool is checked true)
    mvpRealtors = Realtor.objects.all().filter(isMvp=True)
    # Context to pass to the template
    context = {
        'realtors': realtors,
        'mvpRealtors': mvpRealtors
    }
    return render(request, 'pages/about.html', context)
