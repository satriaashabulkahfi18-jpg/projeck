ap# leaf_segmentation.py - Object Detection & Segmentation untuk Daun Singkong
import cv2
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Conv2D, UpSampling2D, Concatenate
from tensorflow.keras.models import Model
import os

class LeafSegmenter:
    """
    Class untuk segmentasi daun singkong dari gambar kompleks
    Menggunakan U-Net architecture dengan VGG16 backbone
    """

    def __init__(self, model_path=None):
        self.model = None
        self.model_path = model_path or "models/leaf_segmentation_model.h5"
        self.load_or_create_model()

    def create_unet_model(self, input_shape=(224, 224, 3)):
        """
        Membuat model U-Net untuk segmentasi daun
        """
        # Encoder (VGG16 backbone)
        base_model = VGG16(weights='imagenet', include_top=False, input_shape=input_shape)

        # Encoder layers
        s1 = base_model.get_layer('block1_conv2').output
        s2 = base_model.get_layer('block2_conv2').output
        s3 = base_model.get_layer('block3_conv3').output
        s4 = base_model.get_layer('block4_conv3').output
        b1 = base_model.get_layer('block5_conv3').output

        # Decoder
        d1 = self.decoder_block(b1, s4, 512)
        d2 = self.decoder_block(d1, s3, 256)
        d3 = self.decoder_block(d2, s2, 128)
        d4 = self.decoder_block(d3, s1, 64)

        # Output
        outputs = Conv2D(1, 1, padding='same', activation='sigmoid')(d4)

        model = Model(base_model.input, outputs, name='Leaf_Segmentation_UNet')
        return model

    def decoder_block(self, input_tensor, skip_tensor, num_filters):
        """
        Decoder block untuk U-Net
        """
        x = UpSampling2D((2, 2))(input_tensor)
        x = Concatenate()([x, skip_tensor])
        x = Conv2D(num_filters, 3, padding='same', activation='relu')(x)
        x = Conv2D(num_filters, 3, padding='same', activation='relu')(x)
        return x

    def load_or_create_model(self):
        """
        Load model yang sudah ada atau buat model baru
        """
        if os.path.exists(self.model_path):
            try:
                self.model = tf.keras.models.load_model(self.model_path)
                print("✅ Model segmentasi daun berhasil dimuat")
            except Exception as e:
                print(f"⚠️ Gagal load model: {e}, membuat model baru")
                self.model = self.create_unet_model()
        else:
            print("🆕 Membuat model segmentasi daun baru")
            self.model = self.create_unet_model()

        # Compile model
        self.model.compile(
            optimizer='adam',
            loss='binary_crossentropy',
            metrics=['accuracy']
        )

    def preprocess_image(self, image):
        """
        Preprocessing gambar untuk segmentasi
        """
        # Convert to RGB if needed
        if isinstance(image, str):
            image = Image.open(image).convert('RGB')
        elif isinstance(image, np.ndarray):
            image = Image.fromarray(image)

        # Resize
        image = image.resize((224, 224), Image.Resampling.LANCZOS)

        # Convert to array and normalize
        image_array = np.array(image, dtype=np.float32) / 255.0

        return image_array

    def segment_leaf(self, image):
        """
        Segmentasi daun dari gambar
        """
        # Preprocess
        processed_image = self.preprocess_image(image)
        input_image = np.expand_dims(processed_image, axis=0)

        # Predict mask
        mask = self.model.predict(input_image, verbose=0)[0]

        # Threshold mask
        mask = (mask > 0.5).astype(np.uint8)

        return mask.squeeze()

    def extract_leaf_region(self, image, mask, padding=10):
        """
        Ekstrak region daun dari gambar asli berdasarkan mask
        """
        # Convert to numpy array
        if isinstance(image, Image.Image):
            image_array = np.array(image)
        else:
            image_array = image

        # Find contours
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if not contours:
            return image_array  # Return original if no contours found

        # Get largest contour (assuming it's the main leaf)
        largest_contour = max(contours, key=cv2.contourArea)

        # Get bounding box
        x, y, w, h = cv2.boundingRect(largest_contour)

        # Add padding
        x = max(0, x - padding)
        y = max(0, y - padding)
        w = min(image_array.shape[1] - x, w + 2*padding)
        h = min(image_array.shape[0] - y, h + 2*padding)

        # Crop image
        cropped_image = image_array[y:y+h, x:x+w]

        return cropped_image

    def process_image_for_classification(self, image_path):
        """
        Pipeline lengkap: segmentasi + ekstraksi daun untuk klasifikasi
        """
        try:
            # Load image
            original_image = Image.open(image_path).convert('RGB')

            # Segment leaf
            mask = self.segment_leaf(original_image)

            # Extract leaf region
            leaf_region = self.extract_leaf_region(original_image, mask)

            # Convert back to PIL Image
            if isinstance(leaf_region, np.ndarray):
                leaf_region = Image.fromarray(leaf_region)

            return leaf_region, mask

        except Exception as e:
            print(f"❌ Error dalam segmentasi: {e}")
            # Return original image if segmentation fails
            return Image.open(image_path).convert('RGB'), None

