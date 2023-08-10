from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SignupSerializer,LoginSerializer
from django.contrib.auth import authenticate

# Create your views here.

@api_view(['POST'])
def servertest(request):
        if request.method == "POST":
            return Response({
                'status': 200,
                'message': 'working Django server'
            })

@api_view(['POST'])
def register(request):
    try:
        data = request.data
        # print(data) #  print in console
        serializer = SignupSerializer(data = data)
        if serializer.is_valid():
             serializer.save()
             return Response({
             'status': True,
             'message': 'User created successfull',
             'data': serializer.data
             })         
        return Response({
             'status': False,
             'message': 'invalid user details',
             'data': serializer.errors
        })  
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': 'please signup again'
    })

@api_view(['POST'])
def login(request ,format=None):
    try:

        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
             email_db = serializer.data.get('email')
             password_db = serializer.data.get('password')
             user = authenticate(request,email=email_db,password=password_db)
             if user is not None:

                return Response({

                     'status': True,
                     'message': 'User login successfull',
                     'data': serializer.data,

                     }) 
             else:
                return Response({
                    'status': False,
                    'message': 'User email or password incurrect',
                    'data': serializer.errors
                    })
    except Exception as e:
         print(e) 
    return Response({
        'status': False,
        'message': 'please login again'
    })