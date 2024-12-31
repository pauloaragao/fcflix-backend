import pytest
import unittest
from uuid import UUID, uuid4
from category import Category

class TestCategory(unittest.TestCase):
    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'*"):
            Category()
    
    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(ValueError, match="name must have less than 256 characters"):
            Category("a" * 256)
    
    def test_category_must_be_created_with_id_as_uidd(self):
        category = Category(name="Filme")
        assert isinstance(category.id, UUID)

    def test_created_category_with_default_values(self):
        category = Category(name="Filme")
        assert category.name == "Filme"
        assert category.description == ""
        assert category.is_active is True

    
    def test_category_is_created_as_active_by_default(self):
        category = Category(name="Filme")
        assert category.is_active is True

    def test_category_is_created_with_provided_values(self):
        cat_id = uuid4()
        category = Category("Film", cat_id, "Description Film", False)

        assert isinstance(category.id, UUID)
        assert category.name == "Film"
        assert category.description == "Description Film"
        assert category.is_active is False

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