# import spaCy and load in 'en_core_web_md' mode
import spacy
nlp = spacy.load('en_core_web_md')

# open and read movies.txt file
movies_file = open('movies.txt', 'r')
movies_list = movies_file.readlines()
for i in range(0, len(movies_list)):
    movies_list[i] = movies_list[i].split(":")
    
# def movie_compare which takes 1 arg in form of sample description and compares it with movies from movies.txt file 
# return the title of most similar movie
def movie_compare(sample):
    sample = nlp(sample)
    similarity_level = 0
    movie_id = 0
    for i in range(0, len(movies_list)):
        similarity = nlp(movies_list[i][1]).similarity(sample)
        if similarity > similarity_level:
            similarity_level = similarity
            movie_id = i
    return movies_list[movie_id][0]

# set sample, start function and print result
sample = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him in to space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''

movie_name = movie_compare(sample)
print(movie_name)