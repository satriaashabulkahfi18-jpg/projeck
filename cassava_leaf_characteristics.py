# cassava_leaf_characteristics.py - Karakteristik Daun Singkong
"""
Modul untuk menganalisis dan menjelaskan karakteristik yang membedakan
daun singkong dengan jenis daun lainnya.

Berdasarkan studi botani dan computer vision analysis.
"""

import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
try:
    from skimage import feature, filters
except ImportError:
    print("⚠️ scikit-image tidak tersedia, menggunakan fallback methods")
    feature = None
    filters = None
import pandas as pd

class CassavaLeafAnalyzer:
    """
    Analyzer untuk mengidentifikasi karakteristik unik daun singkong
    """

    def __init__(self):
        # Karakteristik morfologi daun singkong
        self.cassava_characteristics = {
            'shape': {
                'lobed_structure': 'Palmate lobes (5-7 lobes)',
                'leaf_margin': 'Serrated/crenate margin',
                'apex_shape': 'Acute to acuminate',
                'base_shape': 'Cordate (heart-shaped)',
                'venation': 'Palmate venation'
            },
            'color': {
                'upper_surface': 'Dark green (RGB: 30-60, 80-120, 30-60)',
                'lower_surface': 'Lighter green with pubescence',
                'color_variance': 'Uniform green with slight variegation',
                'chlorophyll_content': 'High chlorophyll density'
            },
            'texture': {
                'surface_texture': 'Slightly rough/pubescent',
                'vein_texture': 'Prominent midrib and secondary veins',
                'thickness': 'Thin to medium thickness',
                'flexibility': 'Flexible, not brittle'
            },
            'size': {
                'average_length': '15-30 cm',
                'average_width': '10-25 cm',
                'petiole_length': 'Long petiole (15-40 cm)',
                'lobes': '5-9 lobes per leaf'
            }
        }

        # Karakteristik yang membedakan dengan daun lain
        self.differentiating_features = {
            'vs_banana_leaf': [
                'Cassava: Palmate lobes, Banana: Entire leaf',
                'Cassava: Shorter petiole, Banana: Very long petiole',
                'Cassava: Heart-shaped base, Banana: Asymmetric base'
            ],
            'vs_sweet_potato': [
                'Cassava: Larger leaves, Sweet potato: Smaller leaves',
                'Cassava: 5-7 lobes, Sweet potato: 3-5 lobes',
                'Cassava: Rough texture, Sweet potato: Smooth texture'
            ],
            'vs_fruit_trees': [
                'Cassava: Large compound leaves, Fruit trees: Simple leaves',
                'Cassava: Palmate structure, Fruit trees: Various structures',
                'Cassava: Tropical appearance, Fruit trees: Temperate/deciduous'
            ],
            'vs_grass_weeds': [
                'Cassava: Broad leaves, Grass: Narrow linear leaves',
                'Cassava: Lobed structure, Grass: Entire margin',
                'Cassava: Palmate venation, Grass: Parallel venation'
            ]
        }

    def analyze_leaf_morphology(self, image):
        """
        Analisis morfologi daun menggunakan computer vision
        """
        # Convert to numpy array
        if isinstance(image, Image.Image):
            img_array = np.array(image)
        else:
            img_array = image

        # Convert to grayscale for analysis
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

        # Edge detection
        edges = cv2.Canny(gray, 100, 200)

        # Contour detection
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if not contours:
            return None

        # Get largest contour (main leaf)
        main_contour = max(contours, key=cv2.contourArea)

        # Morphological analysis
        area = cv2.contourArea(main_contour)
        perimeter = cv2.arcLength(main_contour, True)

        # Compactness (measure of leaf shape complexity)
        compactness = (perimeter ** 2) / (4 * np.pi * area) if area > 0 else 0

        # Bounding box
        x, y, w, h = cv2.boundingRect(main_contour)
        aspect_ratio = w / h if h > 0 else 0

        # Convex hull analysis (for lobed structure)
        hull = cv2.convexHull(main_contour)
        hull_area = cv2.contourArea(hull)
        solidity = area / hull_area if hull_area > 0 else 0

        # Detect lobes (significant indentations)
        hull_perimeter = cv2.arcLength(hull, True)
        lobe_ratio = hull_perimeter / perimeter if perimeter > 0 else 0

        morphology_features = {
            'area': area,
            'perimeter': perimeter,
            'compactness': compactness,
            'aspect_ratio': aspect_ratio,
            'solidity': solidity,
            'lobe_ratio': lobe_ratio,
            'bounding_box': (w, h),
            'is_lobed': lobe_ratio > 1.2,  # Threshold for lobed leaves
            'is_palmate': compactness > 15  # High compactness indicates palmate structure
        }

        return morphology_features

    def analyze_leaf_color(self, image):
        """
        Analisis karakteristik warna daun
        """
        if isinstance(image, Image.Image):
            img_array = np.array(image)
        else:
            img_array = image

        # Convert to HSV for better color analysis
        hsv = cv2.cvtColor(img_array, cv2.COLOR_RGB2HSV)

        # Calculate color statistics
        h_mean, h_std = np.mean(hsv[:, :, 0]), np.std(hsv[:, :, 0])
        s_mean, s_std = np.mean(hsv[:, :, 1]), np.std(hsv[:, :, 1])
        v_mean, v_std = np.mean(hsv[:, :, 2]), np.std(hsv[:, :, 2])

        # RGB statistics
        r_mean, r_std = np.mean(img_array[:, :, 0]), np.std(img_array[:, :, 0])
        g_mean, g_std = np.mean(img_array[:, :, 1]), np.std(img_array[:, :, 1])
        b_mean, b_std = np.mean(img_array[:, :, 2]), np.std(img_array[:, :, 2])

        # Color classification
        if 80 < h_mean < 140:  # Green hue range
            dominant_color = "green"
            is_healthy_green = s_mean > 50 and v_mean > 100  # Saturated and bright green
        else:
            dominant_color = "non_green"
            is_healthy_green = False

        color_features = {
            'hsv_stats': {
                'hue_mean': h_mean, 'hue_std': h_std,
                'saturation_mean': s_mean, 'saturation_std': s_std,
                'value_mean': v_mean, 'value_std': v_std
            },
            'rgb_stats': {
                'red_mean': r_mean, 'red_std': r_std,
                'green_mean': g_mean, 'green_std': g_std,
                'blue_mean': b_mean, 'blue_std': b_std
            },
            'dominant_color': dominant_color,
            'is_healthy_green': is_healthy_green,
            'color_uniformity': (r_std + g_std + b_std) / 3,  # Lower = more uniform
            'green_dominance': g_mean / (r_mean + b_mean + 1)  # Green vs other colors
        }

        return color_features

    def analyze_leaf_texture(self, image):
        """
        Analisis tekstur daun menggunakan GLCM dan filter banks
        """
        if isinstance(image, Image.Image):
            img_array = np.array(image)
        else:
            img_array = image

        # Convert to grayscale
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

        # Try GLCM features if scikit-image is available
        if feature is not None:
            try:
                # GLCM (Gray Level Co-occurrence Matrix) features
                glcm = feature.graycomatrix(gray, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4],
                                           levels=256, symmetric=True, normed=True)

                # Texture features from GLCM
                contrast = feature.graycoprops(glcm, 'contrast').mean()
                dissimilarity = feature.graycoprops(glcm, 'dissimilarity').mean()
                homogeneity = feature.graycoprops(glcm, 'homogeneity').mean()
                energy = feature.graycoprops(glcm, 'energy').mean()
                correlation = feature.graycoprops(glcm, 'correlation').mean()
            except Exception as e:
                print(f"⚠️ GLCM analysis failed: {e}, using fallback")
                contrast = dissimilarity = homogeneity = energy = correlation = 0.5
        else:
            # Fallback values if scikit-image not available
            contrast = dissimilarity = homogeneity = energy = correlation = 0.5

        # Edge density (roughness measure) - always available
        edges = cv2.Canny(gray, 100, 200)
        edge_density = np.sum(edges > 0) / edges.size

        # Local variance (texture complexity) - using OpenCV
        # Create a simple local variance measure
        kernel = np.ones((5, 5), np.float32) / 25
        local_mean = cv2.filter2D(gray.astype(np.float32), -1, kernel)
        local_var = cv2.filter2D((gray.astype(np.float32) - local_mean)**2, -1, kernel)
        texture_complexity = np.std(local_var)

        texture_features = {
            'glcm_features': {
                'contrast': contrast,
                'dissimilarity': dissimilarity,
                'homogeneity': homogeneity,
                'energy': energy,
                'correlation': correlation
            },
            'edge_density': edge_density,
            'texture_complexity': texture_complexity,
            'surface_smoothness': homogeneity,  # Higher = smoother
            'texture_roughness': contrast  # Higher = rougher
        }

        return texture_features

    def classify_leaf_type(self, morphology, color, texture):
        """
        Klasifikasi jenis daun berdasarkan karakteristik khusus daun singkong
        Fokus pada identifikasi daun singkong vs bukan
        """
        scores = {
            'cassava': 0,
            'not_cassava': 0
        }

        # CRITICAL CASSAVA CHARACTERISTICS CHECK
        cassava_identifiers = 0
        total_checks = 0

        # 1. Morphology Check - PALMATE COMPOUND STRUCTURE (most important)
        if morphology:
            total_checks += 1
            # Cassava has palmate lobes with specific characteristics
            if morphology['is_lobed'] and morphology['is_palmate']:
                if 10 < morphology['compactness'] < 20:  # Specific compactness range for cassava
                    cassava_identifiers += 1
                    scores['cassava'] += 3
                else:
                    scores['not_cassava'] += 2
            else:
                scores['not_cassava'] += 3  # Strong negative for non-lobed leaves

            # 2. Aspect ratio check - cassava leaves are broad, not long and narrow
            total_checks += 1
            if morphology['aspect_ratio'] < 2.5:  # Broad leaves
                cassava_identifiers += 1
                scores['cassava'] += 2
            elif morphology['aspect_ratio'] > 3:  # Very long/narrow (banana-like)
                scores['not_cassava'] += 3

            # 3. Solidity check - cassava has complex lobed structure
            total_checks += 1
            if 0.6 < morphology['solidity'] < 0.9:  # Complex but not too solid
                cassava_identifiers += 1
                scores['cassava'] += 1

        # 2. Color Check - DARK GREEN DOMINANCE
        if color:
            total_checks += 1
            # Cassava has high green dominance and healthy green color
            if color['green_dominance'] > 1.8 and color['is_healthy_green']:
                cassava_identifiers += 1
                scores['cassava'] += 2
            elif color['green_dominance'] < 1.2:  # Low green dominance
                scores['not_cassava'] += 2

            # Color uniformity - cassava is uniform
            total_checks += 1
            if color['color_uniformity'] < 40:  # Uniform color
                cassava_identifiers += 1
                scores['cassava'] += 1

        # 3. Texture Check - ROUGH/PUBESCENT SURFACE
        if texture:
            total_checks += 1
            # Cassava has rough texture with moderate complexity
            if 50 < texture['texture_roughness'] < 200:  # Rough but not extreme
                cassava_identifiers += 1
                scores['cassava'] += 2
            elif texture['texture_roughness'] < 20:  # Too smooth (banana-like)
                scores['not_cassava'] += 2

            # Edge density - cassava has complex edges due to lobes
            total_checks += 1
            if texture['edge_density'] > 0.05:  # Complex edges
                cassava_identifiers += 1
                scores['cassava'] += 1

        # FINAL DECISION BASED ON CASSAVA IDENTIFIERS
        if total_checks == 0:
            return {'predicted_type': 'unknown', 'confidence': 0.0, 'scores': scores}

        # Cassava requires majority of checks to pass
        cassava_ratio = cassava_identifiers / total_checks

        if cassava_ratio >= 0.6:  # 60% of checks pass
            predicted_type = 'cassava'
            confidence = cassava_ratio
        else:
            predicted_type = 'not_cassava'
            confidence = 1 - cassava_ratio

        # Boost confidence for very clear cases
        if cassava_ratio >= 0.8:
            confidence = min(confidence + 0.2, 1.0)  # Boost confidence
        elif cassava_ratio <= 0.3:
            confidence = max(confidence, 0.7)  # High confidence for clear non-cassava

        return {
            'predicted_type': predicted_type,
            'confidence': confidence,
            'scores': scores,
            'cassava_identifiers': cassava_identifiers,
            'total_checks': total_checks,
            'cassava_ratio': cassava_ratio
        }

    def get_cassava_identification_guide(self):
        """
        Panduan lengkap mengidentifikasi daun singkong
        """
        guide = {
            'morphological_identifiers': [
                "Bentuk daun: Majemuk palmata dengan 5-7 cuping",
                "Ujung daun: Lancip (acuminate)",
                "Dasar daun: Berbentuk hati (cordate)",
                "Tepi daun: Bergerigi (serrated/crenate)",
                "Panjang tangkai daun: 15-40 cm",
                "Susunan tulang daun: Palmate (seperti tangan)"
            ],
            'color_identifiers': [
                "Warna permukaan atas: Hijau tua mengkilap",
                "Warna permukaan bawah: Hijau muda dengan bulu halus",
                "Kecerahan: Sangat hijau tanpa variegasi berarti",
                "Kandungan klorofil: Tinggi, menunjukkan kesehatan tanaman"
            ],
            'texture_identifiers': [
                "Tekstur permukaan: Sedikit kasar/berbulu halus",
                "Tulang daun utama: Menonjol dan tebal",
                "Ketebalan daun: Tipis hingga sedang",
                "Kekenyalan: Fleksibel, tidak rapuh"
            ],
            'size_identifiers': [
                "Panjang daun: 15-30 cm",
                "Lebar daun: 10-25 cm",
                "Jumlah cuping: 5-9 cuping per daun",
                "Ukuran keseluruhan: Daun besar untuk tanaman tropis"
            ]
        }

        return guide

    def compare_with_other_leaves(self, leaf_type='cassava'):
        """
        Perbandingan karakteristik dengan jenis daun lainnya
        """
        comparisons = {
            'cassava_vs_banana': {
                'similarities': [
                    'Keduanya tanaman tropis',
                    'Warna hijau dominan',
                    'Daun besar'
                ],
                'differences': [
                    'Cassava: 5-7 lobes, palmat, petiole 15-40cm',
                    'Banana: Entire leaf, no lobes, petiole 2-3m',
                    'Cassava: Heart-shaped base, Banana: Asymmetric base',
                    'Cassava: Rough texture, Banana: Smooth and waxy'
                ]
            },
            'cassava_vs_sweet_potato': {
                'similarities': [
                    'Keduanya umbi akar',
                    'Daun hijau',
                    'Tanaman tropis'
                ],
                'differences': [
                    'Cassava: Larger leaves (15-30cm), Sweet potato: Smaller (5-15cm)',
                    'Cassava: 5-7 lobes, Sweet potato: 3-5 lobes',
                    'Cassava: Rough/pubescent, Sweet potato: Smooth',
                    'Cassava: Cordate base, Sweet potato: Various bases'
                ]
            },
            'cassava_vs_fruit_trees': {
                'similarities': [
                    'Daun hijau',
                    'Fotosintesis'
                ],
                'differences': [
                    'Cassava: Large compound leaves, Fruit trees: Simple leaves',
                    'Cassava: Palmate structure, Fruit trees: Elliptic/lanceolate',
                    'Cassava: Tropical evergreen, Fruit trees: Often deciduous',
                    'Cassava: Rough texture, Fruit trees: Smooth/waxy'
                ]
            },
            'cassava_vs_grass_weeds': {
                'similarities': [
                    'Hijau',
                    'Fotosintesis'
                ],
                'differences': [
                    'Cassava: Broad lobed leaves, Grass: Narrow linear leaves',
                    'Cassava: Palmate venation, Grass: Parallel venation',
                    'Cassava: Large size, Grass: Small/fine leaves',
                    'Cassava: Compound structure, Grass: Simple structure'
                ]
            }
        }

        return comparisons.get(f'{leaf_type}_vs_{leaf_type}', {})

