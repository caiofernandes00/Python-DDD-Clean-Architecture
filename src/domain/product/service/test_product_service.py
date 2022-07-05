from src.domain.product.entity.product import Product
from src.domain.product.service.product_service import ProductService


class TestProductService:

    def test_should_change_products_price(self):
        # When
        product1 = Product("1", "product1", 100)
        product2 = Product("2", "product2", 200)

        ProductService.increase_price([product1, product2], 100)

        assert product1.price == 200
        assert product2.price == 400
