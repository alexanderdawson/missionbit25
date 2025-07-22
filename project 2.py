import csv

# Organized list of movies with title, genres, and rating
movies = [
#    ["0.", "Bullet Train", ["Action", "Comedy", "Thriller"], 7.3],
#   ["1.", "All Quiet on the Western Front", ["Action", "Drama", "War"], 7.8],
#    ["2.", "Top Gun: Maverick", ["Action", "Drama"], 8.3],
#     ["3.", "Pathaan", ["Action", "Adventure", "Drama"], 6.6],
#    ["4.", "Teen Wolf: The Movie", ["Action", "Drama", "Fantasy"], 5.6],
#     ["5.", "The Dark Knight", ["Action", "Crime", "Drama"], 9.0],
#     ["6.", "Inception", ["Action", "Adventure", "Sci-Fi"], 8.8],
#    ["7.", "Spider-Man: No Way Home", ["Action", "Adventure", "Fantasy"], 8.2],
#     ["8.", "Gladiator", ["Action", "Adventure", "Drama"], 8.5],
#     ["9.", "Avengers: Endgame", ["Action", "Adventure", "Drama"], 8.4],
]

row_reader = []
with open('animation.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header if needed
    for row in reader:
        print(row)
        movies.append(row)
print(movies)

def select_movie():
    print("Welcome to the movie selection program!")
    print("Here are the available movies:")
    for movie in movies:
        print(f"{movie[0]} {movie[1]}")
    choice = input("Please enter the number of the movie you want to select: ")
    if choice.isdigit() and int(choice) < len(movies):
        selected_movie = movies[int(choice)]
        print(f"You selected: {selected_movie[2]}")
        print(f"Genres: {(selected_movie[5])}")
        print(f"Rating: {selected_movie[6]}/10")
        return selected_movie
    else:
        print("Invalid choice.")
        return None

selected_movie = select_movie()

if selected_movie:
    rating = float(selected_movie[6])
    print(type(rating))
    if rating >= 7.0:
        print("This movie is rated above 7.0!")
    elif rating >= 6.0:
        print("This movie is rated between 6.0 and 7.0.")
    if rating >= 8.0:
        print("This movie is highly rated!")
    else:
        print("this movie has a average rating.")
    print(f"you selected: {selected_movie[1]}")
    
    while True:
        user_input = input("Do you want to watch a different movie? (yes/no): ").strip().lower()
        if user_input == "yes":
            selected_movie = select_movie()
            if selected_movie:
                rating = float(selected_movie[6])
                if rating >= 7.0:
                    print("This movie is rated above 7.0!")
                elif rating >= 6.0:
                    print("This movie is rated between 6.0 and 7.0.")
                if rating >= 8.0:
                    print("This movie is highly rated!")
                else:
                    print("this movie has a average rating.")
                print(f"you selected: {selected_movie[1]}")
        else:
            break
    
# while True:
#     user_input = input("Do you want to exit the program? (yes/no): ").strip().lower()
#     if user_input == "yes":
#         print("Thank you for using the movie selection program. Goodbye!")
#         break
#     elif user_input == "no":
#         print("You can continue selecting movies.")
#     else:
#         print("Invalid input, please type 'yes' or 'no'.")
#         continue

# calculate_average_rating = sum(movie[6] for movie in movies) / len(movies)
# print(f"The average rating of all movies is: {calculate_average_rating:.2f}/10")

def calculate_average_rating(movies):
    rating_list = []
    for movie in movies: 
        try:
            if movie[6].strip():
                rating = float(movie[6])
                rating_list.append(rating)
        except:
            continue
    return sum(rating_list) / len(rating_list)

avg_rating = calculate_average_rating(movies)
print("Average rating: ", avg_rating)

def show_highest(movies):
    highest_movie = None
    highest_rating = 0
    for movie in movies: 
        try:
            if movie[6].strip():
                rating = float(movie[6])
                if rating > highest_rating:
                    highest_rating = rating
                    highest_movie = movie[1]
        except:
            continue
    if highest_rating:
        print("highest movie: ", highest_movie)
        print("Rating: " , highest_rating)
    else:
        print("No ratings found.")
        print()

show_highest(movies)

def filter_by_genre():
    genre = input("Type a genre to look for: ")
    found = False
    for movie in movies:
        if genre.lower() in movie[5].lower():
            print("Title;", movie[1])
            print("Genres;", movie[5])
            print("Rating;", movie[6])
            Found = True
    if not Found:
        print("No movies found with that genre.")

#filter_by_genre()
