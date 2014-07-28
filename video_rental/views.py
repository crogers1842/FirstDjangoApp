from django.shortcuts import render
from django.views import generic
from models import Video
# Create your views here.


# class VideoListView(generic.ListView):
#     template_name = "video_rental/list.html"
#     context_object_name = 'video_list'
#
#     def get_queryset(self):
#         return Video.objects.all()
#
#
# class VideoView(generic.DetailView):
#     model = Video
#     template_name = "video_rental/view.html"
#
#
# def home(request):
#     return render(request, "video_rental/home.html")
#
#
# def search(request):
#     return render(request, "video_rental/search.html")
#
#
# def rent(request):
#     return render(request,"")