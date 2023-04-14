import string


class MatchedMismatchedWords:

    def matched_mismatched_words(self, sentence1: str, sentence2:str):
        """
        Para duas frases e devolver uma matriz que tenha as palavras que 
        aparecem em uma frase e não na outra e uma matriz com as palavras em comum.

        :param sentence1: str
        :param sentence2: str

        :return {common_words: list, different_words: list}:
        """  
        
        # Remove a pontuação das frases
        sentence1 = "".join(c for c in sentence1 if not c in string.punctuation)
        sentence2 = "".join(c for c in sentence2 if not c in string.punctuation)

        # Converte as frases em lists de words
        list_sentence1 = sentence1.split()
        list_sentence2 = sentence2.split()

        # Cria duas lists vazias para armazenar as words em comum e diferentes
        common_words = []
        different_words = []

        # Percorre a list de words da primeira frase
        for word in list_sentence1:
            # Se a word aparece na segunda frase, adiciona à list de words em comum
            if word in list_sentence2:
                common_words.append(word)
            # Senão, adiciona à list de words diferentes
            else:
                different_words.append(word)

        # Percorre a list de words da segunda frase
        for word in list_sentence2:
            # Se a word não aparece na primeira frase, adiciona à list de words diferentes
            if word not in list_sentence1:
                different_words.append(word)

        # Retorna uma tupla com as duas listas
        return common_words, different_words