def create_leaf_comparison_visualization():
    """
    Membuat visualisasi perbandingan karakteristik daun
    """
    analyzer = CassavaLeafAnalyzer()

    # Data untuk comparison table
    comparison_data = {
        'Feature': ['Shape', 'Size', 'Texture', 'Color', 'Venation', 'Margin'],
        'Cassava': ['Palmate lobes', '15-30cm', 'Rough', 'Dark green', 'Palmate', 'Serrated'],
        'Banana': ['Entire', '2-3m', 'Smooth/waxy', 'Light green', 'Parallel', 'Entire'],
        'Sweet Potato': ['Lobed (3-5)', '5-15cm', 'Smooth', 'Light green', 'Palmate', 'Lobed'],
        'Fruit Trees': ['Simple', 'Various', 'Smooth/waxy', 'Various', 'Pinnate', 'Various'],
        'Grass': ['Linear', 'Small', 'Smooth', 'Light green', 'Parallel', 'Entire']
    }

    df = pd.DataFrame(comparison_data)
    return df

def analyze_image_and_identify(image_path):
    """
    Analisis lengkap gambar daun dan identifikasi jenisnya
    """
    try:
        analyzer = CassavaLeafAnalyzer()

        # Load image
        image = Image.open(image_path).convert('RGB')

        # Analyze features
        morphology = analyzer.analyze_leaf_morphology(image)
        color = analyzer.analyze_leaf_color(image)
        texture = analyzer.analyze_leaf_texture(image)

        # Classify
        classification = analyzer.classify_leaf_type(morphology, color, texture)

        # Get identification guide
        guide = analyzer.get_cassava_identification_guide()

        result = {
            'morphology_analysis': morphology,
            'color_analysis': color,
            'texture_analysis': texture,
            'classification': classification,
            'identification_guide': guide,
            'is_cassava': classification['predicted_type'] == 'cassava',
            'confidence': classification['confidence']
        }

        return result

    except Exception as e:
        return {'error': f'Analysis failed: {str(e)}'}

