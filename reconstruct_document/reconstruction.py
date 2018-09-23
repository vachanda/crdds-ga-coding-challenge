class Reconstruction:
    def __init__(self, input_path, output, lexicon):
        """
        Initializer
        """
        self.sentences = self._load_input(input_path)
        self.output_path = output
        self.lexicon = self._load_lexicon(lexicon)

    def _load_lexicon(self, lexicon_path):
        """
        Loads the lexicon to memory from file.
        :param lexicon_path: Path to the lexicon file.
        :returns: A lexicon list
        """
        with open(lexicon_path) as lines:
            lexicon = lines.read().splitlines()

        return lexicon

    def _load_input(self, input_path):
        """
        Loads the input document to memory and splits the document sentences based on delimiter('.').
        :param input_path: Path to the input file.
        :return: List of the input document sentences.
        """
        with open(input_path) as lines:
            document_data = lines.read().splitlines()

        sentences = []

        for lines in document_data:
            sentences += lines.split(".")

        return list(filter(None, sentences))

    def _lexicon_lookup(self, word):
        """
        Checks if the word is present in the lexicon.
        :param word: String word of the document.
        :return: True if the word is present.
        """
        return word in self.lexicon

    def _backtrack(self, sentence, length, output):
        """
        Extracts the word array based on the lexicon.
        :param sentence: De-constructed string sentence.
        :param length: Length of the sentence.
        :param output: Output array of words.
        """
        for i in range(length):
            sub_str = sentence[0:i]
            if self._lexicon_lookup(sub_str):
                output += [sub_str]
                if i == length:
                    return
                self._backtrack(sentence[i:], (length - i), output)

    def re_construct(self):
        """
        Re-constructs the document based on the lexicon.
        """
        reconstructed_sentences = ""
        for sentence in self.sentences:
            result = []
            self._backtrack(sentence, len(sentence) + 1, result)
            reconstructed_sentences += " ".join(result)
            reconstructed_sentences += "."

        with open(self.output_path, 'w') as writer:
            writer.write("%s" % reconstructed_sentences)

        return
