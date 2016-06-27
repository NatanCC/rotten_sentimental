from rotten_sentimental import Splitter, POSTagger, DictionaryTagger

def rotten_sentimental_analysis(review):
    splitter = Splitter()
    postagger = POSTagger()

    splitted_sentences = splitter.split(review)

    pos_tagged_sentences = postagger.pos_tag(splitted_sentences)

    dicttagger = DictionaryTagger(['dictionaries/positive.yml', 'dictionaries/negative.yml', 'dictionaries/inc.yml', 'dictionaries/dec.yml', 'dictionaries/inv.yml'])

    dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)
      
    if sentiment_score(dict_tagged_sentences) < -1:
        return "negativo"
    elif sentiment_score(dict_tagged_sentences) >= 1:
        return "positivo"
    else:
        return "neutro"

def value_of(sentiment):
    if sentiment == 'positive': return 1
    if sentiment == 'negative': return -1
    return 0


def sentence_score(sentence_tokens, previous_token, acum_score):
    if not sentence_tokens:
        return acum_score
    else:
        current_token = sentence_tokens[0]
        tags = current_token[2]
        token_score = sum([value_of(tag) for tag in tags])
        if previous_token is not None:
            previous_tags = previous_token[2]
            if 'inc' in previous_tags:
                token_score *= 2.0
            elif 'dec' in previous_tags:
                token_score /= 2.0
            elif 'inv' in previous_tags:
                token_score *= -1.0
        return sentence_score(sentence_tokens[1:], current_token, acum_score + token_score)

def sentiment_score(review):
    return sum([sentence_score(sentence, None, 0.0) for sentence in review])


def analyze_file(file_name):
    with open(file_name, 'r') as input:
        content = input.read().splitlines()

        reviews = map(rotten_sentimental_analysis, content)
        return reviews

