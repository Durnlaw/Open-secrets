import pandas as pd
from sklearn.cluster import KMeans

pac_vote_totals_path = 'C:\\Programming\\repos\\Open-secrets\\data\\sum_pac_vote_data.csv'
pac_vote_totals = pd.read_csv(pac_vote_totals_path, index_col = 'org_name')
print(pac_vote_totals.shape)
pac_vote_totals = pac_vote_totals.drop(['total'], axis = 1)
print(pac_vote_totals.shape)


import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# # create dataset
# X, y = make_blobs(
#    n_samples=150, n_features=2,
#    centers=3, cluster_std=0.5,
#    shuffle=True, random_state=0
# )

# # plot
# plt.scatter(
#    X[:, 0], X[:, 1],
#    c='white', marker='o',
#    edgecolor='black', s=50
# )
# plt.show()



# km = KMeans(
#     n_clusters=3, init='random',
#     n_init=10, max_iter=300,
#     tol=1e-04, random_state=0
# )

# y_km = km.fit_predict(X)


# plt.scatter(
#     X[y_km == 0, 0], X[y_km == 0, 1],
#     s=50, c='lightgreen',
#     marker='s', edgecolor='black',
#     label='cluster 1'
# )

# plt.scatter(
#     X[y_km == 1, 0], X[y_km == 1, 1],
#     s=50, c='orange',
#     marker='o', edgecolor='black',
#     label='cluster 2'
# )

# plt.scatter(
#     X[y_km == 2, 0], X[y_km == 2, 1],
#     s=50, c='lightblue',
#     marker='v', edgecolor='black',
#     label='cluster 3'
# )

# # plot the centroids
# plt.scatter(
#     km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],
#     s=250, marker='*',
#     c='red', edgecolor='black',
#     label='centroids'
# )
# plt.legend(scatterpoints=1)
# plt.grid()
# plt.show()



distortions = []
for i in range(1, 11):
    km = KMeans(
        n_clusters=i, init='random',
        n_init=10, max_iter=300,
        tol=1e-04, random_state=0
    )
    km.fit(pac_vote_totals)
    distortions.append(km.inertia_)

# plot
plt.plot(range(1, 11), distortions, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.show()

#! Thinking 5 min, 7 max