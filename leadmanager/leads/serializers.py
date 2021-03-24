from rest import serializers
from leads.models import Lead

# Lead serializer
class LeadSerializer(serializers.ModelSerializers):
    class Meta:
        model = Lead
        fields = '__all__'