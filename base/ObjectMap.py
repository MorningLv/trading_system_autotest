# @Time: 2023/8/19 11:37
# @Author: LCC
import time
from selenium.common.exceptions import ElementNotVisibleException


class ObjectMap:
    def element_get(self, driver, locate_type, locator_expression, timeout=10, must_visible=False):
        start_ms = time.time() * 1000
        stop_ms = start_ms + (timeout * 1000)
        for i in range(int(timeout * 10)):
            try:
                element = driver.find_element(by=locate_type, value=locator_expression)
                if not must_visible:
                    return element
                else:
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
            except Exception:
                now_ms = time.time() * 1000
                if now_ms > stop_ms:
                    break
            time.sleep(0.1)
        raise ElementNotVisibleException("元素定位失败，定位方式：" + locate_type + ",定位表达式：" + locator_expression)
