from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
from datetime import date

def index(request):
    # Handle creating a new User via form POST
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        birth_date = request.POST.get('birth_date')
        
        if name and surname and birth_date:
            Person.objects.create(name=name, surname=surname, birth_date=birth_date)
            return redirect('users_index') # redirect to same page to prevent double submisson
            
    # Regular GET request logic
    person = Person.objects.last() # Show the most recently added person
    age_text = "ჯერ არ არის დამატებული იუზერი ბაზაში."
    
    if person:
        today = date.today()
        # Calculate age exactly
        age = today.year - person.birth_date.year - ((today.month, today.day) < (person.birth_date.month, person.birth_date.day))
        age_text = f"ბოლოს დამატებული იუზერი - სახელი: {person.name}, გვარი: {person.surname}, ასაკი: {age} წელი"
        
    return render(request, 'users/add_user.html', {'age_text': age_text})

