#Schema files define the structure of the data and the type of the data , schema is nothing but role book of our data
log_schema = {
"timestamp": "datetime",
"level": "string",
"service": "string",
"message": "string",
}
#dataframe=df.astype(log_schema)