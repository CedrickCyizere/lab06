import os
import pandas as pd
from collections import defaultdict
import sys
import numpy as np

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

def cosine_similarity(A, B):
    dot_product = np.dot(A, B)
    magnitude = np.linalg.norm(A) * np.linalg.norm(B)
    return dot_product / magnitude

def main():
    # Get the directory path from the command line arguments
    directory = sys.argv[1]

    # Create the term-document matrix
    df = create_term_document_matrix(directory)

    # Read the query vector from stdin
    query_vector = np.array([float(x) for x in input().split()])

    # Compute the cosine similarity of the query vector with all document vectors
    similarities = {file: cosine_similarity(query_vector, df[file].values) for file in df.columns}

    # Sort the documents by similarity
    sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)

    # Dump the similarity and document name pairs into stdout
    for file, similarity in sorted_similarities:
        print(f'{similarity} {file}')

if __name__ == '__main__':
    main()
