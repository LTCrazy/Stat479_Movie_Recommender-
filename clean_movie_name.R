#ML data cleaning

library(data.table)
library(dplyr)
library(tidyverse)
library(stringr)

movie_mvlens <- fread("./ml-latest-small/movies.csv")

#extract year of each movie and clean movie names
movie_mvlens1 <- movie_mvlens %>% 
  mutate(title = gsub("\\s*\\([^\\)]+\\)", "", title)) %>% 
  mutate(title = sub(", A", "", title)) %>% 
  mutate(title = sub(", The", "", title))

fwrite(movie_mvlens1, file = "./ml-latest-small/movie_mvlens_clean.csv")
  #mutate(year= str_extract(title, pattern = "(.)$"))


