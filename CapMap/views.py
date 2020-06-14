from django.shortcuts import render
from django.http import HttpResponse
from .models import MapLocation


def map_view(request):
    key = str('AIzaSyCw6G6AnBOLTw1tcl3n4sxxvIPZTqO2khQ')
    all_location = MapLocation.objects.all()
    print(all_location)
    # for location in all_location:
    #     print(location.latitude)
    if request.method == 'POST':
        lat = request.POST["latitude"]
        lng = request.POST["longitude"]
        pop_up_text = request.POST["PopUp_Text"]
        # print(f"Latitude: {lat}\nLongitude: {lng}")
        hunter1 = float(lat)
        hunter2 = float(lng)
        add_lat = MapLocation(latitude=hunter1, longitude=hunter2, pop_up_text=pop_up_text)
        add_lat.save()
        print(add_lat)
        # print(hunter1, hunter2)
        return render(request, 'CapMap/MapPage.html')
    return render(request, 'CapMap/MapPage.html', {
            'key': key,
            'all_location': all_location}
         )


