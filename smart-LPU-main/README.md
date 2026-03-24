# CSR Management – Smart Campus Ecosystem

**CSR Management** is a state-of-the-art, high-performance campus resource and attendance management system. Designed with a **Cyberpunk-inspired Premium Dark Theme**, it provides a seamless experience for students, faculty, administrators, and vendors.

---

## 🚀 Vision
To revolutionize campus operations by combining **AI-driven biometric attendance**, **smart food pre-ordering**, and **automated administrative analytics** into a single, cohesive interface.

---

## ✨ Key Features

### 1. Smart Attendance Suite
*   **AI Face Recognition**: High-accuracy face detection and recognition using LBPH algorithms.
*   **Live Mode**: Continuous real-time attendance marking via webcam.
*   **Snapshot Mode**: Bulk mark attendance by uploading a single group photo.
*   **Manual Marking**: Intuitive checkbox-based marking with built-in confirmation logic.

### 2. Food & Smart-Dining
*   **Pre-Order System**: Students can pre-order meals from multiple stalls to avoid canteen rushes.
*   **Vendor Dashboard**: Specialized interface for stall owners to manage orders and inventory.
*   **Loyalty System**: Earn and spend points on every purchase.

### 3. Administrative Powerhouse
*   **CSR Dashboard**: Comprehensive overview of campus sessions, student metrics, and faculty workload.
*   **Resource Analytics**: Monitor capacity utilization of blocks and classrooms.
*   **Automatic Superuser**: Zero-config setup with a built-in administrative account.

### 4. Premium Aesthetic
*   **Cyberpunk Dark UI**: A high-contrast, modern interface that ensures readability and a premium "command center" feel.
*   **Responsive Design**: Optimized for everything from lecture hall monitors to mobile devices.

---

## 🛠️ Tech Stack
*   **Backend**: Django (Python)
*   **AI/Computer Vision**: OpenCV (Face Recognition, Haar Cascades)
*   **Frontend**: Vanilla CSS (High-Contrast Custom Variables), Bootstrap 5 (Layout)
*   **Email**: Integrated notification system for attendance and orders.

---

## 🏁 Quick Start

### 1. Requirements
Ensure you have Python 3.10+ installed.

### 2. Setup
```bash
# Clone the repository
git clone https://github.com/your-repo/csr-management.git
cd csr-management

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Seed the database with sample data
python manage.py seed_all
```

### 3. Default Logins
The system automatically creates two administrative accounts for instant access:

**Admin 1 (Primary)**:
- **Email**: `Chimbilicharan@gmail.com`
- **Password**: `Charan@1835`

**Admin 2 (Co-Admin)**:
- **Email**: `csupreethreddy@gmail.com`
- **Password**: `csr@123`

### 4. Run Server
```bash
python manage.py runserver
```
Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## ⚙️ Face Recognition Setup
For optimal accuracy:
1.  Navigate to **Manage Data > Face Samples**.
2.  Upload **6–10 clear photos** per student (different angles, good lighting).
3.  The system will automatically train the recognizer on the fly for each session!

---

## 📞 Support & Documentation
Managed by the **CSR Development Team**.
