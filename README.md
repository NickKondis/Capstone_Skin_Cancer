# Capstone_Skin_Cancer
## Repository For Skin Cancer Project

### Overview
This project will employ machine learning techniques, including the creation, training, and testing of methods of image identification and commensurate classification of the seven most common types of skin cancer.  

The first step of the project will create, and then optimize, a convolution neural network for the image classification from the image training (and test) set.  After optimizing parameters for the CNN, I will apply a variety of pre-trained image classification models for example (but not limited to) VGG, ResNet, ShuffleNet V2, and MobileNet V2.

After the best (highest test accuracy) model is determined, I will prepare the model for implementation.

### Area of Interest
The choice of the topic of skin cancer was motivated by a recent and personal experience with skin.  My personal experience reinforced the significance of early and efficient diagnosis.

Additionally, skin cancer affects 1 in 5 Americans in their lifetimes.  In the specific case of melanoma, which is included as a class in the classification, early diagnosis results in better than 99 percent recovery.  If the melanoma is left untreated (resulting presumably for lack of diagnosis) and the melanoma spreads to the lymph nodes, recovery falls to 74 percent.  If the melanoma further progresses to metastasis, survival rates fall to 34 percent.

The statistics above show the importance and benefit of early diagnosis.

This project's focus on identification, rather than a purely diagnostic model, was decided on two factors.  First, a dataset describing a lack of cancer is difficult to model.  In other words, a no cancer diagnosis is a lack of information and it is impractical to model an absence of information.


### Practical Implications of Early Identification

Since healthcare and treatment of skin cancer, as with all medical treatments, is a limited resource, identification of the types of skin cancer allows for better prioritization of patients and more efficient use of resources.  More concretely, a suggested pre-diagnosis could allow medical care practitioners to prioritize skin legions suspected of being of a more dangerous type prioritized access to diagnosis by a healthcare partitioner.


Early identification of cancer types, and the associated p-value associated with the classification, also implicitly suggests a partial diagnostic model.

### Data Set To Be Used

The image dataset to be used for modeling is the HAM10000.  This dataset can be found at:

https://www.kaggle.com/datasets/surajghuwalewala/ham1000-segmentation-and-classification

This dataset contains 10,000+ images of skin cancer legions and an associated CSV file with classification labels for each of the 7 types of skin cancers.  The CSV file uses a binary labeling system (1.0 to indicate the type in the respective feature or 0.0 otherwise). 

Types of skin cancer lesions in the dataset:

1. Actinic keratoses and intraepithelial carcinoma / Bowen's disease (AKIEC),
2. basal cell carcinoma (BCC),
3. benign keratosis-like lesions (solar lentigines / seborrheic keratoses and lichen-planus like keratoses, BKL),
4. dermatofibroma (DF),
5. melanoma (MEL),
6. melanocytic nevi (NV)
7. vascular lesions (angiomas, angiokeratomas, pyogenic granulomas and hemorrhage, VASC)

Since these 7 types vary considerably in their perniciousness (for example, melanoma (type 4, MEL) is considerably more dangerous than benign keratosis-like lesions (type 3, BKL)), this further reinforces the significance of proper identification.


## Updates to project

After evaluating the results of my first neural network model, I noticed a significant data imbalance, with 67% of the dataset consisting of NV (melanocytic nevi). This imbalance skewed the model's predictions, favoring NV, which limited the model's practical utility.

To address this issue, I applied random oversampling to balance the dataset.

Subsequently, I developed a second neural network with additional layers to enhance classification performance. This adjustment led to improved identification of skin lesions.

In parallel, I implemented several pre-trained models, including ResNet50, EfficientNetB0, InceptionV3, VGG16, DenseNet, Xception, and NASNetMobile. However, due to processing time constraints, these models have not yet been fully tested.

Anticipating the results of the pre-trained models' accuracy, I also designed an ensemble classifier. This classifier averages the predictions from each model and classifies based on consensus, aiming to improve overall accuracy. Although all models are included in the code, adjustments may be made based on the performance (accuracy) of each model.


## Further Updates to the Project

After creating several models, some from scratch and some from modifications of large pre-trained models (including an ensemble neural network model), it was determined that the smaller created model gave the best results.  The created models are:

1. A small 13-layer convolution neural network (parameters stored as my_model_nn.keras)
2. A larger 17-layer convolution neural network (parameters stored as my_model_nn_2.keras)
3. Adaptation of pre-trained model ResNET (parameters stored as model_Resnet.keras)
4. Adaptation of pre-trained model EfficientNetB0 (parameters stored as model_Eff.keras)
5. Adaptation of pre-trained model InceptionV3 (parameters stored as model_IncV3.keras)
6. Adaptation of pre-trained model VGG16 (parameters stored as model_VGG16.keras)
7. Adaptation of pre-trained model DenseNet (parameters stored as model_DenseNet.keras)
8. Adaptation of pre-trained model NASNet (parameters stored as model_NASNet.keras)
9. Adaptation of pre-trained model Xception (parameters stored as model_Xcept.keras)
10. Creation of a 3-part ensemble CNN
11. Recreation of a small model

After exhausting multiple model types (created and pre-trained), the final model (listed above as number 11) yielded the best accuracy on the test set and will be used for the deployment.

## Analysis of the Models

I initially expected the larger, pre-trained models to yield the highest accuracy. However, during testing, these models exhibited significant overfitting and performed poorly on the test set. This outcome is likely because these models were originally designed to classify a much broader range of images (ImageNet includes 1000 diverse classes). In contrast, my dataset is limited to just 7 classes, all of which are variations of similar skin lesions. As a result, the pre-trained models struggled to generalize effectively.

Realizing that simpler models might be better suited for this task, I developed a new model and evaluated it using 4-fold cross-validation. The best-performing model during training was saved as model_my_nn_fold_4.keras.

## Implementation of the best model

This model was subsequently deployed as a locally hosted web app for demonstration purposes.

A video demonstration of the app is included in this repository.














