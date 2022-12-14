import joblib
def predict(data):
    # get a new test image
    test_image = skimage.data.astronaut()
    test_image = skimage.color.rgb2gray(test_image)
    test_image = skimage.transform.rescale(test_image, 0.5)
    test_image = test_image[:160, 40:180]
    plt.imshow(test_image, cmap='gray')
    plt.axis('off');

    #  Create a window that iterates over patches of this image, and compute HOG features for each patch:
    def sliding_window(img, patch_size=positive_patches[0].shape,istep=2, jstep=2, scale=1.0):
        Ni, Nj = (int(scale * s) for s in patch_size)
        for i in range(0, img.shape[0] - Ni, istep):
            for j in range(0, img.shape[1] - Ni, jstep):
                patch = img[i:i + Ni, j:j + Nj]
                if scale != 1:
                    patch = transform.resize(patch, patch_size)
                yield (i, j), patch
    
    indices, patches = zip(*sliding_window(test_image))
    patches_hog = np.array([feature.hog(patch) for patch in patches])

    #Use our face detector to evaluate whether each patch contains a face
    labels = model.predict(patches_hog)
    labels.sum()

    # Draw face detected patches as rectangles
    fig, ax = plt.subplots()
    ax.imshow(test_image, cmap='gray')
    ax.axis('off')
    Ni, Nj = positive_patches[0].shape
    indices = np.array(indices)
    for i, j in indices[labels == 1]:
        ax.add_patch(plt.Rectangle((j, i), Nj, Ni, edgecolor='red',alpha=0.3, lw=2, facecolor='none'))

    best_model = joblib.load("Nesrine&Rihab.sav")
    return best_model.predict(data)
