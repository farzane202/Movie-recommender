
# Function to suggest movies based on the user's preferred genre
def suggest_movies(preferred_genre, my_movies):
    """Return a list of movies matching the preferred genre."""
    results = []
    
    for title, details in my_movies.items():
        if preferred_genre.lower() in details["genre"].lower():
            results.append(title)
    return results

def main():
    

    my_movies = {
        "Inception": {"genre": "Action, Sci-Fi"},
        "The Dark Knight": {"genre": "Action, Drama"},
        "La La Land": {"genre": "Romance, Musical"},
        "Parasite": {"genre": "Thriller, Drama"},
        "Interstellar": {"genre": "Sci-Fi, Adventure"},
        "The Matrix": {"genre": "Action, Sci-Fi"},
        "Coco": {"genre": "Animation, Family, Musical"},
        "Joker": {"genre": "Thriller, Drama"},
        "Titanic": {"genre": "Romance, Drama"}
    }

    
    print("Welcome to My Personal Movie Recommender!")
    running = True

    while running:
        # Display the main menu
        print("\n1. Get movie suggestions")
        print("2. See all movies in database")
        print("3. Exit")
        user_choice = input("Choose an option: ")

        if user_choice == "1":
            # Get the user's preferred genre
            genre_input = input("Enter your favorite genre: ")
            # Fetch recommendations based on the genre
            recommendations = suggest_movies(genre_input, my_movies)
            if recommendations:
                print("\n We recommend these movies:")
                for movie in recommendations:
                    print(f"- {movie}")
            else:
                print("Sorry, no movies found for this genre.")
        elif user_choice == "2":
            
            print("\n All movies in our database:")
            for movie, details in my_movies.items():
                print(f"{movie} ({details['genre']})")
        elif user_choice == "3":
            # Exit the program
            print("Goodbye! Thanks for using the Recommender ")
            running = False
        else:
           
            print(" Invalid option. Try again!")

# Run the main program
if __name__ == "__main__":
    main()

