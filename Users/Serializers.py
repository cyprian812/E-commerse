from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class CustomSerializer(RegisterSerializer):
    productmanager = serializers.BooleanField(default=False)
    cartmanager = serializers.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Call the parent save method to create the user
        user = super().save(*args, **kwargs)

        # Set the custom field based on the validated data
        user.productmanager = self.validated_data.get('for_product_Manager', False)
        user.cartmanager = self.validated_data.get('for_carmanager', False)
        user.save() # Save the updated user instance
        return user