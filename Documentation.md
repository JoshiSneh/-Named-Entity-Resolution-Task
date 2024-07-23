# Document your solution here

  - **Data Preprocessing:** Steps and methods used to clean and standardize the data.
  - **Matching Algorithm:** Description of the algorithm used for entity resolution, including any models or libraries utilized.
  - **Analysis:** Examples of correct and incorrect matches, and an analysis of why mismatches occurred.
  - **Challenges:** Discussion of any challenges faced and the solutions implemented to overcome them.
  
  
# Entity Matching : Amazon and Flipkart Products

1) Data Preprocessing:

   --> Loaded the given dataset using the pandas library by read_csv() method
   --> Checked the information about the dataset by .info() method. It gave the all the information about the dataset including the missing values for each column.
   --> Checked for the duplicate values in dataset using .duplicated() method and null values with the isnull() method.
   --> Dropped 'crawl_timestamp', 'product_url', 'is_FK_Advantage_product', 'product_rating', 'overall_rating' columns from both the dataset as they were irrelevant for the final product matching.
   --> Dropped the missing values from the "image","description","brand","product_specifications" columns from both the dataset using the dropna() method.
   --> Calculated the mean values of the "retail_price" column and replaced it with the missing values of the "retail_price" column and same for the "discount_price" column
   --> Defined a pre_processing function for normalizing the text of "product_name", "brand", and "description" columns that include lower casing the text, removing the special character and removing the white spaces.
   --> Defined a normalize_category function for normalizing the text and return the main category of the product from the category tree.
   
2) Matching Algorithm:
   
   --> For the product matching from both the dataset a function is defined i.e matching_product that accpet both the dataset as a input and return a list of matched products from both of the dataset.
   --> Used a fuzzywuzzy libray which is used for the string/fuzzy matching. It uses Levenshtein Distance to calculate the distance between sequences and match the string by giving a score b/w the two matched string.
   --> How Algorithm works?
       
       : Iterated through the Amazon Dataset and extracted relevant attributes like "product_description", "brands", "retail_price", and "product_category_tree". Here "product_description" is a combination of the "product_name" and "description" for the better entity matching from both the datasets.
       
       : Using the extracted attributes, the algorithm filtered the flipkart dataset and stored the filtered dataset in to "filtered_flipkart" variable. The attributes for the filteration of the data are - "brand", "retail_price", and "product_category_tree".
       
       : Algorithm will proceed to the next step (next amazon product) if the filtered data remains empty.
       
       : The algorithm uses the fuzzywuzzy library for the fuzzy matching. There is a method "process.extractOne" which find the one best match for the Amazon product within the filtered Flipkart dataset.
       
       : "process.extractone" method returns a tuple which contains the best matched string from the flipkart filtered dataset, the similarty score of both the string how close they match, and the index of the matched string.
       
       : Now, we check for the extact mach i.e a similarity score of 100, if the score is 100 then the algorithm retrieves the matched product details from the flipkart dataset using the iloc method which searched the records based on the index.
       
       : At last we returned the list of the product matched from both the datasets.
       
     --> Created a new CSV file for the matched products which contains the uniq_id of product from both the dataset and the product name.
     
3) Analysis of the Match Product:

   --> Example from the Amazon Dateset:
       
       Name: FabHomeDecor Fabric Double Sofa Bed
       Category: Furniture
       Price: 32143
       Description: FabHomeDecor Fabric Double Sofa Bed (Finish Color - Leatherette Black Mechanism Type - Pull Out) Price: Rs. 22,646 • Fine deep seating experience • Save Space with the all new click clack Sofa Bed • Easy to fold and vice versa with simple click clack mechanism • Chrome legs with mango wood frame for long term durability • Double cushioned Sofa Bed to provide you with extra softness to make a fine seating experience • A double bed that can easily sleep two,Specifications of FabHomeDecor Fabric Double Sofa Bed (Finish Color - Leatherette Black Mechanism Type - Pull Out) Installation & Demo Installation & Demo Details Installation and demo for this product is done free of cost as part of this purchase. Our service partner will visit your location within 72 business hours from the delivery of the product. In The Box 1 Sofa Bed General Brand FabHomeDecor Mattress Included No Delivery Condition Knock Down Storage Included No Mechanism Type Pull Out Type Sofa Bed Style Contemporary & Modern Filling Material Microfiber.
       
    --> Example from the Flipkart Dateset:
       
       Name: FabHomeDecor Fabric Double Sofa Bed
       Category: Furniture
       Price: 32157.0
       Description: FabHomeDecor Fabric Double Sofa Bed (Finish Color - Leatherette Black Mechanism Type - Pull Out) Price: Rs. 22,646 • Fine deep seating experience • Save Space with the all new click clack Sofa Bed • Easy to fold and vice versa with simple click clack mechanism • Chrome legs with mango wood frame for long term durability • Double cushioned Sofa Bed to provide you with extra softness to make a fine seating experience • A double bed that can easily sleep two,Specifications of FabHomeDecor Fabric Double Sofa Bed (Finish Color - Leatherette Black Mechanism Type - Pull Out) Installation & Demo Installation & Demo Details Installation and demo for this product is done free of cost as part of this purchase. Our service partner will visit your location within 72 business hours from the delivery of the product. In The Box 1 Sofa Bed General Brand FabHomeDecor Mattress Included No Delivery Condition Knock Down Storage Included No Mechanism Type Pull Out Type Sofa Bed Style Contemporary & Modern Filling Material Microfiber.
       
    Attributes Comparison:

    Name: The product names are identical, which is a strong reason that they are the same product.
    Category: Both the products fall under the same category.
    Price: The prices are almost identical (32143 on Amazon vs. 32157.0 on Flipkart).
    Description: Both product descriptions are identical.
    
    

4) Challenges Faced:
   
    --> Challenge regarding the data quality: There were inconsistency in the data like missing values, hierarchical category tree which can lead to the incorrect matching. Solved this problem byimplementing data cleaning steps to normalize and standardize the data across both the datasets. Extract the main category of the product from the "product_category_tree". 
    