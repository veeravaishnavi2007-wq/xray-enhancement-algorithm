class NoiseEstimationModule:
    def __init__(self, image):
        self.image = image

    def calculate_laplacian_variance(self):
        import cv2
        import numpy as np

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        # Compute the Laplacian of the image
        laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)

        # Calculate the variance of the Laplacian
        var_laplacian = laplacian.var()

        return var_laplacian

    def estimate_noise_level(self):
        var_laplacian = self.calculate_laplacian_variance()

        # Determine noise level based on the variance of the Laplacian
        if var_laplacian < 100:
            return 'Low Noise'
        elif var_laplacian < 500:
            return 'Moderate Noise'
        else:
            return 'High Noise'