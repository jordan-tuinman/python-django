from django.shortcuts import render

# Create your views here.

def index(request):
  meetups = [
    {'title': 'A sample meetup', 
    'location': 'Tokyo', 
    'slug': 'a-first-meetup'},
    {'title': 'A second sample meetup', 
    'location': 'New York', 
    'slug': 'a-second-meetup'},
    {'title': 'A third sample meetup', 
    'location': 'Tokyo', 
    'slug': 'a-third-meetup'},
    {'title': 'A fourth sample meetup', 
    'location': 'Tokyo', 
    'slug': 'a-fourth-meetup'}
  ]
  return render(request, 'meetups/index.html', {
    'show_meetups': True,
    'meetups': meetups
  })
