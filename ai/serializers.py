from rest_framework import serializers
from .models import Grocery
# from .serializers import CoordinateSerializers

# 현제 식료품
class GrocerySerializer(serializers.Serializer):
    name = serializers.CharField(required=False, allow_null=True)
    count = serializers.IntegerField(required=False, allow_null=True)
    coordinate = serializers.JSONField(required=False, allow_null=True)
    # coordinates = CoordinateSerializers(many=True, read_only=True)
    # coordinate = serializers.ListField(required=False, allow_null=True)
    # coordinate = serializers.ListField(
    #     child=serializers.CharField()
    # )
    # coordinate = serializers.ListField(
    #     child = serializers.ListField(
    #         child = serializers.FloatField()
    #      )
    # )
    class Meta:
        # model = Grocery
        fields= ('name', 'count', 'coordinate',)



# class CoordinateSerializers(serializers.Serializer):
#     x = serializers.FloatField(many=True, read_only=True)
#     y = serializers.FloatField(many=True, read_only=True)

#     class Meta:
#         model = Coordinate
#         fields = ('x', 'y')


# # class StopOncomingSerialier(serializers.Serializer):
# #     idn = serializers.IntegerField(read_only=True)
# #     buses = BusSerializer(many=True)