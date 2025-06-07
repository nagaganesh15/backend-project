from django.shortcuts import render
import json
from .models import User,Memorygame
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

from django.core.mail import send_mail
from django.conf import settings




@csrf_exempt
def register(request):
    if request.method=="POST":
        try:
            data=json.loads(request.body)
            username=data.get('username')
            email=data.get('email')
            password=data.get('password')
            # username=request.POST.get('username')
            # email=request.POST.get('email')
            # password=request.POST.get('password')
            if not username or not email or not password:
                return JsonResponse({"err":"Fill the Details"})
            elif User.objects.filter(email=email).exists():
                return JsonResponse({"err":"Already Registered"},status=400)
            elif User.objects.filter(username=username).exists():
                return JsonResponse({"err":"Username already exist"},status=300)
            else:
                User.objects.create(username=username,email=email,password=make_password(password))
                # Send a confirmation email
                send_mail(
                    subject='🎮 Welcome to GameZone - Let the Fun Begin!',
                    message=f'''
🎮 Welcome to GameZone!

Hi {username},

We’re thrilled to have you on board! GameZone is your gateway to exciting adventures, challenges, and endless fun.

🎯 Start playing, beat high scores, and enjoy with friends.

Have fun and game on!

Best regards,  
Mullangi Naga Ganesh  
Team GameZone
''',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email],  # <-- Fixed this line
                    fail_silently=False,
                )
                return JsonResponse({"err":"Register Successfull"},status=200)
        except Exception as e:
            return JsonResponse({"err":str(e)},status=500)
    else:
        return JsonResponse({"err":"Give me corrcet Method"})

@csrf_exempt
def loginuser(request):
    if request.method=="POST":
        try:
            data=json.loads(request.body.decode('utf-8'))
            email=data.get('email')
            password=data.get('password')
            if not email or not password:
                return JsonResponse({"err":"Fill the details"})
            try:
                user=User.objects.get(email=email)
            except User.DoesNotExist:
                return JsonResponse({"err":"Does Not Exist"},status=404)
            if check_password(password,user.password):
                return JsonResponse({"succ":"Login Successfull","email":user.email},status=200)
            else:
                return JsonResponse({"err":"Invalid Password"},status=400)
        except Exception as e:
            return JsonResponse({"err":str(e)},status=500)
    else:
        return JsonResponse({'err':"Give correct Method"})
    
@csrf_exempt
def resetpassword(request):
    if request.method=="POST":
        try:
            data=json.loads(request.body)
            email=data.get('email')
            password=data.get('password')
            if not email or not password:
                return JsonResponse({"err":"Fill the details"})
            elif User.objects.filter(email=email).exists():
                user=User.objects.get(email=email)
                user.password=make_password(password)
                user.save()
                return JsonResponse({"succ":"Reset password is Successful"},status=200)
            else:
                return JsonResponse({"err":"First Register"},status=400)
        except Exception as e:
            return JsonResponse({"err":str(e)},status=500)
    else:
        return JsonResponse({"err":"Give Correct Method"})
    

@csrf_exempt
def saveusername(request):
    if request.method=="POST":
        try:
            data=json.loads(request.body)
            email=data.get('email')
            username=data.get('profilename')
            if User.objects.filter(username=username).exists():
                return JsonResponse({"err":"Username is already exists.please change the name"},status=400)
            user=User.objects.get(email=email)
            user.username=username
            user.save()
            return JsonResponse({"succ":"updated Successful"},status=200)
        except Exception as e:
            return JsonResponse({"err":str(e)})
    else:
        return JsonResponse({"err":"Give correct method"})

@csrf_exempt
def getusername(request):
    if request.method=="POST":
        try:
            data=json.loads(request.body)
            email=data.get('email')
            user=User.objects.get(email=email)
            return JsonResponse({"username":user.username,"profileimage":user.profileimage.url if user.profileimage else None,"memoryscore":user.memoryscore,"stonescore":user.stonescore,"guessscore":user.guessscore,"waterscore":user.waterscore,"brickscore":user.brickscore},status=200)
        except Exception as e:
            return JsonResponse({"err":str(e)})
    else:
        return JsonResponse({"err":"Give correct method"})
