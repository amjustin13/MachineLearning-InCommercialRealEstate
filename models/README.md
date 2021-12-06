# Models

We trained 5 iterations of a model that would allow us to predict the permit type given a general description of the construction permit in string format. The model uses BERT as the core architecture and fine tuned for our use case. The 5 iterations of oour model are:

- boston_bert_rev1: The first iteration of the model that was trained on the Boston dataset. The model is biased because we didn't strip the permit ID from the input training data. 
- boston_bert_rev2: The second iteration of the model that was trained on the Boston dataset. The model is more generalized as the input training data consist only of permit descriptions. 
- Aus_Bos_SF_rev3: The third iteration of the model that was trained on data from Austin, Boston, and San Francisco. We grouped all permit types into 4 categories: electrical, plumbing, building, and mechanical. This model is biased because we didn't randomly choose which data point for training and testing. The first 80% was for training and the last 20% for testing. 
- Aus_Bos_SF_rev4: The fourth iteration of the model that was trained on data from Austin, Boston, San Francisco. We grouped all the permit types into 4 categories: electrical, plumbing, building, and mechanical. We shuffled the data so that the 80/20 split is more random. 
- Aus_Bos_SF_rev5: The fifth iteration of the model that was trained on data from Austin, Boston, San Francisco. We grouped the training data permit types from the previous iteration into two classifcations: during construction and post construction. The building class is during classifcation and the other three are grouped into post construction. 


All the Tensorflow models are in the Drive. The original processed data is located in the Drive and the reorganized data for training can be obtained using a script from file_scripts.py