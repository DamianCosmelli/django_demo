from rest_framework.response import Response
from rest_framework.views import APIView, status
from firstapi import serializer


class Saludos(APIView):

    serializer_class = serializer.SaludosSerializer

    def get(self, request, format=None):
        return Response({'message':'Mensaje de prueba'})

    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hola {name}'
            return Response({'message': message}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
