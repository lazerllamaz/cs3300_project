from django.test import TestCase
from django.urls import reverse
from .models import Item, Inventory

# Create your tests here.

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