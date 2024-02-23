from rest_framework import serializers
from .models import Business
from .models import Capital
from .models import Income
from  .models import Growth
from .models import Staff , BusinessStaff, ConnectToBusiness , BusinessPartnerShip
from .models import Comparison , UserBusinessInterests ,BusinessLike,BusinessComment,BusinessTag , BusinessFollower

class BusinessSerializer (serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

class UserBusinessInterestSerializer (serializers.ModelSerializer):
    class Meta:
        model = UserBusinessInterests
        fields = '__all__'

class BusinessFollowerSerializer (serializers.ModelSerializer):
    class Meta:
        model = BusinessFollower
        fields = '__all__'


class CapitalSerializer (serializers.ModelSerializer):
    class Meta:
        model = Capital
        fields = '__all__'

class IncomeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

class GrowthSerializer ( serializers.ModelSerializer):
    class Meta :
        model = Growth
        fields = '__all__'

class StaffSerializer (serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
class ComparisonSerializer (serializers.ModelSerializer):
    class Meta:
        model = Comparison
        fields = '__all__'

class BusinessLikeSerializer (serializers.ModelSerializer):
    class Meta:
        model = BusinessLike
        fields = '__all__'

class BusinessCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessComment
        fields = '__all__'

class BusinessTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessTag
        fields = '__all__'

class BusinessStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessStaff
        fields = '__all__'

class BusinessPartnerShipSerializer(serializers.ModelSerializer):
    class Meta:
        modle = BusinessPartnerShip
        fields = '__all__'

class ConnectToBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectToBusiness
        fields = '__all__'