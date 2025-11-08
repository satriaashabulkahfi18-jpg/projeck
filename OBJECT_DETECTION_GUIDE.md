# 🔍 Object Detection Guide - Phase 2 (Future)

## 📋 Overview

Setelah berhasil menyelesaikan Phase 1 (Multi-task Classification), fase berikutnya adalah menambahkan Object Detection untuk:
- ✅ Mendeteksi lokasi penyakit pada daun
- ✅ Mengidentifikasi objek di sekitar daun (tanah, batang, serangga)
- ✅ Membuat prediksi lebih informatif dengan bounding boxes

---

## 🎯 Use Cases

```
INPUT: Foto daun singkong → 
OUTPUT 1: Disease class (mosaic, healthy, etc.)
OUTPUT 2: Binary (cassava or non-cassava)
OUTPUT 3: Bounding boxes dengan labels
          [disease area, soil, stem, insect]
```

---

## 📊 Dataset Preparation untuk Object Detection

### Step 1: Collect Images
```
collect_images/
├── diseased_leaves/
├── healthy_leaves/
└── non_cassava/
```

### Step 2: Annotate dengan Bounding Boxes

Tools yang bisa digunakan:
1. **LabelImg** (Recommended - Simple & Fast)
2. **CVAT** (Advanced - Team collaboration)
3. **Roboflow** (Cloud-based - Easy integration)

### Step 3: Export Format
```
Supported formats:
- YOLO format (.txt files)
- COCO format (.json)
- Pascal VOC format (.xml)
```

---

## 🛠️ Annotation Tools Setup

### Option 1: LabelImg (Recommended)

**Installation:**
```bash
pip install labelimg
```

**Usage:**
```bash
labelimg
```

Then:
1. Open dir with images
2. Create bounding boxes
3. Save as YOLO format
4. Export as .txt files

**Output Structure:**
```
annotated_images/
├── image_001.jpg
├── image_001.txt  # Format: class_id x_center y_center width height
├── image_002.jpg
├── image_002.txt
└── classes.txt    # List of class names
```

### Option 2: Roboflow (Cloud-based)

Visit: https://roboflow.com

Steps:
1. Create project
2. Upload images
3. Draw bounding boxes in browser
4. Export in desired format
5. Download annotated dataset

**Advantages:**
- ✅ No installation required
- ✅ Built-in augmentation
- ✅ Free tier available
- ✅ Automatic train/val/test split

---

## 📝 Annotation Format Examples

### YOLO Format
```txt
# image_001.txt
0 0.5 0.3 0.4 0.5   # class_id, x_center, y_center, width, height (normalized)
1 0.7 0.6 0.2 0.3
```

**Classes:**
```txt
# classes.txt
disease_area
soil
stem
insect
```

### COCO Format
```json
{
  "images": [
    {"id": 1, "file_name": "image_001.jpg", "height": 480, "width": 640}
  ],
  "annotations": [
    {
      "id": 1,
      "image_id": 1,
      "category_id": 0,
      "bbox": [100, 50, 250, 300],
      "area": 75000,
      "iscrowd": 0
    }
  ],
  "categories": [
    {"id": 0, "name": "disease_area"},
    {"id": 1, "name": "soil"}
  ]
}
```

---

## 🚀 YOLOv8 Implementation

### Installation
```bash
pip install ultralytics opencv-python
```

### Training Code
```python
from ultralytics import YOLO

# Load model
model = YOLO('yolov8m.pt')  # m=medium, n=nano, l=large

# Train
results = model.train(
    data='dataset.yaml',  # Path to dataset config
    epochs=100,
    imgsz=640,
    batch=16,
    patience=20,
    device=0  # GPU device
)

# Validate
metrics = model.val()

# Predict
predictions = model.predict(source='image.jpg', conf=0.5)

# Export
model.export(format='onnx')  # TensorFlow, TorchScript, etc.
```

### dataset.yaml Format
```yaml
path: /path/to/dataset
train: images/train
val: images/val
test: images/test

nc: 4
names: ['disease_area', 'soil', 'stem', 'insect']
```

---

## 🔗 Faster R-CNN Option

