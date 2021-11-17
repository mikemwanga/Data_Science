## Selecting models

Reading from [here](https://machinelearningmastery.com/a-gentle-introduction-to-model-selection-for-machine-learning/)

Model selection is challenging but different approaches exists.

### Model Selection with Cross Validation.

Model selection is the process of choosing one among many candidate models for a predictive modeling problem. There may be many competing concerns when performing model selection beyond model performance, such as complexity, maintainability, and available resources. The two main classes of model selection techniques are **probabilistic measures** and **resampling methods**.

**NOTE:** *There is no such thing as **best** model. All models have existing errors due to the type of datasets. We just need to select a model that is **good enough** to do the prediction.*

In this ideal situation, we would split the data into training, validation, and test sets, then fit candidate models on the training set, evaluate and select them on the validation set, and report the performance of the final model on the test set. 

However most a times this is impractical considering the dynamics of real world datasets.

#### Probabilistic Measures  
Involves analytically scoring a candidate model using both its performance on the training dataset and the complexity of the model. 
Probabilistic model selection measures includeS: 
1. BAC
2. AIC 
3. MDL etc

#### Resampling Measures   
Resampling methods seek to estimate the performance of a model (or more precisely, the model development process) on out-of-sample data. This is achieved by splitting the training dataset into sub train and test sets, fitting a model on the sub train set, and evaluating it on the test set. This process may then be repeated multiple times and the mean performance across each trial is reported.

Resampling methods include;
1. Random train/test splits
2. Cross validation (k-fold)  - split the data into folds and test models. Select model with least cross validation error rate.
3. Bootstrapping