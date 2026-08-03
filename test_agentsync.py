# test_agentsync.py
"""
Tests for AgentSync module.
"""

import unittest
from agentsync import AgentSync

class TestAgentSync(unittest.TestCase):
    """Test cases for AgentSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AgentSync()
        self.assertIsInstance(instance, AgentSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AgentSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
