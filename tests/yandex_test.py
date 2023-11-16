import unittest
import requests


class TestYandexUploader(unittest.TestCase):
    def setUp(self):
        self.token = ''
        self.folder_name = 'Test Folder'
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers = {'Authorization': f'OAuth {self.token}'}

    def test_create_folder(self):
        params = {"path": self.folder_name}
        result = requests.put(f'{self.url}', headers=self.headers, params=params)
        self.assertEqual(201, result.status_code)


if __name__ == '__main__':
    unittest.main()