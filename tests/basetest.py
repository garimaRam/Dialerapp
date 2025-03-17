import pytest
from config.driver_setup import get_driver

class BaseTest:
    @pytest.fixture(scope="function",autouse=True)
    def setup(self, request):
        self.driver = get_driver()
        request.cls.driver = self.driver
        yield
        self.driver.quit()
