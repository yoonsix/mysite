from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

# 최상위 urls.py 에서 
# 127.0.0.1/polls/ 를 파싱해주고 
# path별로 다른 앱으로 분기를 시켜줌