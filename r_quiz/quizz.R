seaflow <- read.csv(file="assignment5/seaflow_21min.csv", header=TRUE, sep=",")

#Q1 and Q2
summary(seaflow)

#Q3
library(caret)
inTrain <- createDataPartition(seaflow$pop, p=0.50, list=FALSE)
training <- seaflow[inTrain,]
testing <- seaflow[-inTrain,]

#Q4
library(ggplot2)
ggplot(training, aes(x=pe,y=chl_small)) + geom_point(aes(colour = pop))

#Q5, Q6 and Q7
library(rpart)
fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
model <- rpart(fol, method="class", data=training)
print(model)

#Q8
testpredict <- predict(model, testing, type="class")
testsame <- testpredict == testing$pop
sum(testsame)/length(testpredict)

#Q9
library("randomForest")
model <- randomForest(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small, data=training)
forestpredict <- predict(model, testing, type="class")
forestsame <- forestpredict == testing$pop
sum(forestsame)/length(forestpredict)

#Q10
importance(model)

#Q11
library("e1071")
model <- svm(fol, data=training)
epredict <- predict(model, testing, type="class")
esame <- epredict == testing$pop
svmorg<-sum(esame)/length(epredict)
svmorg

#Q12
table(pred = testpredict, true = testing$pop)
table(pred = forestpredict, true = testing$pop)
table(pred = epredict, true = testing$pop)

#Q13
ggplot(training,aes(time,fsc_small)) + geom_point()
ggplot(training,aes(time,fsc_perp)) + geom_point()
ggplot(training,aes(time,fsc_big)) + geom_point()
ggplot(training,aes(time,pe)) + geom_point()
ggplot(training,aes(time,chl_small)) + geom_point()
ggplot(training,aes(time,chl_big)) + geom_point()

#Q14
clean<-seaflow[seaflow$file_id!=208,]
inTrain <- createDataPartition(clean$pop, p=0.50, list=FALSE)
ctraining <- clean[inTrain,]
ctesting <- clean[-inTrain,]

fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
model <- svm(fol, data=ctraining)
cepredict <- predict(model, ctesting, type="class")
cesame <- cepredict == ctesting$pop
svmnew<-sum(cesame)/length(cepredict)
svmnew-svmorg
