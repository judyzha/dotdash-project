import json
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class fakeApi(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path= '/home/yuzhang/Documents/selenium_jars/geckodriver')

    # Test service status of the API endpoint (only one in this case)
    def test_verifyServiceStatus(self):
        self.driver.get("http://localhost/dotdash-project/fake-api-call.php");
        elem = self.driver.find_element_by_tag_name("body")
        content = elem.text
        assert content is not None
        print ("\nURL works fine")

    # Find how many tasks do not have "category" assigned
    def test_tasksNoCategory(self):
        self.driver.get("http://localhost/dotdash-project/fake-api-call.php");
        elem = self.driver.find_element_by_tag_name("body")
        content = elem.text
        j = json.loads(content)
        tc = 0
        for key in j:
            if (key["category"] == ""):
                tc += 1
        print
        print(tc, "tasks do not have \"category\" assigned")

    # Aggregate and print only "task names"
    def test_onlyPrintTaskNames(self):
        self.driver.get("http://localhost/dotdash-project/fake-api-call.php");
        elem = self.driver.find_element_by_tag_name("body")
        content = elem.text
        j = json.loads(content)
        print
        print("task names:")
        for key in j:
            print (key["task name"])

    # Read API response and print tasks in descending "due date" order
    def test_tasksOrderByDueDate(self):
        self.driver.get("http://localhost/dotdash-project/fake-api-call.php");
        elem = self.driver.find_element_by_tag_name("body")
        content = elem.text
        j = json.loads(content)
        print
        print("tasks order by due date desc:")
        lines = sorted(j, key=lambda i: i['due date'], reverse=True)
        for key in lines:
            print(key["task name"])

    # Count and validate the number of tasks
    def test_countValidateTasks(self):
        self.driver.get("http://localhost/dotdash-project/fake-api-call.php");
        elem = self.driver.find_element_by_tag_name("body")
        content = elem.text
        try:
            json_object = json.loads(content)
            tc = 0
            for key in json_object:
                if (key["task name"] != ""):
                    tc += 1
            print(tc, " valid tasks")
        except ValueError:
            return False
        return True

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
