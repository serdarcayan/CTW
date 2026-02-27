"""
{
    "id": 0
    "title": "",
    "source_type": "web",
    "fetch_mode": "manual",
    "duration": 600,
    "url": "",
    "xpaths": [],
    "cache_policy": "save_all",
    "created_at": "2026-02-23T21:12:28.005800"
}
"""


class ContentModel:
    
    DATA_FILE = "data/items.json"
    
    def __init__(self, item):
        self.item = item
        # self.name = ""
        # self.type = ""
        # self.description = ""
        # self.tags = []
        # self.created_at = None
        # self.updated_at = None
        
        with open(self.DATA_FILE, "r") as f:
            self.data = f.read()

    def create(self):
        # Veritabanına kaydetme işlemi burada yapılacak
        print(f"Creating content in the database... {self.item}")
        pass

    def read(self, content_id):
        # Veritabanından içeriği okuma işlemi burada yapılacak
        pass

    def update(self, **kwargs):
        # İçeriği güncelleme işlemi burada yapılacak
        pass

    def delete(self):
        # İçeriği silme işlemi burada yapılacak
        pass
