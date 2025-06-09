import graphene
from graphene_django.types import DjangoObjectType
from .models import Product, ProductType,DollarPrice


class ProductTypeType(DjangoObjectType):
    class Meta:
        model = ProductType


class ProductType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    price = graphene.String()
    url1 = graphene.String()
    url2 = graphene.String()
    url3 = graphene.String()
    url4 = graphene.String()
    url5 = graphene.String()
    image1=graphene.String()
    image2=graphene.String()
    image3=graphene.String()
    image4=graphene.String()
    image5=graphene.String()
    
    description = graphene.String()
    discount = graphene.String()
    status = graphene.Boolean()
    age = graphene.String()
    type = graphene.String()  # Return just the string from the related type model

    def resolve_type(self, info):
        if self.type:
            return self.type.type  # Return the type string
        return None

    def resolve_name(self, info):
        return self.name

    def resolve_price(self, info):
        return self.price

    def resolve_url1(self, info):
        return self.url1

    def resolve_url2(self, info):
        return self.url2

    def resolve_url3(self, info):
        return self.url3

    def resolve_url4(self, info):
        return self.url4

    def resolve_url5(self, info):
        return self.url5
    def resolve_image1(self, info):
            return self.image1
    def resolve_image2(self, info):
            return self.image2
    def resolve_image3(self, info):
            return self.image3
    def resolve_image4(self, info):
            return self.image4
    def resolve_image5(self, info):
            return self.image5

    def resolve_description(self, info):
        return self.description

    def resolve_discount(self, info):
        return self.discount

    def resolve_status(self, info):
        return self.status

    def resolve_age(self, info):
        return self.age

class DollarPriceType(DjangoObjectType):
    class Meta:
        model = DollarPrice
        fields = ("id", "dollar_price") 
class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType, type=graphene.String(), status=graphene.Boolean())
    product_by_id = graphene.Field(ProductType, id=graphene.ID())
    product_types = graphene.List(ProductTypeType)
    search_products = graphene.List(ProductType, word=graphene.String())
    dollar_price_by_pk = graphene.Field(DollarPriceType, id=graphene.UUID(required=True))
    def resolve_all_products(self, info, type=None, status=None):
        qs = Product.objects.all()
        if type:
            qs = qs.filter(type__type=type)
        if status is not None:
            qs = qs.filter(status=status)
        return qs

    def resolve_product_by_id(self, info, id):
        return Product.objects.get(id=id)

    def resolve_product_types(self, info):
        return ProductType.objects.all()

    def resolve_search_products(self, info, word=None):
        if word:
            print(word)
            return Product.objects.filter(name__icontains=word)
        return Product.objects.none()
    def resolve_dollar_price_by_pk(self, info, id):
        return DollarPrice.objects.get(pk=id)

schema = graphene.Schema(query=Query)
