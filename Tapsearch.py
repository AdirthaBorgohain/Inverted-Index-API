import re

class TapSearch:
    def __init__(self, text):
        self.text = text
        self.docs = self.extract_docs()
        self.inverted_index = dict()
        self.doc_indexes = dict()
        
    def __repr__(self):
        return str(self.inverted_index)
    
    def extract_docs(self):
        docs = self.text.split("\n\n")
        return docs
    
    def __index_doc(self, doc, doc_idx):
        if doc_idx not in self.doc_indexes:
            self.doc_indexes[doc_idx] = doc
            
        clean_doc = re.sub(r'[^\w\s]','', doc)
        clean_doc = clean_doc.lower()
        terms = clean_doc.split(' ')
        
        for term in terms:
            if term in self.inverted_index:
                if doc_idx in self.inverted_index[term]:
                     self.inverted_index[term][doc_idx]["frequency"] += 1
                else:
                    self.inverted_index[term][doc_idx] = { "frequency": 1 }
            else:
                temp_dict = {
                        doc_idx: { "frequency" : 1 }
                    }
                self.inverted_index[term] = temp_dict
    
    def search_term(self, term):
        term = term.lower()
        if term in self.inverted_index:
            print(self.inverted_index[term])
            term_dict = self.inverted_index[term]
            result_idx = sorted(term_dict.keys(), key=lambda x: term_dict[x]['frequency'], reverse=True)
        for idx in result_idx:
            print(self.doc_indexes[idx])
        
    def create_inverse_index(self):
        for idx, doc in enumerate(self.docs):
            self.__index_doc(doc, idx+1)
    
    def retrieve_dict(self):
        return self.inverted_index
        
def main():
    test_obj = TapSearch('I am a dog and a very faithful VERY one.\n\nShe is very harmless.\n\nI love this college')
#    ret = test_obj.extract_docs()
    test_obj.create_inverse_index()
#    x = test_obj.retrieve_dict
    test_obj.search_term('very')
#    print(x)
    
if __name__ == "__main__":
    main()