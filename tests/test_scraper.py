#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from episodescript import scrape_episode_scripts

class TestScraper(unittest.TestCase):
    def test_scraper(self):
        title, script = scrape_episode_scripts("Elementary", 5, 3)
        self.assertIsNotNone(title)
        self.assertIsNotNone(script)
        self.assertIsInstance(title, type(u""))  # this way, works both on python 2 and 3
        self.assertIsInstance(script, type(u""))
        
        
if __name__ == '__main__':
    unittest.main()
       


