import os
import shutil
import unittest
import tempfile
from picopayments import srv


CP_URL = "http://139.59.214.74:14000/api/"


class TestVirginSetup(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp(prefix="picopayments_test_")
        self.basedir = os.path.join(self.tempdir, "basedir")
        srv.main([
            "--testnet",
            "--basedir={0}".format(self.basedir),
            "--cp_url={0}".format(CP_URL)
        ], serve=False)

    def tearDown(self):
        shutil.rmtree(self.tempdir)

    def test_paths_and_files_created(self):

        # check basedir was created
        self.assertTrue(os.path.exists(self.basedir))

        # check terms created
        terms_path = os.path.join(self.basedir, "testnet.terms")
        self.assertTrue(os.path.exists(terms_path))

        # check database created
        db_path = os.path.join(self.basedir, "testnet.db")
        self.assertTrue(os.path.exists(db_path))

        # check log file created
        log_path = os.path.join(self.basedir, "testnet.log")
        self.assertTrue(os.path.exists(log_path))


if __name__ == "__main__":
    unittest.main()
