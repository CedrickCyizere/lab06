import os
import pandas as pd
from collections import defaultdict

def create_term_document_matrix(directory):
    # Initialize a defaultdict of type int
    term_document_matrix = defaultdict(int)

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Open each file
        with open(os.path.join(directory, filename), 'r') as f:
            # Read the file content
            content = f.read()
            # Split the content into words
            words = content.split()
            # Iterate over all words
            for word in words:
                # Increment the count of the word in the term-document matrix
                term_document_matrix[(word, filename)] += 1

    # Convert the defaultdict to a pandas DataFrame and pivot it
    df = pd.DataFrame(list(term_document_matrix.items()), columns=['term_file', 'count'])
    df[['term', 'file']] = pd.DataFrame(df['term_file'].tolist(), index=df.index)
    df = df.pivot(index='term', columns='file', values='count').fillna(0)

    return df

# Use the function
df = create_term_document_matrix('/cedrickcyizere/a6')
print(df)
