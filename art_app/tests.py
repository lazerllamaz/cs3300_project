from django.test import TestCase
from django.urls import reverse
from .models import Item, Inventory

# Create your tests here.

# Test the __str__ method from Item model
class ItemModelTest(TestCase):
    # Create an item for testing
    def setUp(self):
        self.inventory = Inventory.objects.create(title='test inventory')
        self.item = Item.objects.create(id=2, name='Test Item', item_Img='static/images/test_image.png',  quantity=1, item_Type=Item.MATERIAL, inventory=self.inventory)

    # Test that __str__ method gets the item's name
    def test_item_str(self):
        self.assertEqual(str(self.item), 'Test Item')

    # Check that item detail is at right url
    def test_item_detail_url(self):
        response = self.client.get("/items/2/")
        self.assertEqual(response.status_code, 200)


# Test item detail view - does it create/fetch correctly?
class ItemDetailViewTest(TestCase):
    
    #create a test item and inventory
    def setUp(self):  
        self.inventory = Inventory.objects.create(title='test inventory')
        self.item = Item.objects.create(name='Test Item', item_Img='static/images/test_image.png',  quantity=1, item_Type=Item.MATERIAL, inventory=self.inventory)

    #Test that the item exists and it's in the right spot
    def test_item_detail_view(self):
        response = self.client.get(reverse('item-detail', args=[self.item.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'art_app/item_detail.html')
        self.assertContains(response, 'Test Item')