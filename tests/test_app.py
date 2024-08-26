"""import unittest
from image_resizer.app import create_app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()

"""
import unittest
from image_resizer.app import create_app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Choose an image file', response.data)  # Updated to check for actual label text

    def test_image_upload_and_resize(self):
        # Create a dummy image file
        from PIL import Image
        import io

        image = Image.new('RGB', (100, 100), color='red')
        img_bytes = io.BytesIO()
        image.save(img_bytes, format='PNG')
        img_bytes.seek(0)

        response = self.client.post('/', data={
            'file': (img_bytes, 'test.png'),
            'width': '200',
            'height': '200'
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Resized Image', response.data)  # Ensure resized image is present

    def test_download_resized_image(self):
        # Create a dummy image file
        from PIL import Image
        import io

        image = Image.new('RGB', (100, 100), color='blue')
        img_bytes = io.BytesIO()
        image.save(img_bytes, format='PNG')
        img_bytes.seek(0)

        # Upload image and resize it
        upload_response = self.client.post('/', data={
            'file': (img_bytes, 'test.png'),
            'width': '50',
            'height': '50'
        })

        self.assertEqual(upload_response.status_code, 200)
        resized_image_base64 = upload_response.data.decode().split('data:image/png;base64,')[1]

        # Test downloading the resized image
        download_response = self.client.get('/download?image=' + resized_image_base64)
        self.assertEqual(download_response.status_code, 200)
        self.assertEqual(download_response.mimetype, 'image/png')

if __name__ == '__main__':
    unittest.main()