class LeafDetector:
    """
    Class untuk deteksi daun menggunakan color thresholding
    Alternatif yang lebih sederhana dari deep learning segmentation
    """

    def __init__(self):
        pass

    def detect_leaf_color_threshold(self, image):
        """
        Deteksi daun singkong menggunakan color thresholding yang lebih spesifik
        Fokus pada warna hijau khas daun singkong
        """
        # Convert to numpy array
        if isinstance(image, Image.Image):
            image_array = np.array(image)
        else:
            image_array = image

        # Convert to HSV
        hsv = cv2.cvtColor(image_array, cv2.COLOR_RGB2HSV)

        # Define range for cassava leaf green color (more specific)
        # Cassava leaves typically have specific green hue range
        lower_green = np.array([30, 30, 30])  # Lower bound for cassava green
        upper_green = np.array([90, 255, 255])  # Upper bound for cassava green

        # Create initial mask
        mask = cv2.inRange(hsv, lower_green, upper_green)

        # Additional filtering for cassava leaf characteristics
        # Filter out very bright or very dark areas (not typical for healthy cassava leaves)
        value_channel = hsv[:, :, 2]
        saturation_channel = hsv[:, :, 1]

        # Healthy cassava leaves have moderate brightness and saturation
        brightness_mask = (value_channel > 50) & (value_channel < 220)
        saturation_mask = (saturation_channel > 40) & (saturation_channel < 200)

        # Combine masks
        combined_mask = mask & brightness_mask & saturation_mask

        # Morphological operations to clean mask
        kernel = np.ones((7, 7), np.uint8)  # Larger kernel for better cleaning
        combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_OPEN, kernel)
        combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_CLOSE, kernel)

        # Additional filtering: remove small noise
        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(combined_mask, connectivity=8)

        # Keep only components larger than minimum area (filter noise)
        min_area = 500  # Minimum area for cassava leaf region
        filtered_mask = np.zeros_like(combined_mask)

        for i in range(1, num_labels):  # Skip background (label 0)
            if stats[i, cv2.CC_STAT_AREA] > min_area:
                filtered_mask[labels == i] = 255

        return filtered_mask.astype(np.uint8)

    def extract_largest_green_region(self, image, mask, min_area=2000):
        """
        Ekstrak region hijau terbesar dari gambar dengan fokus pada daun singkong
        """
        # Find contours
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if not contours:
            return image  # Return original if no contours

        # Filter contours by area and shape characteristics typical for cassava leaves
        valid_contours = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > min_area:
                # Additional cassava leaf characteristics
                perimeter = cv2.arcLength(cnt, True)
                if perimeter > 0:
                    # Calculate circularity (cassava leaves are not perfectly circular)
                    circularity = 4 * np.pi * area / (perimeter * perimeter)
                    # Cassava leaves typically have circularity between 0.1-0.7
                    if 0.1 < circularity < 0.7:
                        # Check aspect ratio (cassava leaves are elongated)
                        x, y, w, h = cv2.boundingRect(cnt)
                        aspect_ratio = float(w) / h if h > 0 else 0
                        if 0.3 < aspect_ratio < 3.0:  # Reasonable aspect ratio for cassava leaves
                            valid_contours.append((cnt, area))

        if not valid_contours:
            return image

        # Get largest contour by area
        largest_contour, _ = max(valid_contours, key=lambda x: x[1])

        # Create mask for largest contour
        leaf_mask = np.zeros_like(mask)
        cv2.drawContours(leaf_mask, [largest_contour], -1, 255, -1)

        # Apply mask to original image
        if isinstance(image, Image.Image):
            image_array = np.array(image)
        else:
            image_array = image

        # Create RGBA image with transparency
        rgba_image = np.zeros((image_array.shape[0], image_array.shape[1], 4), dtype=np.uint8)
        rgba_image[:, :, :3] = image_array
        rgba_image[:, :, 3] = leaf_mask

        return rgba_image

