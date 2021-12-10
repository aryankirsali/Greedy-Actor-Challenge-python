import json
import itertools

movie_list=[]
#loading the json file and storing its data in movies
with open("movies.json", "r") as file:
  movies=json.load(file)
#The loop below will add the movie names in an empty list named movie_list  
for i in movies:
  movie_list.append(i)
possible_movies=[]
permutations=[]

#Since the comparision cannot start with just 1 movie, we have to take atleast 2 movies to compare. So we start the loop with 2 as its initial value
for i in range(2,len(movies)):
  permutations+=list(itertools.combinations(movie_list,i))
#the loop above will create combinations of movies

possiblities=[]
#This loop takes each permutation and checks if the movies in it satisfies the below conditions or not
for i in permutations:
  sequence=list(i)
  dummy=0
  for j in range(len(sequence)-1):
    current_movie=sequence[j]
    next_movie=sequence[j+1]
    current_movie_start_date=movies[current_movie]["starting_date"]
    current_movie_start_month=movies[current_movie]["starting_month"]
    current_movie_end_date=movies[current_movie]["ending_date"]
    current_movie_end_month=movies[current_movie]["ending_month"]

    next_movie_start_date=movies[next_movie]["starting_date"]
    next_movie_start_month=movies[next_movie]["starting_month"]
    next_movie_end_date=movies[next_movie]["ending_date"]
    next_movie_end_month=movies[next_movie]["ending_month"]

    if next_movie_start_month==current_movie_end_month:
      if next_movie_start_date<=current_movie_end_date:
        dummy=1
      else:
        pass       
  if dummy==0:
    possiblities.append(sequence)


maximum_work=[]
length=0
#possiblities contain all the permutations which satisfied the conditions 
#the below loop will get the length of longest combination
for i in possiblities:
  if len(i)>length:
    length=len(i)
#the loop below will add the combinations with maximum length into an empty list
for i in possiblities:
  if len(i)==length:
    maximum_work.append(i)
print("Actor's Choices are\n")
index=0
#the below loop will print those combinations along with their values from the json file
for i in maximum_work:
  index+=1
  print(f"Choice {index}")
  for j in i:
    movie_name=j
    movie_start=str(movies[j]["starting_date"])+' '+movies[j]["starting_month"]
    movie_end=str(movies[j]["ending_date"])+' '+movies[j]["ending_month"]
    print(f"{movie_name} from {movie_start} to {movie_end}")

print(f"The actor can make maximum {length} crore doing these movies")




















