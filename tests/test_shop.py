"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models.webshop import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def list_of_products():
    book = Product("book", 100, "This is a book", 1000)
    fork = Product("fork", 5, "This is a fork", 10000)
    spoon = Product("spoon", 10, "This is a fork", 50000)
    return [book, fork, spoon]


@pytest.fixture()
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1) == True
        assert product.check_quantity(1000) == True
        assert product.check_quantity(1001) == False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(1) == 'Success'
        assert product.buy(1000) == 'Success'

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        assert cart.add_product(product, 1) == {product: 1}
        assert cart.add_product(product, 1) == {product: 2}
        assert cart.add_product(product, 100) == {product: 102}

    def test_add_product_multiple(self, list_of_products, cart):
        for item in list_of_products:
            cart.add_product(item)
        assert cart.products == {list_of_products[0]: 1, list_of_products[1]: 1, list_of_products[2]: 1}

    def test_remove_product(self, product, cart):
        cart.add_product(product, 100)
        assert cart.remove_product(product, 1) == {product: 99}
        assert cart.remove_product(product, 98) == {product: 1}
        assert cart.remove_product(product, 1) == {}

    def test_remove_product_multiple(self, list_of_products, cart):
        for item in list_of_products:
            cart.add_product(item, 100)
        assert (
                cart.remove_product(list_of_products[1], 1) ==
                {list_of_products[0]: 100, list_of_products[1]: 99, list_of_products[2]: 100}
        )
        assert (
                cart.remove_product(list_of_products[1], 98) ==
                {list_of_products[0]: 100, list_of_products[1]: 1, list_of_products[2]: 100}
        )
        assert (
                cart.remove_product(list_of_products[1], 1) ==
                {list_of_products[0]: 100, list_of_products[2]: 100}
        )

    def test_clear(self, list_of_products, cart):
        for item in list_of_products:
            cart.add_product(item, 100)
        assert cart.clear() == {}

    def test_get_total_price(self, cart):
        pass

    def test_buy(self, cart):
        pass
