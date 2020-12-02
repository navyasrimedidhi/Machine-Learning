#reading the data.
mydata <- iris
#Showing the data.
mydata
#verifying the relationship between the variables.
plot(mydata)
#installing the packages to split the data.

require(caTools)
#setting the seed to shuffle the data.
set.seed(1234)
#spliting the data 75% and 25% as train and test dataset.
sam <- sample.split(mydata$Species, SplitRatio = .75)
train_data <- subset(mydata, sam == TRUE)
test_data <- subset(mydata, sam == FALSE)
#using linear regression model function.
linmod <- lm(Petal.Length~Petal.Width+Sepal.Length+Sepal.Width,data = train_data)
#Plotting the data of linmod in line graph.
plot(linmod)
#A straight line passing through the point.
abline(linmod, col = 'red')
#predicting the test dataset values.
pmod <- predict(linmod,test_data)
pmod
