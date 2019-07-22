import matplotlib.pyplot as plt

IMAGE_SHAPE = (28, 28)


def show_features(features, title):
    plt.imshow(features.reshape(IMAGE_SHAPE), cmap="gray")
    plt.title(title)
    plt.show()
