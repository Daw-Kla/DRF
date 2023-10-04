from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title, validate_title_no_hello     #two types of validation

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
            view_name='product-detail',
            lookup_field='pk'
    )

    #email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[validate_title_no_hello, validate_title])
    #u dont have to nessecearly overwrite origrinal field 'title'
    #name = serializers.CharField(source='title', read_only=True)
    class Meta:
        model = Product
        fields = [
            #'user',
            'url',
            'edit_url',
            #'email',
            'pk',
            'title',
            #'name',
            'content',
            'price', 
            'sale_price',
            'my_discount'
        ]

    # filed validation method validae_<field name>, i did it in .validators
    # def validate_title(self, value):
    #     #qs = Product.objects.filter(title__iexact=value)     # iexact case isensitive
    #     qs = Product.objects.filter(title__exact=value)     # exact case sensitive
    #     if qs.exists():
    #         raise serializers.ValidationError(f'{value} is already a product name')
    #     return value
    
    
    # exaple of using specific methods and fields
    # def create(self, validated_data):
    #     email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     print(email, obj)
    #     return obj
    #     # or use this
    #     #return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     instance.title = validated_data.get('title')
    #     return super().update(instance, validated_data)
    
    #return path to product
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-update', kwargs={'pk': obj.pk}, request=request)

    def get_my_discount(self, obj):

        #checki if obj is not an instance
        #its only based on the serializer and serializer method field - in this case 'my_discount'
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
        