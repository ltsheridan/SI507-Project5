import unittest
from SI507project5_code import *

class TumblrTest(unittest.TestCase):
    def setUp(self):
        blog_url = 'https://api.tumblr.com/v2/tagged'
        CACHE_DICTION = json.loads(cache_json)
        tumblr_search_params = {"tag":"millenials","limit":"20"}
        tumblr_result = get_data_from_api(blog_url,"Tumblr",tumblr_search_params)
        self.response = tumblr_result['response'][0]
        self.tags = tumblr_result['response'][0]['tags']
        self.blogname = tumblr_result['response'][0]['blog_name']

    def test_tumblr_data1(self):
        self.assertEqual(type(self.response['blog_name']),type(u"s"))

    def test_tumblr_data2(self):
        self.assertEqual(type(self.response),type({}))

    def test_tumblr_data3(self):
        self.assertEqual(self.tags, ['my mom', 'parents', 'millenials', 'emojis'])

    def test_tumblr_data4(self):
        self.assertEqual(self.blogname, 'kerek-the-unhallowed')

    def test_tumblr_data5(self):
        self.assertEqual(type(self.blogname), type('kerek-the-unhallowed'))





if __name__ == "__main__":
    unittest.main(verbosity=2)
