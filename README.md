# SGX3 Coding Institute Repo

# Flask Application Routes

This README file summarizes the available API routes in the Flask application, `app.py`.

## Routes

### `/`
- **Method:** GET
- **Description:** Returns the first 10 rows of the `traffic_df` DataFrame as a JSON array.
- **Example Response:**
```json
[
  {
    "Published Date": "2023-01-01T00:00:00",
    "Location": "Some Street",
    "Traffic Count": 100
  }
]
```

### `/head`
- **Method:** GET
- **Description:** Returns a specified number of rows from the head of the `traffic_df` DataFrame as a JSON array.
- **Parameters:**
  - `count` (integer, required): The number of rows to return.
- **Example Request:** `/head?count=5`
- **Example Response:**
```json
[
  {
    "Published Date": "2023-01-01T00:00:00",
    "Location": "Some Street",
    "Traffic Count": 100
  }
]
```

### `/shape`
- **Method:** GET
- **Description:** Returns the dimensions (number of rows and columns) of the `traffic_df` DataFrame.
- **Example Response:** `Dataframe has 1000 rows and 5 columns`

### `/columns`
- **Method:** GET
- **Description:** Returns a list of all column names in the `traffic_df` DataFrame.
- **Example Response:** `['Published Date', 'Location', 'Traffic Count']`

### `/uniquevalues`
- **Method:** GET
- **Description:** Returns a list of unique values for a specified column in the `traffic_df` DataFrame.
- **Parameters:**
  - `col` (string, required): The name of the column.
- **Example Request:** `/uniquevalues?col=Location`
- **Example Response:** `["Downtown", "North Austin", "South Austin"]`

### `/uniquecount`
- **Method:** GET
- **Description:** Returns the count of unique values for a specified column in the `traffic_df` DataFrame.
- **Parameters:**
  - `col` (string, required): The name of the column.
- **Example Request:** `/uniquecount?col=Location`
- **Example Response:** `3`

### `/info`
- **Method:** GET
- **Description:** Returns a formatted string containing information about the `traffic_df` DataFrame, similar to `pandas.DataFrame.info()`.
- **Example Response:** (Pre-formatted text with DataFrame info)

### `/describe`
- **Method:** GET
- **Description:** Returns descriptive statistics for the `traffic_df` DataFrame as a JSON object, similar to `pandas.DataFrame.describe()`.
- **Example Response:**
```json
{
  "Traffic Count": {
    "count": 1000,
    "mean": 500,
    "std": 200,
    "min": 100,
    "25%": 300,
    "50%": 500,
    "75%": 700,
    "max": 900
  }
}
```

### `/filter`
- **Method:** GET
- **Description:** Filters the `traffic_df` DataFrame based on a column value and an optional year, returning matching rows as a JSON array.
- **Parameters:**
  - `col` (string, required): The name of the column to filter by.
  - `col_val` (string, required): The value to filter the column by.
  - `year` (integer, optional): The year to filter by (e.g., `2023`).
- **Example Request:** `/filter?col=Location&col_val=Downtown&year=2023`
- **Example Response:**
```json
[
  {
    "Published Date": "2023-01-01T00:00:00",
    "Location": "Downtown",
    "Traffic Count": 150
  }
]
```

### `/hours`
- **Method:** GET
- **Description:** Filters the `traffic_df` DataFrame to include entries within a specified hour range (inclusive) based on the 'Published Date' column, returning matching rows as a JSON array.
- **Parameters:**
  - `start` (integer, required): The starting hour (0-23).
  - `end` (integer, required): The ending hour (0-23).
- **Example Request:** `/hours?start=9&end=17`
- **Example Response:**
```json
[
  {
    "Published Date": "2023-01-01T10:00:00",
    "Location": "Some Street",
    "Traffic Count": 120
  }
]
```

### `/coords`
- **Method:** GET
- **Description:** Finds traffic data entries within a specified radius (in kilometers) of given latitude and longitude coordinates, returning matching rows as a JSON array.
- **Parameters:**
  - `lat` (float, required): The latitude of the center point.
  - `lon` (float, required): The longitude of the center point.
  - `radius` (float, optional): The radius in kilometers. Defaults to 1 km.
- **Example Request:** `/coords?lat=30.2672&lon=-97.7431&radius=5`
- **Example Response:**
```json
[
  {
    "Published Date": "2023-01-01T00:00:00",
    "Location": "Near Capitol",
    "Traffic Count": 200,
    "Latitude": 30.268,
    "Longitude": -97.745
  }
]
```




