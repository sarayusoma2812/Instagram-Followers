# Loading Dataset
install.packages("expss")
library(expss)

install.packages("readxl")
library("readxl")

info <- read_excel("C:\\Users\\sarayu\\Downloads\\top 100 insta followers dataset.xlsx")
print(info)

#Summary Statistics
a <- info$rank
summary(a)
b <- info$influence_score
summary(b)


#most influcenrs containing country
country_table <- table(info$country)
country_table
country_max <- which.max(table(info$country))
country_max
