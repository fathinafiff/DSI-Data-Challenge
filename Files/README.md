# Product Catalog Mapper
This Flask application is designed to map user-provided product names to similar products in a given catalog. It utilizes TF-IDF (Term Frequency-Inverse Document Frequency) for text embedding and cosine similarity for matching.

##How to Use
1. Ensure you have the required dependencies installed. You can install them using:
```python
pip install -r requirement.txt
```
2. Prepare your product catalog in an Excel file named productCatalog.xlsx and place it in the data directory.
3. Run the Flask application:
```python
python app.py
```
4. Open your web browser and go to http://127.0.0.1:5000/ to access the application.
5. Enter a product name in the provided form on the homepage and submit the form.
6. View the results on the next page, which includes the mapped product SKU and the similarity score.

## Files
- your_app_name.py: The main Flask application file.
- templates/index.html: HTML template for the homepage.
- templates/result.html: HTML template for displaying the mapping results.
- data/productCatalog.xlsx: Sample product catalog in Excel format.
## Dependencies

- Flask
- pandas
- scikit-learn

## Routes
- `/` : Homepage with a form to enter the product name.
- `/result` : Result page displaying the mapped product SKU and similarity score.

## Customization
You can customize the application by modifying the map_product_names function or adjusting similarity thresholds in the result route.
Feel free to explore and adapt this application to fit your specific use case!