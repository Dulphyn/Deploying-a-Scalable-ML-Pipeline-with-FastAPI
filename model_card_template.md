# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
# Person or organization developing model
The model was developed by Nicolas Valdez.
# Model date
The model was last updated on June 14, 2026.
# Model version
The model version is 1.0.0.
# Model type
The model uses a random forest classifier.

## Intended Use
# Primary intended uses
The model intends to predict if an individual earns more than a $50,000 salary.  
# Primary intended users
The model was developed for educational purposes.
# Out-of-scope use cases
The model was designed with only the census data features in mind.

## Training Data
The model was trained using an extraction of 1994 census income data.
Kohavi, R. (1996). Census Income [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5GP7S.

## Evaluation Data
The model was trained using an extraction of 1994 census income data. The data labels whether income exceeds $50,000 per year.
Kohavi, R. (1996). Census Income [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5GP7S.

## Metrics
_Please include the metrics used and your model's performance on those metrics._
# Model performance measures
The model achieved a precision score of 0.7419, a recall score of 0.6384, and an F1 score of 0.6863.
## Ethical Considerations
The data does not contain personally identifiable information. 
## Caveats and Recommendations
Not all feature values had the same number of samples. Additionally, some feature values has such a small number of samples that the performance values measures on specific slices of certain features do not provide useful information.