```python
import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torch.utils.data import DataLoader, Dataset

# Load pretrained model
model = fasterrcnn_resnet50_fpn(
    pretrained=True,
    num_classes=5  # 4 objects + background
)

# Custom dataset
class CassavaDataset(Dataset):
    def __init__(self, image_dir, annotation_dir):
        self.images = [...]
        self.annotations = [...]
    
    def __getitem__(self, idx):
        image = ...
        boxes = ...  # [[x1,y1,x2,y2], ...]
        labels = ...  # [1, 2, 3]
        
        return image, {
            'boxes': boxes,
            'labels': labels,
            'image_id': idx
        }
    
    def __len__(self):
        return len(self.images)

# Train
optimizer = torch.optim.SGD(model.parameters(), lr=0.005)
model.train()

for epoch in range(10):
    for images, targets in dataloader:
        loss_dict = model(images, targets)
        losses = sum(loss for loss in loss_dict.values())
        
        optimizer.zero_grad()
        losses.backward()
        optimizer.step()
```

---

## 🎯 RetinaNet Alternative

```python
from torchvision.models.detection import retinanet_resnet50_fpn

model = retinanet_resnet50_fpn(
    pretrained=True,
    num_classes=5
)

# Training similar to Faster R-CNN
# Better for small objects
```

---

## 🔄 Integration Strategy: 3-Task Learning

Gabungkan Classification + Binary + Detection:

```
INPUT IMAGE
    ↓
SHARED BACKBONE (VGG16 or ResNet)
    ↓
    ├─→ Disease Classifier (softmax 6 classes)
    ├─→ Binary Classifier (softmax 2 classes)
    └─→ Object Detector (bounding boxes + class)
    ↓
OUTPUT:
{
  'disease': 'mosaic',
  'disease_confidence': 0.92,
  'cassava_type': 'cassava',
  'cassava_confidence': 0.98,
  'detections': [
    {'class': 'disease_area', 'bbox': [100,50,250,300], 'conf': 0.89},
    {'class': 'soil', 'bbox': [0,200,640,480], 'conf': 0.95}
  ]
}
```

---

## 📈 Performance Benchmarks

| Model | mAP@0.5 | Inference | Model Size |
|-------|---------|-----------|-----------|
| YOLOv8n | 37.3% | 6.3ms | 3.2MB |
| YOLOv8s | 44.9% | 11.4ms | 11.2MB |
| YOLOv8m | 50.2% | 25.9ms | 26MB |
| Faster R-CNN | 41.9% | 61.0ms | 142MB |
| RetinaNet | 39.1% | 74.0ms | 138MB |

**Recommendation:** YOLOv8m untuk balance antara accuracy & speed

---

## ✅ Best Practices

### 1. Data Collection
- ✅ Minimum 500 annotated images
- ✅ Balanced classes (min 50 per class)
- ✅ Varied lighting conditions
- ✅ Different angles & distances

### 2. Annotation Quality
- ✅ Consistent bounding box sizing
- ✅ Double-check labels
- ✅ Remove duplicate annotations
- ✅ Use tool validation features

### 3. Training
- ✅ Split: 70% train, 15% val, 15% test
- ✅ Use augmentation (rotation, flip, brightness)
- ✅ Monitor mAP metric
- ✅ Save best checkpoint

### 4. Validation
- ✅ Check IoU threshold (0.5, 0.75)
- ✅ Calculate precision & recall per class
- ✅ Test on diverse samples
- ✅ Document results

---

## 🔄 Workflow Timeline

```
Current (Phase 1) → Phase 2 Preparation → Phase 2 Implementation → Phase 3

Timeline:
Week 1-2: Collect 500+ images
Week 3-4: Annotate with bounding boxes
Week 5-6: Train object detection model
Week 7-8: Integrate with classification model
Week 9+: Deploy 3-task system
```

---

## 📞 Troubleshooting

| Problem | Solution |
|---------|----------|
| Poor mAP | More annotations, better augmentation |
| False positives | Increase conf threshold, retrain with more examples |
| Slow inference | Use smaller model (nano, small) or optimize |
| Memory issues | Reduce batch size, use model quantization |
| Classes imbalanced | Use weighted loss, augmentation |

---

## 🎯 Next Checklist

- [ ] Collect 500+ images with disease
- [ ] Collect 500+ images without disease
- [ ] Setup annotation tool (LabelImg or Roboflow)
- [ ] Complete annotations
- [ ] Export in YOLO format
- [ ] Train YOLOv8m model
- [ ] Integrate with Phase 1 model
- [ ] Test on real-world samples
- [ ] Deploy to production
