# @Time: 2023/8/19 11:37
# @Author: LCC
import time
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException, NoSuchElementException, \
    StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from common.yaml_config import GetConf


class ObjectMap:
    url = GetConf().get_url()

    def element_get(self, driver, locate_type, locator_expression, timeout=10, must_visible=False):
        start_ms = time.time() * 1000  # 获取当前时间，毫秒
        stop_ms = start_ms + (timeout * 1000)
        for i in range(int(timeout * 10)):  # 循环100次，每次time.sleep(0.1)即0.1秒，一共10秒
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

    def wait_for_ready_state_complete(self, driver, timeout=30):
        start_ms = time.time() * 1000
        stop_ms = start_ms + (timeout * 1000)
        for i in range(int(timeout * 10)):
            try:
                # 获取页面加载状态
                ready_state = driver.execute_script("return document.readyState")
            except WebDriverException:
                # 如果driver出错，执行js失败会直接跳过
                time.sleep(0.03)
                return True
            if ready_state == "complete":
                time.sleep(0.01)
                return True
            else:
                now_ms = time.time() * 1000
                if now_ms > stop_ms:
                    break
                time.sleep(0.1)
        raise Exception("页面在%s秒后仍然没有完全加载完成" % timeout)

    def element_disappear(self, driver, locate_type, locator_expression, timeout=30):
        # 等待页面元素消失
        if locate_type:
            start_ms = time.time() * 1000
            stop_ms = start_ms + (timeout * 1000)
            for i in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        now_ms = time.time() * 1000
                        if now_ms > stop_ms:
                            break
                        time.sleep(0.1)
                except Exception:
                    return True
            raise Exception("元素没有消失，定位方式：" + locate_type + ",定位表达式：" + locator_expression)
        else:
            pass

    def element_appear(self, driver, locate_type, locator_expression, timeout=30):
        # 等待页面元素出现
        if locate_type:
            start_ms = time.time() * 1000
            stop_ms = start_ms + (timeout * 1000)
            for i in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
                except Exception:
                    now_ms = time.time() * 1000
                    if now_ms > stop_ms:
                        break
                    time.sleep(0.1)
            raise ElementNotVisibleException("元素没有出现，定位方式：" + locate_type + ",定位表达式：" + locator_expression)
        else:
            pass

    def element_to_url(self, driver, url, locate_type_disappear=None, locator_expression_disappear=None,
                       locate_type_appear=None, locator_expression_appear=None):
        try:
            driver.get(self.url + url)
            time.sleep(3)
            self.wait_for_ready_state_complete(driver)
            self.element_disappear(driver, locate_type_disappear, locator_expression_disappear)
            self.element_appear(driver, locate_type_appear, locator_expression_appear)
        except Exception as e:
            print("跳转地址出现异常，异常原因：%s" % e)
            return False
        return True

    def element_is_display(self, driver, locate_type, locator_expression):
        try:
            element = driver.find_element(by=locate_type, value=locator_expression)
            return True
        except NoSuchElementException:
            return False

    def element_fill_value(self, driver, locate_type, locator_expression, fill_value, timeout=10):

        element = self.element_appear(driver, locate_type, locator_expression, timeout)
        try:
            element.clear()
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver)
            time.sleep(0.06)
            element = self.element_appear(driver, locate_type, locator_expression, timeout)
            try:
                element.clear()
            except Exception:
                pass
        except Exception:
            pass
        if type(fill_value) is int or type(fill_value) is float:
            fill_value = str(fill_value)
        try:
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver)
            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.ENTER)
                self.wait_for_ready_state_complete(driver)
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver)
            time.sleep(0.06)
            element = self.element_appear(driver, locate_type, locator_expression, timeout)
            element.clear()
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver)
            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.ENTER)
                self.wait_for_ready_state_complete(driver)
        except Exception:
            raise Exception("元素填值失败")

        return True

    def element_click(self, driver, locate_type, locator_expression, locate_type_disappear=None,
                      locator_expression_disappear=None,
                      locate_type_appear=None, locator_expression_appear=None, timeout=30):

        element = self.element_appear(driver, locate_type, locator_expression, timeout)
        try:
            element.click()
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver)
            time.sleep(0.5)
            element = self.element_appear(driver, locate_type, locator_expression, timeout)
            element.click()
        except Exception as e:
            print("元素不可点击", e)
            return False

        try:
            self.element_appear(driver, locate_type_appear, locator_expression_appear)
            self.element_disappear(driver, locate_type_disappear, locator_expression_disappear)
        except Exception as e:
            print("等待元素消失或出现失败", e)
            return False
        return True

    def upload(self,driver,locate_type, locator_expression, file_path):
        element=self.element_get(driver,locate_type,locator_expression)
        return element.send_keys(file_path)

    def switch_win_to_lastest_handle(self,driver):
        window_handles=driver.window_handles
        driver.switch_to.window(window_handles[-1])

    def switch_into_iframe(self,dirver,locate_iframe_type,locator_iframe_expression):
        iframe=self.element_get(dirver,locate_iframe_type,locator_iframe_expression)
        dirver.switch_to.frame(iframe)

    def switch_from_ifame_to_content(self,driver):
        driver.switch_to.parent_frame()