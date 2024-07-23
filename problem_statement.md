# Named Entity Resolution Task: Amazon and Flipkart Products

## Objective
Resolve named entities across two different e-commerce databases by matching products from Amazon with corresponding products on Flipkart, considering information from all the columns.

## Task Description

### Dataset Preparation
You are provided with two CSV files containing product information with multiple attributes/columns. Each row represents a product with attributes such as product name, description, price, category, and brand.

### Task Requirements
1. **Data Preprocessing:**
   - Implement preprocessing steps to standardize the data, such as normalizing product names, descriptions, prices, categories, and brands and describe each step properly either in code or the Documentation.

2. **Entity Matching:**
   - Develop an algorithm or use a pre-trained model to match products from Dataset A (Amazon) with Dataset B (Flipkart) based on the available attributes. Detail the approach and algorithm used for matching. This could involve techniques such as string matching, fuzzy matching, and the use of embeddings.
   - BONUS: You can also fetch the images of the products and use them as a feature for product matching.
   
3. **Challenges and Solutions:**
   - Discuss any challenges encountered during the task and how they were addressed.


## Deliverables

### 1. Code
- Provide Python scripts or Jupyter notebooks used for data cleaning, entity matching, and evaluation. Ideally code should be implemented in Solution.ipynb. You can either upload the data on this server and solve it here or download and solve locally and then upload any relevant files.

### 2. Matched Entities File
- Submit a CSV file containing matched products from Amazon and Flipkart.

### 3. Report
- A detailed report covering:
  - **Data Preprocessing:** Steps and methods used to clean and standardize the data.
  - **Matching Algorithm:** Description of the algorithm used for entity resolution, including any models or libraries utilized.
  - **Analysis:** Examples of correct and incorrect matches, and an analysis of why mismatches occurred.
  - **Challenges:** Discussion of any challenges faced and the solutions implemented to overcome them.
- This should be added to Documentation.md

## Evaluation Criteria
- **Technical Skills:** Proficiency in data preprocessing, entity matching algorithms, and model evaluation.
- **Problem-Solving:** Ability to handle real-world data issues and develop effective solutions for entity resolution.
- **Analysis:** Depth of analysis regarding model performance and error cases.
- **Communication:** Clarity and thoroughness of the report, explaining the approach and findings.

This task will test your ability to handle data inconsistencies, apply entity resolution techniques, and effectively communicate your methodology and results in the context of e-commerce product matching.

Make sure to save your files properly before you submit.