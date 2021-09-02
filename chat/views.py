from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def roomview(request):
    room_no = request.POST['room_no']
    room_name = request.POST['room_name']
    return render(request, 'room.html', {'room_no' : room_no, 'room_name' : room_name})