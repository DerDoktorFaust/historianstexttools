def chunk(number_of_sentences=1, overlap=0, language='english'):
    pass

def semantic_chunking(documents, language='english'):
    pass

def sentence_chunking(documents):
    pass

def wordcount_chunking(documents, chunk_size) -> list:
    '''Chunks all documents by a specified and static word count. If document ends before chunk size is hit, it ends the chunk at end-of-document.'''

    chunked_documents = []

    for doc in documents:
        split_doc = doc.split()
        doc_length = len(split_doc)

        if doc_length > chunk_size:
            beginning = 0

            while beginning < doc_length:
                end = min(beginning + chunk_size, doc_length)
                current_chunk_array = split_doc[beginning:end]
                chunked_documents.append(' '.join(current_chunk_array))
                beginning = end

        else:
            chunked_documents.append(doc)

    return chunked_documents