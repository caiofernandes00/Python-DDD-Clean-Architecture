from src.domain.product.factory.product_factory import ProductFactory


class TestProductFactory:

    def test_create_product(self):
        # When
        product = ProductFactory().create("type a", "Product 1", 1)

        # Then
        assert hasattr(product, "id")
        assert product.name == "Product 1"
        assert product.price == 1
