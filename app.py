
from flask import Flask, jsonify, request
import pandas as pd
import os
import io

# Define your global DataFrame
traffic_df = None

app = Flask(__name__)

def load_traffic_data():
    global traffic_df
    print("Loading Austin Traffic Data...")
    traffic_df = pd.read_csv("atxtraffic.csv")
    print(f"Loaded {len(traffic_df)} rows into memory.")

@app.route("/")
def index():
    global traffic_df
    sample = traffic_df.head(10).to_dict(orient="records")
    return jsonify(sample)

@app.route("/head")
def tap():
    global traffic_df
    try:
        num = int(request.args.get('count'))
        sample = traffic_df.head(num).to_dict(orient="records")
    except TypeError:
        return f"Please specify the count parameter for the head function to use"
    return jsonify(sample)

@app.route("/shape")
def show_shape():
    global traffic_df
    return f"Dataframe has {traffic_df.shape[0]} rows and {traffic_df.shape[1]} columns"

@app.route("/columns")
def show_columns():
    global traffic_df
    return f"{traffic_df.columns.tolist()}"

@app.route("/uniquevalues")
def unique_column():
    global traffic_df
    try:
        col = request.args.get('col')

        if col not in traffic_df.columns:
            return f"Column '{col}' not found in DataFrame.", 404
    except TypeError:
        return f"Please specify the count parameter for the column name to use"
   
    return jsonify(traffic_df[col].unique().tolist())

@app.route("/uniquecount")
def unique_count():
    global traffic_df
    try:
        col = request.args.get('col')
        if col not in traffic_df.columns:
            return f" column {col} not in dataframe"
    except TypeError:   
       f"Please specify the column name to use"
    return traffic_df[col].nunique()

@app.route("/info")
def show_info():
    global traffic_df

    buffer = io.StringIO()
    traffic_df.info(buf=buffer)  # send output to buffer
    info_str = buffer.getvalue()  # get the string value
    return f"<pre>{info_str}</pre>"  # use <pre> to preserve formatting

@app.route("/describe")
def show_describe():
    global traffic_df
    describe_df = traffic_df.describe(include='all')  # include='all' to cover all column types
    return jsonify(describe_df.to_dict())

@app.route("/filter")
def query():
    global traffic_df
    try:
        col_name = request.args.get('col')
        col_val = request.args.get('col_val')
        if col_name not in traffic_df.columns:
            return f"column {col_name} not in dataframe"
    except TypeError:
        f"Please specify the column name to use"
    try:
        year = request.args.get('year')
    except ValueError:
        return f"year needs to be an integer"
    
    traffic_df['Published Date'] = pd.to_datetime(traffic_df['Published Date'])
    if year is not None:
        year = int(year)
        traffic_df_queried = traffic_df[(traffic_df[col_name]==col_val)&(traffic_df['Published Date'].dt.year==year)]
    else:
        traffic_df_queried = traffic_df[traffic_df[col_name]==col_val]
    return jsonify(traffic_df_queried.to_dict(orient='records'))


        

if __name__ == "__main__": 
    load_traffic_data()  # <- This runs BEFORE the server starts
    app.run(debug=True, host="0.0.0.0", port=8022)
