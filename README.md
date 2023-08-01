# A Computational Method to Reveal Psychological Constructs from Text Data
Accompanying Material to Herderich, Freudenthaler, &amp; Garcia (2023): A Computational Method to Reveal Psychological Constructs from Text Data <br>
To the preprint: - insert preprint link -

## Abstract
When starting to formalize psychological constructs, researchers traditionally rely on two distinct approaches: The quantitative approach, which defines 
constructs as part of a testable theory based on prior research and domain knowledge often deploying self-report questionnaires, or the qualitative approach, 
which gathers data mostly in the form of text and bases construct definitions on exploratory analyses. Quantitative research might lead to an incomplete 
understanding of the construct, while qualitative research is limited due to challenges in the systematic processing of data, especially when its 
scale is large. We present a new computational method that combines the comprehensiveness of qualitative research and the scalability of quantitative 
data analysis to define psychological constructs from semi-structured text data. Based on structured questions, participants are prompted to generate 
sentences reflecting the dimensions of the construct of interest. On these sentences, we apply computational methods to calculate embeddings as numerical 
representations of the text, which we then run through a clustering algorithm to arrive at groupings of sentences as psychologically-relevant classes. 
The pipeline includes methods for the measurement and correction of bias introduced by the data generation process, and the assessment of cluster 
validity according to human judgment. We demonstrate the applicability of our method on an example from emotion regulation. Based on short descriptions of 
emotion regulation attempts collected through an open-ended situational judgment test, we use our method to derive classes of emotion regulation strategies.
Our approach shows how machine learning and psychology can be combined to provide new perspectives on the conceptualization of psychological processes.

## Organisation of the repository
The repository is structured according to the steps of the _construct mining pipeline_ as described in the paper and depicted in Figure `CMP.pdf`. Each step of the pipeline corresponds to one jupyter notebook. Outputs of each step are stored in the folders:
* `data`: contains the original data (`strategies_raw.csv`), original sentence embeddings (Step 1), vignette embeddings (Step 3), and masked sentence embeddings (Step 4)
* `bias`: contains the results of item bias measurement (Step 3)
* `evaluation`: contains the results of hyperparameter tuning on UMA and HDBSCAN (Steps 5 and 6)
* `robustness_check`: contains the results of the robustness check of UMAP against different random initializations (Step 7)
* `intrusion`: contains intrusion survey materials (`survey`), raw intrusion survey data (`results`) and intrusion survey analysis results (Step 8)
* `solution`: contains the plot of the final clustering
* `dim_curse`: contains an illustration of the curse of dimensionality as described in the appendix of the paper
* `noise`: contains raw data (`labeled_data`) and results of the analysis of unclassified samples as described in the appendix of the paper
* `plots`: contains plots from the manuscript
* `bonus`: contains plots of a few additional analyses not described in the paper (see notebook `99_bonus-analyses`)


