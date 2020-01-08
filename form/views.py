from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

from .forms import SomeForm

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SomeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # extract data from input form
            added_numbers = form.cleaned_data['first_number'] + form.cleaned_data['second_number']
            reply_text = f"Submission from:  {form.cleaned_data['last_name']} yields {added_numbers}"
            # reset form
            if form.cleaned_data['reset_form']:
                form = SomeForm()
            # display data and empty form
            return render(request, 'form.html', {'reply_text': reply_text, 'form': form})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SomeForm()
    return render(request, 'form.html', {'form': form})