def create_leaf_focused_preprocessing(image_path, use_deep_learning=True):
    """
    Fungsi utama untuk preprocessing gambar agar fokus pada daun singkong saja
    """
    try:
        original_image = Image.open(image_path).convert('RGB')

        if use_deep_learning:
            # Use deep learning segmentation
            segmenter = LeafSegmenter()
            processed_image, mask = segmenter.process_image_for_classification(image_path)
        else:
            # Use improved color thresholding for cassava leaves
            detector = LeafDetector()
            mask = detector.detect_leaf_color_threshold(original_image)

            # Check if we found a valid cassava leaf region
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            valid_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 2000]

            if valid_contours:
                # Found potential cassava leaf regions
                processed_image = detector.extract_largest_green_region(original_image, mask)
            else:
                # No valid cassava leaf found, return original image
                print("⚠️ No valid cassava leaf region detected, using original image")
                processed_image = original_image

        return processed_image

    except Exception as e:
        print(f"⚠️ Error in preprocessing: {e}, returning original image")
        return Image.open(image_path).convert('RGB')

# Utility functions
def visualize_segmentation(image_path, save_path=None):
    """
    Visualisasi hasil segmentasi untuk debugging
    """
    try:
        segmenter = LeafSegmenter()
        original = Image.open(image_path).convert('RGB')
        mask = segmenter.segment_leaf(original)

        # Create visualization
        original_array = np.array(original)
        mask_colored = np.zeros_like(original_array)
        mask_colored[mask > 0] = [0, 255, 0]  # Green overlay

        # Blend images
        alpha = 0.5
        overlay = cv2.addWeighted(original_array, 1-alpha, mask_colored, alpha, 0)

        result = Image.fromarray(overlay)

        if save_path:
            result.save(save_path)

        return result

    except Exception as e:
        print(f"❌ Error in visualization: {e}")
        return None

if __name__ == "__main__":
    # Test segmentation
    print("🧪 Testing leaf segmentation...")

    # Example usage
    test_image = "contoh daun singkong.jpg"  # Ganti dengan path gambar Anda

    if os.path.exists(test_image):
        print(f"📸 Processing image: {test_image}")

        # Test deep learning segmentation
        processed = create_leaf_focused_preprocessing(test_image, use_deep_learning=True)
        print("✅ Deep learning segmentation completed")

        # Test color thresholding
        processed_color = create_leaf_focused_preprocessing(test_image, use_deep_learning=False)
        print("✅ Color thresholding completed")

        print("🎉 Leaf segmentation system ready!")
    else:
        print(f"⚠️ Test image not found: {test_image}")
        print("📝 Please provide a test image to validate the segmentation system")