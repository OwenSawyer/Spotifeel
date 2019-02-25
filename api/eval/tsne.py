import numpy as np
import matplotlib.pyplot as plt
from time import time
from matplotlib import offsetbox
from sklearn import datasets, manifold

def plot_embedding(X, title=None):
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)

    plt.figure(figsize=(15,15))
    ax = plt.subplot(111)
    for i in range(X.shape[0]):
        plt.text(X[i, 0], X[i, 1], str(digits.target[i]),
                 color=plt.cm.Set1(y[i] / 10.),
                 fontdict={'weight': 'bold', 'size': 9})

    if hasattr(offsetbox, 'AnnotationBbox'):
        shown_images = np.array([[1., 1.]])  # just something big
        for i in range(digits.data.shape[0]):
            dist = np.sum((X[i] - shown_images) ** 2, 1)
            if np.min(dist) < 4e-3:
                # don't show points that are too close
                continue
            shown_images = np.r_[shown_images, [X[i]]]
            imagebox = offsetbox.AnnotationBbox(
                offsetbox.OffsetImage(digits.images[i], cmap=plt.cm.gray_r),
                X[i])
            ax.add_artist(imagebox)
    plt.xticks([]), plt.yticks([])
    if title is not None:
        plt.title(title)
        plt.savefig('tsne_tsne_test.png')


if __name__ == '__main__':

    digits = datasets.load_digits(n_class=6)
    X = digits.data
    y = digits.target
    n_samples, n_features = X.shape
    n_neighbors = 30

    t0 = time()
    tsne = manifold.TSNE(n_components=2, init='pca', random_state=1, method='barnes_hut', n_iter=1000, verbose=20)
    Xts = tsne.fit_transform(X)
    plot_embedding(Xts, title="t-SNE visualization of MNIST digits 0-5")
    t1 = time()
    dts = t1 - t0

    print('TIME: ' + str(dts))
