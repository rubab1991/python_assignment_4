import streamlit as st
import qrcode
import cv2
import numpy as np
from PIL import Image
import io

st.set_page_config(page_title="QR Code App", layout="centered")
st.title("🔳 QR Code Encoder / Decoder")

tab1, tab2 = st.tabs(["📤 Encode", "📥 Decode"])

# -----------------------
# ENCODER
# -----------------------
with tab1:
    st.header("📤 Encode Text/URL to QR Code")
    text_input = st.text_input("Enter text or URL")

    if st.button("Generate QR Code") and text_input:
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(text_input)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

        # Convert image to bytes
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        byte_img = buf.getvalue()

        # Show and download QR code
        st.image(byte_img, caption="Generated QR Code", use_column_width=False)
        st.download_button("Download QR Code", byte_img, file_name="qr_code.png", mime="image/png")

# -----------------------
# DECODER
# -----------------------
with tab2:
    st.header("📥 Decode QR Code Image")
    uploaded_file = st.file_uploader("Upload a QR code image", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(img)

        st.image(img, channels="BGR", caption="Uploaded QR Code")

        if data:
            st.success(f"✅ Decoded Data: {data}")
        else:
            st.error("🚫 No QR code detected in the image.")
