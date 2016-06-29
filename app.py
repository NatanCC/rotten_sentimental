from rotten_sentimental import Splitter, POSTagger, DictionaryTagger
import sys
from PyQt4 import QtCore, QtGui
from gui import *

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
    

    def analyze_file(self, file_name):
        with open(file_name, 'r') as input:
            content = input.read().splitlines()
    
            reviews = map(self.rotten_sentimental_analysis, content)
            return reviews
        
    
class AppGUI(QtGui.QTabWidget):
    def __init__(self, parent=None):
        self.analyzer = Analyzer()
        self.review = ""
        self.reviews = []
        
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_main()
        self.ui.setupUi(self)
        
        QtCore.QObject.connect(self.ui.button_analyze,QtCore.SIGNAL("clicked()"), self.normal_analysis)
        QtCore.QObject.connect(self.ui.button_file_analyze,QtCore.SIGNAL("clicked()"), self.file_analysis)
        QtCore.QObject.connect(self.ui.button_open,QtCore.SIGNAL("clicked()"), self.show_file)
        
        
    def show_file(self):
        self.ui.file_text.setText("")
        fd = QtGui.QFileDialog(self)
        self.filename = fd.getOpenFileName()
        from os.path import isfile
        if isfile(self.filename):
            count = 1
            for line in open(self.filename).read().splitlines():
                self.ui.file_text.append(str(count) + " - " + line)
                count += 1
                                         
            
    def file_save(self):
        from os.path import isfile
        if isfile(self.filename):
            file = open(self.filename, 'w')
            file.write(self.ui.editor_window.toPlainText())
            file.close()
    
    def normal_analysis(self):
        result = "positivo"
        self.ui.result_text.setText(result.capitalize())
    
    
    def file_analysis(self):
        results = ["positivo", "neutro", "negativo"]
        
        self.ui.results_text.setText("")
        
        count = 1
        for result in results:
            self.ui.results_text.append(str(count) + "- " + result.capitalize())
            count += 1
        


def main():
    app = QtGui.QApplication(sys.argv)
    myapp = AppGUI()
    myapp.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()    


