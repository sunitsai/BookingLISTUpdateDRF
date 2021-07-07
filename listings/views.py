from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import *
from django.db.models import Q

# Create your views here.


class BookingInfoView(APIView):

    def get(self,request,price=None):
        print("=============ENTER=================")
        pri = request.query_params.get("price")

        if price:
            print("=============1=========")
            book = None
            if pri == "equals":
                print("=============2=========")
                book = BookingInfo.objects.filter(price=price)
            elif pri == "greaterthan":
                print("=============3=========")
                book = BookingInfo.objects.filter(price__gt=price)
            elif pri == "lessthan":
                print("=============4=========")
                book = BookingInfo.objects.filter(price__lt=price)
            if book:
                print("=============5=========")
                serializer = BookingInfoSerializers(book,many=True)
                print("Serailzer 1 ------------->",serializer)
            else:
                print("=============7=========")
                return Response({"message":"Please enter valid price"},status=status.HTTP_404_NOT_FOUND)
            
        else:
            bookall = BookingInfo.objects.all()
            serializer = BookingInfoSerializers(bookall,many=True)
        return Response({'items':serializer.data,'success':True,'message':"Data is fetched"})


    #  def get(self,request,price=None):
    #     print("=============ENTER=================")
    #     pri = request.query_params.get("price")

    #     if price:
    #         print("=============1=========")
    #         book = None
    #         if pri == "equals":
    #             print("=============2=========")
    #             book = BookingInfo.objects.filter(price=price)
    #         elif pri == "greaterthan":
    #             print("=============3=========")
                
    #             book = BookingInfo.objects.filter(price__gt=price)
    #         elif pri == "lessthan":
    #             print("=============4=========")
    #             book = BookingInfo.objects.filter(price__lt=price)
    #         if book:
    #             print("=============6=========")
    #             serializer = BookingInfoSerializers(book,many=True)

    #         else:
    #             print("=============7=========")
    #             return Response({"message":"Please enter valid price"},status=status.HTTP_404_NOT_FOUND)
            
    #     else:
    #         bookall = BookingInfo.objects.all()
    #         serializer = BookingInfoSerializers(bookall,many=True)
    #     return Response({'items':serializer.data,'success':True,'message':"Data is fetched"})