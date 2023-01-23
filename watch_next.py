# import spacy
import spacy

# Load advanced language model 'en_core_web_md'
nlp = spacy.load('en_core_web_md')

# Function takes 2 parametrs 'description' and list of titles of movies and their descriptions
def next_movie (description, movies):
    similarity = {}
    # Loop create a dictionary with titles as keys() and e similarity between description of 
    # wattched movie and description each movie in list as values()
    for line in movies:
        similarity[line[0]] = nlp(line[1]).similarity(nlp(description))

    # loop check max value of similarities and return their title
    for title in similarity.keys():
        if similarity[title] == max(similarity.values()):
            return title
    
# Variable with description of watched movie
watched_movie = '''
Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''

# Empty list for stor title and description of movies from file
movies = []

# Open file 'movies.txt' with try-except method for avoid crashing program if file don't exist.
file = None
try:
    file = open("movies.txt",'r',encoding='utf - 8')
    # loop read each line in file, strip() in and split() by " :"
    # Then append it to list 'movies'
    for line in file.readlines():
        description = line.strip().split(" :")
        movies.append(description)
 
except FileNotFoundError:
    print("\nFile you try to open does not exist!\n")

finally:
    if file is not None:
        # create variable wich store value of title most similar movie and print it  
        recommendation = next_movie(watched_movie, movies)
        print(f"\nThe most similar movie is - {recommendation}\n")
        file.close()
 