# Utility functions
def print_cassava_characteristics():
    """
    Print semua karakteristik daun singkong
    """
    analyzer = CassavaLeafAnalyzer()

    print("🌿 KARAKTERISTIK DAUN SINGKONG")
    print("=" * 50)

    print("\n📏 MORFOLOGI:")
    for key, value in analyzer.cassava_characteristics['shape'].items():
        print(f"  • {key}: {value}")

    print("\n🎨 WARNA:")
    for key, value in analyzer.cassava_characteristics['color'].items():
        print(f"  • {key}: {value}")

    print("\n🔍 TEKSTUR:")
    for key, value in analyzer.cassava_characteristics['texture'].items():
        print(f"  • {key}: {value}")

    print("\n📐 UKURAN:")
    for key, value in analyzer.cassava_characteristics['size'].items():
        print(f"  • {key}: {value}")

def compare_leaves():
    """
    Print perbandingan dengan daun lainnya
    """
    analyzer = CassavaLeafAnalyzer()

    print("\n🔄 PERBANDINGAN DENGAN DAUN LAIN:")
    print("=" * 50)

    for comparison_type, features in analyzer.differentiating_features.items():
        print(f"\n{comparison_type.upper().replace('_', ' VS ')}:")
        for feature in features:
            print(f"  • {feature}")

if __name__ == "__main__":
    # Print characteristics
    print_cassava_characteristics()
    compare_leaves()

    # Create comparison table
    comparison_df = create_leaf_comparison_visualization()
    print("\n📊 TABEL PERBANDINGAN:")
    print(comparison_df.to_string(index=False))