from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        # Memuat dataset
        product_catalog = pd.read_excel("data/productCatalog.xlsx")

        # Menerima input dari formulir
        user_input = request.form['product_name']

        # Memetakan nama produk
        mapped_results = map_product_names(user_input, product_catalog)

        # Menampilkan hasil pemetaan
        return render_template('result.html', input=user_input, results=mapped_results)

def preprocess_text(text):
    return str(text).lower()

def map_product_names(user_input, catalog_df, threshold=0.7, new_sku_threshold=0.5, formula_threshold=0.7):
    # Text preprocessing
    user_input_processed = preprocess_text(user_input)
    catalog_df["Processed_Product_Name"] = catalog_df["productSKUCleaned"].apply(preprocess_text)

    # Text embedding using TF-IDF
    vectorizer = TfidfVectorizer()
    catalog_embeddings = vectorizer.fit_transform(catalog_df["Processed_Product_Name"])
    user_embeddings = vectorizer.transform([user_input_processed])

    # Similarity calculation for product names
    similarity_scores = cosine_similarity(user_embeddings, catalog_embeddings)[0]

    # Mapping based on similarity threshold
    mapped_sku_index = similarity_scores.argmax()
    mapped_sku = catalog_df.iloc[mapped_sku_index]['productSKUCleaned']
    similarity_score = similarity_scores[mapped_sku_index]

    # Propose new SKU for low similarity
    if similarity_score < new_sku_threshold:
        mapped_sku = "NEW_SKU"

    return {
        "Mapped_Product_SKU": mapped_sku,
        "Similarity_Score": similarity_score
    }

if __name__ == '__main__':
    app.run(debug=True)
