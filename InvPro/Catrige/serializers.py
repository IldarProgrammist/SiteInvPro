
from rest_framework import serializers


from Catrige.models import CatrigeModel, JurnalCatrige, Catrige


# Список всех моделей картриджей
class CatrigeModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatrigeModel
        fields = '__all__'


# Статусы картриджей
class CatrigeStatusSerializer(serializers.ModelSerializer):
    class  Meta:
        model = JurnalCatrige
        fields = '__all__'


class CatrigeSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Catrige
        fields = '__all__'