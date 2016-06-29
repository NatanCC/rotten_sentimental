from rotten_sentimental import Splitter, POSTagger, DictionaryTagger

class Analyzer(object):
    def __init__(self):
        self.splitter = Splitter()
        self.postagger = POSTagger()
        self.dicttagger = DictionaryTagger(['dictionaries/positive.yml', 'dictionaries/negative.yml', 'dictionaries/inc.yml', 'dictionaries/dec.yml', 'dictionaries/inv.yml'])
        
    def rotten_sentimental_analysis(self, review):
        splitted_sentences = self.splitter.split(review)
        pos_tagged_sentences = self.postagger.pos_tag(splitted_sentences)
        dict_tagged_sentences = self.dicttagger.tag(pos_tagged_sentences)
        
        if self.sentiment_score(dict_tagged_sentences) < -1:
            return "negativo"
        elif self.sentiment_score(dict_tagged_sentences) >= 1:
            return "positivo"
        else:
            return "neutro"
    
    def value_of(self, sentiment):
        if sentiment == 'positive': return 1
        if sentiment == 'negative': return -1
        return 0
    
    def sentence_score(self, sentence_tokens, previous_token, acum_score):
        if not sentence_tokens:
            return acum_score
        else:
            current_token = sentence_tokens[0]
            tags = current_token[2]
            token_score = sum([self.value_of(tag) for tag in tags])
            if previous_token is not None:
                previous_tags = previous_token[2]
                if 'inc' in previous_tags:
                    token_score *= 2.0
                elif 'dec' in previous_tags:
                    token_score /= 2.0
                elif 'inv' in previous_tags:
                    token_score *= -1.0
            return self.sentence_score(sentence_tokens[1:], current_token, acum_score + token_score)
        
    def sentiment_score(self, review):
        return sum([self.sentence_score(sentence, None, 0.0) for sentence in review])
    


def analyze_file(file_name):
    analyzer = Analyzer()
    
    with open(file_name, 'r') as input:
        content = input.read().splitlines()

        reviews = map(analyzer.rotten_sentimental_analysis, content)
        return reviews
    


