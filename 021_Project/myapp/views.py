from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from myapp.models import *
from myapp.serializer import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission


class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_staff

class CategoryAPIView(APIView):

    authentication_classes = [JWTAuthentication]
   
    def get_permissions(self):
        """
        Set permissions for the view.
        """
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAuthenticated(),IsStaffUser()]
        return [AllowAny()]

    """
    API view for handling category-related operations.
    """
    def post(self, request):
        """
        Handle POST requests to create a new category.
        """
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def get(self, request, pk=0):
        """
        Handle GET requests to retrieve a specific category by ID.
        """
        print(pk)
        try:
            if pk == 0:
                categories = Category.objects.all()
                serializer = CategorySerializer(categories, many=True)
                return Response(serializer.data)
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=404)
        
    def put(self, request, pk):
        """
        Handle PUT requests to update an existing category.
        """
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=404)
        
    def delete(self, request, pk):
        """
        Handle DELETE requests to delete a category.
        """
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response({'message': 'Category deleted successfully'}, status=204)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=404)
        
class ProductAPIView(APIView):

    authentication_classes = [JWTAuthentication]
   
    def get_permissions(self):
        """
        Set permissions for the view.
        """
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAuthenticated(),IsStaffUser()]
        return [AllowAny()]

    """
    API view for handling product-related operations.
    """
    def post(self, request):
        """
        Handle POST requests to create a new product.
        """
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def get(self, request, pk=0):
        """
        Handle GET requests to retrieve a specific product by ID.
        """
        try:
            if pk == 0:
                products = Product.objects.all()
                serializer = ProductSerializer(products, many=True)
                return Response(serializer.data)
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)
        
    def put(self, request, pk):
        """
        Handle PUT requests to update an existing product.
        """
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)
        
    def delete(self, request, pk):
        """
        Handle DELETE requests to delete a product.
        """
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response({'message': 'Product deleted successfully'}, status=204)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)
        
class ProductByCategoryAPIView(APIView):
    """
    API view for retrieving products by category.
    """
    def get(self, request, category_id):
        """
        Handle GET requests to retrieve products by category ID.
        """
        try:
            products = Product.objects.filter(category_id=category_id)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=404)
        
class ProductSearchAPIView(APIView):
    """
    API view for searching products by name.
    """ 
    def get(self, request):
        """
        Handle GET requests to search products by name.
        """
        query = request.query_params.get('q', '')
        if query:
            products = Product.objects.filter(name__startswith=query)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        return Response({'error': 'No search query provided'}, status=400)
    
class UserRegistrationAPIView(APIView):
    """
    API view for user registration.
    """
    def post(self, request):
        """
        Handle POST requests to register a new user.
        """
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully', 'user_id': user.id}, status=201)
        return Response(serializer.errors, status=400)
    

class CartAPIView(APIView):
    authentication_classes = [JWTAuthentication]
   
    def get_permissions(self):
        """
        Set permissions for the view.
        """
        if self.request.method in ['POST', 'PUT', 'DELETE','GET']:
            return [IsAuthenticated()]
        

    """
    API view for handling cart-related operations.
    """
    def post(self, request):
        """
        Handle POST requests to add a product to the cart.
        """
        user = request.user
        if not user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=401)
        
        # Ensure product with the given ID exists
        product_id = request.data.get('product')
        isExist = Cart.objects.filter(product_id=product_id,user_id=user.id).exists()
        if isExist:
            return Response({'error': 'Product already exists in cart'}, status=400)
        request.data['user'] = user.id
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def get(self, request):
        """
        Handle GET requests to retrieve the user's cart.
        """
        user = request.user
        if not user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=401)
        
        try:
            
            cart_items = Cart.objects.filter(user=user)
            serializer = CartSerializer(cart_items, many=True)
            return Response(serializer.data)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response({'error': 'Cart item not found'}, status=404)