# @csrf_exempt
# def memoryscore(request):
#     if request.method=="POST":
#         try:
#             data=json.loads(request.body)
#             profilename=data.get('profilename')
#             memoryscore=data.get('memoryscore')
#             memoryproof=data.get('memoryproof')
#             if not memoryscore:
#                 return JsonResponse({"err":"fill the details"})
#             else:
#                 Memory.objects.create(profilename=profilename,memoryscore=memoryscore,memoryproof=memoryproof)
#                 return JsonResponse({"succ":"Updated successful"},status=200)
#         except Exception as e:
#             return JsonResponse({"err":str(e)},status=500)
#     else:
#         return JsonResponse({"err":"Give me correct Method"})


# @csrf_exempt
# def memoryscore(request):
#     if request.method == "POST":
#         try:
#             profileimage=request.FILES.get('profileimage')
#             profilename = request.POST.get('profilename')
#             memoryscore = request.POST.get('memoryscore')
#             memoryproof = request.FILES.get('memoryproof')  # Get file from request.FILES

#             if not memoryscore or not memoryproof:
#                 return JsonResponse({"err": "Fill all details including screenshot"}, status=400)
#             if Memorygame.objects.filter(profilename=profilename).exists():
#                 user=Memorygame.objects.get(profilename=profilename)
#                 user.memoryscore=memoryscore
#                 user.memoryproof=memoryproof
#                 user.save()
#                 return JsonResponse({"succ": "Updated successful"}, status=200)
#             else:
#                 Memorygame.objects.create(
#                     profileimage=profileimage,
#                     profilename=profilename,
#                     memoryscore=memoryscore,
#                     memoryproof=memoryproof
#                 )
#                 return JsonResponse({"succ": "Updated successful"}, status=200)
#         except Exception as e:
#             return JsonResponse({"err": str(e)}, status=500)
#     else:
#         return JsonResponse({"err": "Give me correct Method"}, status=405)
    
@csrf_exempt
def updateprofileimage(request):
    if request.method=="POST":
        try:
            # data=json.loads(request.body)
            # email=data.get('email')
            # username=data.get('profilename')
            email=request.POST.get('email')
            profileimage=request.FILES.get('profileimage')

            user=User.objects.get(email=email)
            user.profileimage=profileimage
            user.save()
            return JsonResponse({"succ":"updated Successful"},status=200)
        except Exception as e:
            return JsonResponse({"err":str(e)})
    else:
        return JsonResponse({"err":"Give correct method"})

@csrf_exempt
def updatememoryscore(request):
    if request.method=="POST":
        try:
            email=request.POST.get('email')
            memoryscore=request.POST.get('memoryscore')
            memoryproof=request.FILES.get('memoryproof')
            if not memoryscore or not memoryproof:
                return JsonResponse({"err":"Fill the details"},status=400)
            user=User.objects.get(email=email)
            user.memoryscore=memoryscore
            user.memoryproof=memoryproof
            user.save()
            return JsonResponse({"succ":"updated Successful"},status=200)
        except Exception as e:
            return JsonResponse({"err":str(e)})
    else:
        return JsonResponse({"err":"Give correct method"})
    

@csrf_exempt
def updatestonescore(request):
    if request.method=="POST":
        try:
            email=request.POST.get('email')
            stonescore=request.POST.get('stonescore')
            stoneproof=request.FILES.get('stoneproof')
            if not stonescore or not stoneproof:
                return JsonResponse({"err":"Fill the details"},status=400)
            user=User.objects.get(email=email)
            user.stonescore=stonescore
            user.stoneproof=stoneproof
            user.save()
            return JsonResponse({"succ":"updated Successful"},status=200)
        except Exception as e:
            return JsonResponse({"err":str(e)})
    else:
        return JsonResponse({"err":"Give correct method"})
    

