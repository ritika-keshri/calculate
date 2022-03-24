from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import sys
import re

# Create your views here.
class Calculate(APIView):
    def post(self, request):
        try:
            status = 400
            data = request.data
            if "input" in data:
                inputData = data["input"]
                
                if bool(inputData):
                    try:
                        result = eval(inputData)
                        message = {"message": result}
                        status = 200
                    except:
                        message = {"message":"Invalid format"}
                        
                else:
                    message = {"message":"input is required"}
                    
            else:
                message = {"message":"input is required"}
        except Exception as e:
            traceBack = sys.exc_info()[2]
            errorMessage = ""
            if hasattr(e, "message"):
                errorMessage = e.message
            else:
                errorMessage = e
            message = {"errorMessage": str(errorMessage) +" " + str(traceBack.tb_lineno)}
            status = 400
        finally:
            return Response(message, status)
    