import re

class TapSearch:
    def __init__(self, text):
        self.text = text
        self.docs = self.extract_docs()
        self.inverted_index = dict()
        self.doc_indexes = dict()
        
    def __repr__(self):
        return str(self.inverted_index)
    
    def __index_doc(self, doc, doc_idx):
        if doc_idx not in self.doc_indexes:
            self.doc_indexes[doc_idx] = doc
            
        clean_doc = re.sub(r'[^\w\s]','', doc)
        clean_doc = clean_doc.lower()
        clean_doc = clean_doc.replace("\r","")
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
                
    def extract_docs(self):
        docs = self.text.split("\n\n")
        return docs
        
    def create_inverse_index(self):
        for idx, doc in enumerate(self.docs):
            self.__index_doc(doc, idx+1)
        return self.docs
    
    def retrieve_dict(self):
        return self.inverted_index
    
    def retrieve_doc_dict(self):
        return self.doc_indexes

    @staticmethod
    def search_term(inverted_index, document_index, term):
#        print('************************')
#        print(inverted_index)
#        print('************************')
#        print(document_index)
        term = term.lower()
        if term in inverted_index:
            print(inverted_index[term])
            term_dict = inverted_index[term]
            result_idx = sorted(term_dict.keys(), key=lambda x: term_dict[x]['frequency'], reverse=True)
            results = []
            print(document_index)
#            print(result_idx)
#            for idx in result_idx:
#                results.append(document_index[idx])
#                print(document_index[idx])
        else:
            results = []
        return results
        
def main():
    test_obj = TapSearch('I am a dog and a very faithful VERY one.\n\nShe is very harmless.\n\nI love this college')
#    ret = test_obj.extract_docs()
    test_obj.create_inverse_index()
#    x = test_obj.retrieve_dict
    x = test_obj.retrieve_dict()
    y= test_obj.retrieve_doc_dict()
    test_obj.search_term(x , y, 'very')
#    print(x)
    
if __name__ == "__main__":
    main()