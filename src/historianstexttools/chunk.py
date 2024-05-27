def chunk(number_of_sentences=1, overlap=0, language='english'):
    pass

def semantic_chunking(documents, language='english'):
    pass

def sentence_chunking(documents, language='english'):
    from nltk.tokenize import sent_tokenize

    sentences = []

    for doc in documents:
        doc_sentences = sent_tokenize(doc, language=language)
        for sentence in doc_sentences:
            sentences.append(sentence)

    return sentences

def wordcount_chunking_without_overlap_and_sentence_breaking(documents, chunk_size):
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


def wordcount_chunking(documents, chunk_size, overlap=0, break_at_sentence=False, language='english') -> list:
    '''Chunks all documents by a specified and static word count. If document ends before chunk size is hit, it ends the chunk at end-of-document.
    overlap: if less than 1 consider as a percentage, if greater than or equal to 1 consider as number of words'''

    if overlap == 0 and break_at_sentence == False:
        return wordcount_chunking_without_overlap_and_sentence_breaking(documents, chunk_size)

    if break_at_sentence == True:
        sentences = sentence_chunking(documents, language=language)

