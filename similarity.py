import pandas as pd
from PyUMLS_Similarity import PyUMLS_Similarity

# Define MySQL information that stores UMLS data in your computer
mysql_info = {
    "username": "root",
    "password": "Pass@123",
    "hostname": "localhost",
    "socket": "/var/run/mysqld/mysqld.sock", #/var/run/mysqld/mysqld.sock
    "database": "umls"
}

umls_sim = PyUMLS_Similarity(mysql_info=mysql_info)

# Define CUI pairs
cui_pairs = [
    # ('Renal failure', 'Kidney failure'),
    ('hand', 'skull'),
]

# Define similarity measures
measures = ['lesk', 'res']

# Calculate similarity
similarity_df = umls_sim.similarity(cui_pairs, measures)
print("Similarity Results:")
print(similarity_df)

# Calculate shortest path
shortest_path_df = umls_sim.find_shortest_path(cui_pairs)
print("\nShortest Path Results:")
print(shortest_path_df)

# Calculate least common subsumer (LCS)
lcs_df = umls_sim.find_least_common_subsumer(cui_pairs)
print("\nLeast Common Subsumer (LCS) Results:")
print(lcs_df)

# Define tasks for concurrent execution
tasks = [
    {'function': 'similarity', 'arguments': (cui_pairs, measures)},
    {'function': 'shortest_path', 'arguments': (cui_pairs)},
    {'function': 'lcs', 'arguments': (cui_pairs)}
]

# Run tasks concurrently
results = umls_sim.run_concurrently(tasks)
print("\nConcurrent Task Results:")
print(results)

# Save results to CSV files
similarity_df.to_csv('similarity_results.csv', index=False)
shortest_path_df.to_csv('shortest_path_results.csv', index=False)
lcs_df.to_csv('lcs_results.csv', index=False)

# If you also want to save the concurrent results
results_df = pd.DataFrame(results)
results_df.to_csv('concurrent_results.csv', index=False)

print("Results saved to CSV files.")
