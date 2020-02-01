"""Everything you see at http://localhost:8000/form/ goes through here

"""
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

from .forms import SomeForm
from form.models import SomeModel

from django.utils import timezone

def index(request):

    """Note that in form.html:
    <form action="/form/" method="post">
    , hence, submitting the form will return to the form with the "post" method. 
    
    If this is a POST request we need to process the form data
    """
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SomeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # extract data from input form
            added_numbers = form.cleaned_data['first_number'] + form.cleaned_data['second_number']
            
            # get the previous submission from the DB
            #latest_entry = SomeModel.objects.latest()
            #added_numbers += latest_entry.first_number
            
            # save to DB model
            new_submission = SomeModel()
            new_submission.date_submitted = timezone.now()
            new_submission.first_name = form.cleaned_data['first_name']
            new_submission.last_name = form.cleaned_data['last_name']
            new_submission.first_number = form.cleaned_data['first_number']
            new_submission.second_number = form.cleaned_data['second_number']
            new_submission.save()
            
            # query from entries in DB
            total_submitted = 0
            # see: https://docs.djangoproject.com/en/3.0/topics/db/queries/
            # for raw SQL query see: https://docs.djangoproject.com/en/3.0/topics/db/sql/
            for obj in SomeModel.objects.all():
                total_submitted += obj.first_number + obj.second_number
            
            # create response text
            reply_text = f"Numbers from  {form.cleaned_data['last_name']} yield {added_numbers:,.2f}! As of {timezone.now().date()}, the total from all submissions, including this one, is {total_submitted:,.2f}"
            
            # reset form
            if form.cleaned_data['reset_form']:
                form = SomeForm()
            
            return render(request, 'form.html', {'reply_text': reply_text, 'form': form})
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SomeForm()
    return render(request, 'form.html', {'form': form})