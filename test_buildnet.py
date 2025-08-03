# test_buildnet.py
"""
Tests for BuildNet module.
"""

import unittest
from buildnet import BuildNet

class TestBuildNet(unittest.TestCase):
    """Test cases for BuildNet class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BuildNet()
        self.assertIsInstance(instance, BuildNet)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BuildNet()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
