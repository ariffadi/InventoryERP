from repositories.category_repository import CategoryRepository


class CategoryService:

    def __init__(self):
        self.repository = CategoryRepository()

    def get_all_categories(self):
        return self.repository.get_all()

    def get_category(self, category_id):
        return self.repository.get_by_id(category_id)

    def get_category_by_name(self, nama):
        return self.repository.get_by_name(nama)