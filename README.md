# Capstone_Skin_Cancer
## Repository For Skin Cancer Project

### Overview
This project will employ machine learning techniques, including creation, training, and testing of methods image identification and commensurate classification of the seven most common types of skin cancer.  

The first step of the project will create, and then optimize, a convolution neural network for the image classification from the image training (and test) set.  After optimizing parameters for the CNN, I will apply a variety of pre-trained image classification models for example (but not limited to) VGG, ResNet, ShuffleNet V2, and MobileNet V2.

After the best (highest test accuracy) model is determined, I will prepare the model for implementation.

### Area of Interest
The choice of topic of skin cancer was motivated by a recent and personal experience with skin.  My personal experience reinforced the significance of early and efficient diagnosis.

Additionally, skin cancer affects 1 in 5 Americans in their lifetimes.  In the specific case of melanoma, which is included as a class in the classification, early diagnosis results in better than 99 percent recovery.  If the melanoma is left untreated (resulting presumably for lack of diagnosis) and the melanoma spreads to the lymph nodes, recovery falls to 74 percent.  If the melanoma further progresses to metastasis, survival rates fall to 34 percent.

The statistics above show the importance and benefit of early diagnosis.

This projects focus on identification, rather than a purely diagnostic model, was decided on two factors.  First, a dataset describing a lack of cancer, is difficult to model.  In other words, a no cancer diagnosis is a lack of information and it is impractical to model an absence of information.

### Practical Implications of Early Identification

Since healthcare and treatment of skin cancer, as with all medical treatments, is a limited resource, identification of the types of skin cancer allows for better prioritization of patients and more efficient use of resources.  More concretely, a suggested pre-diagnosis could allow medical care practitioners to prioritize skin legions suspected of being of a more dangerous type prioritized access to diagnosis by a healthcare partitioner.


Early identification of cancer types, and the associated p-value associated with the classification, also implicitly suggests a partial diagnostic model.

### Data Set To Be Used

The image dataset to be used for modeling is the HAM10000.  This dataset can be found at:

https://www.kaggle.com/datasets/surajghuwalewala/ham1000-segmentation-and-classification

This dataset contains 10,000+ images of skin cancer legions and a associated CSV file with classification labels for each of 7 types of skin cancers:

1. Actinic keratoses and intraepithelial carcinoma / Bowen's disease (AKIEC),
2. basal cell carcinoma (BCC),
3. benign keratosis-like lesions (solar lentigines / seborrheic keratoses and lichen-planus like keratoses, BKL),
4. dermatofibroma (DF),
5. melanoma (MEL),
6. melanocytic nevi (NV)
7. vascular lesions (angiomas, angiokeratomas, pyogenic granulomas and hemorrhage, VASC)

Since these 7 types vary considerably in their perniciousness (for example, melanoma (type 4, MEL) is considerably more dangerous than benign keratosis-like lesions (type 3, BKL)), this further reinforces the significance of proper identification.











