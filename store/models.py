from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    """Model representing a customer.

    Attributes:
        user (User): The associated User model representing the customer.
        name (str): The name of the customer.
        email (str): The email address of the customer.

    Methods:
        __str__(): Returns a string representation of the customer.

    """

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Model representing a product.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        digital (bool): Indicates whether the product is digital or physical.
        image (ImageField): An image representing the product.

    Methods:
        __str__(): Returns a string representation of the product.
        imageURL(): Returns the URL of the product's image.

    """

    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    """Model representing an order.

    Attributes:
        customer (Customer): The associated Customer model representing the customer who placed the order.
        date_ordered (DateTimeField): The date and time when the order was placed.
        complete (bool): Indicates whether the order is complete or not.
        transaction_id (str): The transaction ID associated with the order.

    Methods:
        __str__(): Returns a string representation of the order.
        shipping(): Returns True if the order requires shipping; False otherwise.
        get_cart_total(): Returns the total cost of the items in the order.
        get_cart_items(): Returns the total quantity of items in the order.

    """

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        """Check if the order requires shipping.

        Returns:
            bool: True if the order contains physical products; False otherwise.

        """

        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if not i.product.digital:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        """Get the total cost of the items in the order.

        Returns:
            float: The total cost of the items in the order.

        """

        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        """Get the total quantity of items in the order.

        Returns:
            int: The total quantity of items in the order.

        """

        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    """Model representing an item in an order.

    Attributes:
        product (Product): The associated Product model representing the ordered product.
        order (Order): The associated Order model representing the order the item belongs to.
        quantity (int): The quantity of the ordered product.
        date_added (DateTimeField): The date and time when the item was added to the order.

    Methods:
        get_total(): Calculate the total cost of the item.

    """

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        """Calculate the total cost of the item.

        Returns:
            float: The total cost of the item.

        """

        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    """Model representing a shipping address.

    Attributes:
        customer (Customer): The associated Customer model representing the customer.
        order (Order): The associated Order model representing the order.
        address (str): The shipping address.
        city (str): The city of the shipping address.
        state (str): The state of the shipping address.
        zipcode (str): The ZIP code of the shipping address.
        date_added (DateTimeField): The date and time when the shipping address was added.

    Methods:
        __str__(): Returns a string representation of the shipping address.

    """

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