@csrf_exempt
def updateguessscore(request):
    if request.method=="POST":
        try:
            email=request.POST.get('email')
            guessscore=request.POST.get('guessscore')
            guessproof=request.FILES.get('guessproof')
            if not guessscore or not guessproof:
                return JsonResponse({"err":"Fill the details"},status=400)
            user=User.objects.get(email=email)
            user.guessscore=guessscore
            user.guessproof=guessproof
            user.save()
            return JsonResponse({"succ":"updated Successful"},status=200)
        except Exception as e:
            return JsonResponse({"err":str(e)})
    else:
        return JsonResponse({"err":"Give correct method"})
    

@csrf_exempt
def updatewaterscore(request):
    if request.method=="POST":
        try:
            email=request.POST.get('email')
            waterscore=request.POST.get('waterscore')
            waterproof=request.FILES.get('waterproof')
            if not waterscore or not waterproof:
                return JsonResponse({"err":"Fill the details"},status=400)
            user=User.objects.get(email=email)
            user.waterscore=waterscore
            user.waterproof=waterproof
            user.save()
            return JsonResponse({"succ":"updated Successful"},status=200)
        except Exception as e:
            return JsonResponse({"err":str(e)})
    else:
        return JsonResponse({"err":"Give correct method"})
    

@csrf_exempt
def updatebrickscore(request):
    if request.method=="POST":
        try:
            email=request.POST.get('email')
            brickscore=request.POST.get('brickscore')
            brickproof=request.FILES.get('brickproof')
            if not brickscore or not brickproof:
                return JsonResponse({"err":"Fill the details"},status=400)
            user=User.objects.get(email=email)
            user.brickscore=brickscore
            user.brickproof=brickproof
            user.save()
            return JsonResponse({"succ":"updated Successful"},status=200)
        except Exception as e:
            return JsonResponse({"err":str(e)})
    else:
        return JsonResponse({"err":"Give correct method"})


from django.db.models import Max

def getAllhighestscores(request):
    if request.method=="GET":
        try:
            maxscores=User.objects.aggregate(
                memoryscore=Max('memoryscore'),
                stonescore=Max('stonescore'),
                guessscore=Max('guessscore'),
                waterscore=Max('waterscore'),
                brickscore=Max('brickscore'),
            )
            memoryuser=User.objects.filter(memoryscore=maxscores['memoryscore']).first()
            stoneuser=User.objects.filter(stonescore=maxscores['stonescore']).first()
            guessuser=User.objects.filter(guessscore=maxscores['guessscore']).first()
            wateruser=User.objects.filter(waterscore=maxscores['waterscore']).first()
            brickuser=User.objects.filter(brickscore=maxscores['brickscore']).first()
            memoryarr=[memoryuser.profileimage.url if memoryuser.profileimage else None,memoryuser.username,memoryuser.memoryscore]
            stonearr=[stoneuser.profileimage.url if stoneuser.profileimage else None,stoneuser.username,stoneuser.stonescore]
            guessarr=[guessuser.profileimage.url if guessuser.profileimage else None,guessuser.username,guessuser.guessscore]
            waterarr=[wateruser.profileimage.url if wateruser.profileimage else None,wateruser.username,wateruser.waterscore]
            brickarr=[brickuser.profileimage.url if brickuser.profileimage else None,brickuser.username,brickuser.brickscore]
            return JsonResponse({"memorygame":memoryarr,"stonegame":stonearr,"guessgame":guessarr,"watergame":waterarr,"brickgame":brickarr,},status=200)
        except Exception as e:
            return JsonResponse({"err":str(e)})
    else:
        return JsonResponse({"err":"give correct method"})
    
