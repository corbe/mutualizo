
import statistics
import string


class AverageWordsLengthService:

    def average_words_length(self, sentence: str): 

        # Remove a pontuação da frase    
        sentence_without_punctuation = sentence.translate(str.maketrans('', '', string.punctuation))
        
        # Separa a frase em words e calcula o comprimento de cada word
        words = sentence_without_punctuation.split()
        lengths = [len(word) for word in words]    

        # Calcula a média dos comprimentos das words
        average_lengths = statistics.mean(lengths)

        return sentence, average_lengths