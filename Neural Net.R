install.packages("neuralnet")
library(neuralnet)
#creating training dataset
TKS = c(20,10,30,20,80,30)
CSS = c(90,20,40,50,50,80)
Placed = c(1,0,0,0,1,1)
#here, you will combine multiple columns or features into a single set of data
df = data.frame(TKS,CSS,Placed)
require(neuralnet)
nn = neuralnet(Placed~TKS+CSS, data = df, hidden = 3, act.fct = "logistic",linear.output = FALSE)
plot(nn)
#creating test set
TKS = c(30,40,85)
CSS = c(85,50,40)
test = data.frame(TKS,CSS)
#prediction using neural network
Predict = compute(nn,test)
Predict$net.result
prob <- Predict$net.result
pred <- ifelse(prob>0.5,1,0)
pred
