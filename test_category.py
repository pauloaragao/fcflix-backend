import unittest
from uuid import UUID, uuid4
from category import Category

class TestCategory(unittest.TestCase):
    def test_name_is_required(self):
        with self.assertRaisesRegex(TypeError, "missing 1 required positional argument: 'name'*"):
            Category()
    
    def test_name_must_have_less_than_255_characters(self):
        with self.assertRaisesRegex(ValueError, "name must have less than 256 characters"):
            Category("a" * 256)
    
    def test_category_must_be_created_with_id_as_uidd(self):
        category = Category(name="Filme")
        self.assertEqual(type(category.id), UUID)

    def test_created_category_with_default_values(self):
        category = Category(name="Filme")
        self.assertEqual(category.name, "Filme")
        self.assertEqual(category.description, "")
        self.assertEqual(category.is_active, True)
    
    def test_category_is_created_as_active_by_default(self):
        category = Category(name="Filme")
        self.assertEqual(category.is_active, True)

    def test_category_is_created_with_provided_values(self):
        cat_id = uuid4()
        category = Category("Film", cat_id, "Description Film", False)

        self.assertEquals(category.id, cat_id)
        self.assertEquals(category.name, "Film")
        self.assertEquals(category.description, "Description Film")
        self.assertEquals(category.is_active, False)

    def test_category_representation_str(self):
        cat_id = uuid4
        category = Category("Film", cat_id, "Description Film", False)

        self.assertEqual(str(category),str(category), f"{category.name} - {category.description} [{category.id}] ({category.is_active})")

    def test_category_representation_repr(self):
        cat_id = uuid4
        category = Category("Film", cat_id, "Description Film", False)

        self.assertEqual(repr(category), f"<Category {category.name} ({category.id})>s")

if __name__ == "__main__":
    unittest.main()