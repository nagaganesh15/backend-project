from django.urls import path
from .views import register,loginuser,resetpassword,getusername,saveusername,updateprofileimage,updatememoryscore,updatestonescore,updateguessscore,updatewaterscore,updatebrickscore,getAllhighestscores,getMemoryscores,getprofileimg,getStonescores,getGuessscores,getBrickscores,getWaterscores,sendmessage
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('register/',register,name='register'),
    path('login/',loginuser,name='loginuser'),
    path('resetpassword/',resetpassword,name='resetpassword'),
    # path('memoryscore/',memoryscore,name='memoryscore'),
    path('getusername/',getusername,name='getusername'),
    path('saveusername/',saveusername,name='saveusername'),
    path('updateprofileimage/',updateprofileimage,name='updateprofileimage'),
    path('updatememoryscore/',updatememoryscore,name='updatememoryscore'),
    path('updatestonescore/',updatestonescore,name='updatestonescore'),
    path('updateguessscore/',updateguessscore,name='updateguessscore'),
    path('updatewaterscore/',updatewaterscore,name='updatewaterscore'),
    path('updatebrickscore/',updatebrickscore,name='updatebrickscore'),
    path('getAllhighestscores/',getAllhighestscores,name='getAllhighestscores'),
    path('getMemoryscores/',getMemoryscores,name='getMemoryscores'),
    path('getprofileimg/',getprofileimg,name='getprofileimg'),
    path('getStonescores/',getStonescores,name='getStonescores'),
    path('getGuessscores/',getGuessscores,name='getGuessscores'),
    path('getWaterscores/',getWaterscores,name='getWaterscores'),
    path('getBrickscores/',getBrickscores,name='getBrickscores'),
    path('sendmessage/',sendmessage,name='sendmessage'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
