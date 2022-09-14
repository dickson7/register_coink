from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from authentication.models import User


@login_required
def index(request):
    """main view showing the user's data or the list of users if it is superuser

    Args:
        request (get): request with the user's id, it worked with the email address

    Returns:
        context: user's data, to display in the view
    """
    users = User.objects.filter(email=request.user)
    if users[0].is_superuser:
        users = User.objects.all()
    all_count = users.count()
    
    context = {'users': users, 
               'all_count':all_count
               }
    return render(request, 'coink/index.html', context)