@csrf_exempt
def getMemoryscores(request):
    if request.method=="GET":
        try:
            user=User.objects.all().order_by('-memoryscore')
            data=[]
            for i in user:
                data.append({
                    'profileimage': i.profileimage.url if i.profileimage else None,
                    'username':i.username,
                    'score':i.memoryscore,
                })
            return JsonResponse({'memoryuser':data},status=200)
        except Exception as e:
            return JsonResponse({"err":str(e)})
    else:
        return JsonResponse({"err":"give me correct method"})

@csrf_exempt
def getStonescores(request):
    if request.method=="GET":
        try:
            user=User.objects.all().order_by('-stonescore')
            data=[]
            for i in user:
                data.append({
                    'profileimage': i.profileimage.url if i.profileimage else None,
                    'username':i.username,
                    'score':i.stonescore,
                })
            return JsonResponse({'stoneuser':data},status=200)
        except Exception as e:
            return JsonResponse({"err":str(e)})
    else:
        return JsonResponse({"err":"give me correct method"})
    

@csrf_exempt
def getGuessscores(request):
    if request.method=="GET":
        try:
            user=User.objects.all().order_by('-guessscore')
            data=[]
            for i in user:
                data.append({
                    'profileimage': i.profileimage.url if i.profileimage else None,
                    'username':i.username,
                    'score':i.guessscore,
                })
            return JsonResponse({'guessuser':data},status=200)
        except Exception as e:
            return JsonResponse({"err":str(e)})
    else:
        return JsonResponse({"err":"give me correct method"})
    

@csrf_exempt
def getWaterscores(request):
    if request.method=="GET":
        try:
            user=User.objects.all().order_by('-waterscore')
            data=[]
            for i in user:
                data.append({
                    'profileimage': i.profileimage.url if i.profileimage else None,
                    'username':i.username,
                    'score':i.waterscore,
                })
            return JsonResponse({'wateruser':data},status=200)
        except Exception as e:
            return JsonResponse({"err":str(e)})
    else:
        return JsonResponse({"err":"give me correct method"})
    

@csrf_exempt
def getBrickscores(request):
    if request.method=="GET":
        try:
            user=User.objects.all().order_by('-brickscore')
            data=[]
            for i in user:
                data.append({
                    'profileimage': i.profileimage.url if i.profileimage else None,
                    'username':i.username,
                    'score':i.brickscore,
                })
            return JsonResponse({'brickuser':data},status=200)
        except Exception as e:
            return JsonResponse({"err":str(e)})
    else:
        return JsonResponse({"err":"give me correct method"})





@csrf_exempt
def getprofileimg(request):
    if request.method=="POST":
        try:
            data=json.loads(request.body)
            email=data.get('email')
            user=User.objects.get(email=email)
            # return JsonResponse({"su":user.username})
            return JsonResponse({"username":user.username,"profileimg":user.profileimage.url if user.profileimage else None},status=200)
        except Exception as e:
            return JsonResponse({"err":str(e)})
    else:
        return JsonResponse({"err":"Give me correct Method"})
    


@csrf_exempt
def sendmessage(request):
    if request.method=="POST":
        try:
            data=json.loads(request.body)
            firstname=data.get('firstname')
            lastname=data.get('lastname')
            email=data.get('email')
            phone=data.get('phone')
            message=data.get('message')
            send_mail(
                    subject='🎮 Welcome to GameZone - Let the Fun Begin!',
                    message=f'''
🎮 Welcome to GameZone!

Hi This is {firstname} {lastname},

Email: {email},

phone Number: {phone}

Message: {message}

Best regards,  
{firstname} {lastname}
''',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=["nagaganesh.mullangi@gmail.com"],  
                    fail_silently=False,
                )
            return JsonResponse({"username":email},status=200)
            # return JsonResponse({"succ":"Message is Sended",'sam':email},status=200)
        except Exception as e:
            return JsonResponse({"err":str(e)})
    else:
        return JsonResponse({"err":"Give me correct method"})