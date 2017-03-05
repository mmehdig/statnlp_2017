
import math
import nltk
from collections import Counter

# functions to read the corpus
def read_tagged_sentence(f):
    line = f.readline()
    if not line:
        return None
    sentence = []
    while line and (line != '\n'):
        line = line.strip()
        word, tag = line.split('\t', 2)
        sentence.append( (word, tag) )
        line = f.readline()
    return sentence

def read_tagged_corpus(filename):
    sentences = []
    with open(filename, encoding='utf-8') as f:
        sentence = read_tagged_sentence(f)
        while sentence:
            sentences.append(sentence)
            sentence = read_tagged_sentence(f)
    return sentences


# baseline using NLTK

def find_most_common_tag(tagged_sentences):
    # make a frequency table of the tags occurring in the sentences
    tag_counter = Counter(t for s in tagged_sentences for _, t in s)

    # find the tag with the highest frequency, typically noun
    return tag_counter.most_common(1)[0][0]

def train_nltk_baseline(tagged_sentences):
    # find the most common tag
    most_common_tag = find_most_common_tag(tagged_sentences)

    # make a backoff tagger that always outputs that tag
    backoff_tagger = nltk.DefaultTagger(most_common_tag)

    # finally, build a unigram tagger from the corpus
    return nltk.UnigramTagger(tagged_sentences, backoff=backoff_tagger)



# skeleton for the bigram tagger code


def hmm_train_tagger(tagged_sentences):
    # estimate the emission and transition probabilities
    # return the two probability tables
    pass

def hmm_tag_sentence(tagger_data, sentence):
    # apply the Viterbi algorithm
    # then retrace your steps
    # finally return the list of tagged words
    pass

START = "<DUMMY_START_TAG>"
END = "<DUMMY_END_TAG>"

def viterbi(tagger_data, sentence):
    # make a dummy link with log prob of 0, START tag, and no predecessor
    # current list = [ the dummy link ]
    
    # for each word in the sentence:
    #    previous list = current list
    #    current list = []        
    #    determine the possible tags for this word
    #  
    #    for each tag of the possible tags:
    #       determine the emission log probability of the word for this tag
    #       find the predecessor that gives the highest total log probability,
    #          where the total log probability is the sum of
    #          1) the emission log probability,
    #          2) the log probability of the transition from the tag of the 
    #             predecessor to the current tag,
    #          3) the total log probability of the predecessor
    #       make a new link with this tag and add it to the current list

    # end the sequence with a dummy: the highest-scoring link with the tag END
    pass
    
def retrace(end_link, sentence_length):
    # tags = []
    # link = predecessor of end_link
    # while the tag of the link isn't START:
    #     add the tag of the link to tags
    #     link = predecessor of link
    # reverse the list of tags and return it
    pass


all_sentences = read_tagged_corpus(YOUR_CORPUS)

# divide the sentences into a training and a test part

# train the bigram tagger
# train the baseline tagger

# evaluate the bigram tagger and the baseline

