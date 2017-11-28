#coding:utf-8

class Page(object):

    bbs_url = 'https://mail.qq.com/'

    def __init__(self, selenium_driver, base_url = bbs_url, parent = None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self):
        self.driver.get(self.bbs_url)
        assert self.on_page(), 'Did not land on %s' % self.bbs_url 

    def find_element(self, *loc):

        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open()


    def on_page(self):
        return self.driver.current_url == self.base_url
    def scrip(self, src):
        return self.driver.execute_script(src)
    def current_page(self):
        return self.driver.current_url

    def switch_frame(self, id):
        return self.driver.switch_to.frame(id)