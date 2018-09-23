import unittest
from reconstruct_document.reconstruction import Reconstruction
from pathlib import Path


class TestReconstruction(unittest.TestCase):
    def setUp(self):
        self.test_input_path = "test/samples/document.txt"
        self.test_output_path = "test/samples/output.txt"
        self.test_lexicon_path = "test/samples/lexicon_test.txt"
        self.test_lexicon = ["quick", "fox", "jumps", "over", "the", "lazy", "dog", "brown", "wolf"]
        self.test_input_sentence = ["thequickfoxjumpsoverthelazydog"]
        self.test_output_sentence = "the quick fox jumps over the lazy dog"

        self.document_reconstructor = Reconstruction("test/samples/document.txt", "test/samples/output.txt",
                                                     "test/samples/lexicon_test.txt")

    def tearDown(self):
        path = Path(self.test_output_path)

        if path.exists():
            path.unlink()

    def test__load_lexicon(self):
        self.assertListEqual(self.test_lexicon, self.document_reconstructor._load_lexicon(self.test_lexicon_path),
                             "Lexicon load mismatch")

    def test__load_input(self):
        self.assertListEqual(self.test_input_sentence, self.document_reconstructor._load_input(self.test_input_path),
                             "Input load mismatch")

    def test__lexicon_lookup(self):
        self.assertEqual(True, self.document_reconstructor._lexicon_lookup("jumps"),
                         "Lexicon lookup error")
        self.assertEqual(False, self.document_reconstructor._lexicon_lookup("quic"),
                         "Lexicon lookup error")

    def test__backtrack(self):
        test_output = []
        self.document_reconstructor._backtrack(self.test_input_sentence[0], len(self.test_input_sentence[0]) + 1, test_output)

        self.assertListEqual(self.test_output_sentence.split(" "), test_output, "Backtrack output mismatch")

        test_output = []
        self.document_reconstructor._backtrack(self.test_input_sentence[0], len(self.test_input_sentence[0]), test_output)

        self.assertFalse(self.test_output_sentence.split(" ") == test_output, "Backtrack output mismatch")

    def test_reconstruct(self):
        path = Path(self.test_output_path)
        output_sentence = self.test_output_sentence + "."

        self.document_reconstructor.re_construct()

        with open(self.test_output_path) as f:
            lines = f.read()

        self.assertTrue(path.is_file(), "Reconstructed file missing")
        self.assertTrue(lines == output_sentence, "Reconstructed file content mismatch")


if __name__ == "__main__":
    unittest.main()
