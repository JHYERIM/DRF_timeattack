from rest_framework import serializers
from article.models import Article

class Articleserializer(serializers.ModelSerializer):
    model = Article
    fields = "__all__"