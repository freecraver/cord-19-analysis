import unittest

import os
from retrieval.resource_loader import download_all, BASE_DIR

class TestDatasetRetrieval(unittest.TestCase):

    def test_download_all(self):
        mod_base_dir = os.path.join("..", BASE_DIR)
        self.assertTrue(os.path.exists(mod_base_dir))
        download_all(mod_base_dir)
        allen_ai_dir = os.path.join(mod_base_dir, 'allenai')
        self.assertTrue(os.path.exists(allen_ai_dir))
        self.assertEqual(6, len([name for name in os.listdir(allen_ai_dir) if os.path.isfile(os.path.join(allen_ai_dir, name))]))