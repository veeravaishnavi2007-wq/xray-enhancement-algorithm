import cv2
import numpy as np
import logging

logger = logging.getLogger(__name__)


class AdaptiveNoiseReductionModule:
    """Applies region-based filtering to remove noise while protecting edges."""
    
    @staticmethod
    def apply_adaptive_denoising(image: np.ndarray, noise_level: float) -> np.ndarray:
        """
        Apply adaptive denoising based on noise level.
        
        Args:
            image: Input image
            noise_level: Detected noise level (0-1)
            
        Returns:
            Denoised image
        """
        image_float = image.astype(np.float32) / 255.0
        
        if noise_level < 0.3:
            # Low noise: minimal filtering
            denoised = cv2.fastNlMeansDenoising(image, h=5, templateWindowSize=7, searchWindowSize=21)
        elif noise_level < 0.7:
            # Medium noise: moderate filtering
            denoised = cv2.fastNlMeansDenoising(image, h=10, templateWindowSize=7, searchWindowSize=21)
        else:
            # High noise: aggressive filtering with bilateral filter
            denoised = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)
            # Additional mild NLM filtering
            denoised = cv2.fastNlMeansDenoising(denoised, h=12, templateWindowSize=7, searchWindowSize=21)
        
        logger.info(f"Adaptive denoising applied with noise level: {noise_level:.4f}")
        return denoised