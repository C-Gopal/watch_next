# import libraries
import spacy

movie_just_watched = "Planet Hulk :Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator." 

def watch_next(movie_description):
    """Compare similarity of movie description with the movie descriptions in movies text file and return the recommended movie to watch next"""

    # declare variable to keep track of movie similarity
    movie_similarity = 0

    # load spacy 
    nlp = spacy.load("en_core_web_md")
    movie_to_compare = nlp(movie_description)

    with open("movies.txt", "r+", encoding="utf-8") as movies:
        for next_movie in movies:
            recommendation = nlp(next_movie)
            similarity = recommendation.similarity(movie_to_compare)

            if similarity > movie_similarity:
                movie_similarity = similarity
                recommended_movie = recommendation.text
    
    return recommended_movie

movie_to_watch = watch_next(movie_description = movie_just_watched)  # recommended_movie assigned movie_to_watch

print(f"Don't miss out on your next best movie! Watch it now...\n\n{movie_to_watch}")

