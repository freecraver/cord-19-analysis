import unittest

import os
from retrieval.resource_loader import download_all, BASE_DIR

class TestDatasetRetrieval(unittest.TestCase):

    def test_download_all(self):
        mod_base_dir = os.path.join("..", BASE_DIR)
        self.assertTrue(os.path.exists(mod_base_dir))
        download_all(mod_base_dir)

        # check allen ai
        allen_ai_dir = os.path.join(mod_base_dir, 'allenai')
        self.assertTrue(os.path.exists(allen_ai_dir))
        self.assertEqual(6, len([name for name in os.listdir(allen_ai_dir) if os.path.isfile(os.path.join(allen_ai_dir, name))]))

        # check elsevier
        elsevier_dir = os.path.join(mod_base_dir, 'elsevier')
        self.assertTrue(os.path.exists(elsevier_dir))
        self.assertEqual(6, len(
            [name for name in os.listdir(elsevier_dir) if os.path.isfile(os.path.join(elsevier_dir, name))]))
        self.assertEqual(1, len(
            [name for name in os.listdir(elsevier_dir) if os.path.isdir(os.path.join(elsevier_dir, name))]))

        # check dimensions
        dimensions_dir = os.path.join(mod_base_dir, 'dimensions')
        self.assertTrue(os.path.exists(dimensions_dir))
        self.assertEqual(1, len(
            [name for name in os.listdir(dimensions_dir) if os.path.isfile(os.path.join(dimensions_dir, name))]))