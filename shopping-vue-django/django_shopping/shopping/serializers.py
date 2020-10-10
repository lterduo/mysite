from rest_framework import serializers
from shopping.models import Music
from shopping.models import Book
from shopping.models import SpUser

class MusicSerializer(serializers.ModelSerializer):
   
   class Meta:
       model = Music
       # fields = '__all__'
       fields = ('id', 'song', 'singer', 'last_modify_date', 'created')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

#vue用户管理
class SpUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpUser
        fields = '__all__'