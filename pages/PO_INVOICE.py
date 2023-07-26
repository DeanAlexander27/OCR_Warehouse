import pandas as pd
import cv2
from PIL import Image
import numpy as np
import streamlit as st
import imutils
import tensorflow as tf
from sklearn.preprocessing import LabelBinarizer
from datetime import datetime 
import pytz

model = tf.keras.models.load_model("model3")

LB = LabelBinarizer()
LB.fit_transform(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

st.set_page_config(page_title="OCR Warehouse",
                   page_icon=":bar_chart:",
                   layout="wide")


st.sidebar.success("Select a page above")

# ---- SIDEBAR ----
st.sidebar.header("Please Choose Here:")
PO_letter = st.sidebar.multiselect(
    "Select Your Necessary:",
    options=["PO", "Invoice"]
)

st.sidebar.markdown('---')

# ---- SIDEBAR ----
st.sidebar.header("What tools you are going to use?")
PO_letter = st.sidebar.multiselect(
    "Select Your Necessary:",
    options=["Live Camera", "Insert Picture"]
)


def sort_contours(cnts, method="left-to-right"):
    reverse = False
    i = 0
    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))
    # return the list of sorted contours and bounding boxes
    return (cnts, boundingBoxes)


def get_letters(opencv_image):
    letters = []
    gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    dilated = cv2.dilate(thresh1, None, iterations=2)
    cnts = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sort_contours(cnts, method="left-to-right")[0]
    # loop over the contours
    for c in cnts:
        if cv2.contourArea(c) > 20:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(opencv_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi = gray[y:y + h, x:x + w]
        thresh = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        thresh = cv2.resize(thresh, (32, 32), interpolation=cv2.INTER_CUBIC)
        thresh = thresh.astype("float32") / 255.0
        thresh = np.expand_dims(thresh, axis=-1)
        thresh = thresh.reshape(1, 32, 32, 1)
        ypred = model.predict(thresh)
        ypred = LB.inverse_transform(ypred)
        [x] = ypred
        letters.append(x)
    return letters, opencv_image


# Membuat DataFrame awal (kosong)
data = {'PR': [], 'NAMA': []}
df = pd.DataFrame(data)

now = datetime.now()
jakarta_timezone = pytz.timezone('Asia/Jakarta')
now_jakarta = now.astimezone(jakarta_timezone)

# Fungsi untuk memperbarui DataFrame dan menyimpan ke file CSV
def update_dataframe(word):
    # Membaca DataFrame dari file CSV
    df = pd.read_csv('data.csv')

    # Menambahkan entri baru
    new_entry = {'PR': "".join(word[2:6]), 'NAMA': "".join(word[10:14]), 'Check In Date': now_jakarta.date(), 'Check in Time': now_jakarta.time()}
    df = df.append(new_entry, ignore_index=True)

    # Menyimpan DataFrame terbaru ke file CSV
    df.to_csv('data.csv', index=False)

    return df


def main():
    """OCR Warehouse"""

    st.title("OCR for Warehouse")
    html_body = """<body style="background-color:red;"> </body>"""
    st.markdown(html_body, unsafe_allow_html=True)
    html_temp = """
    <body style ="background-color:red;">
    <div style ="background-color:teal ;padding:10px">
    <h2 style = "color:white; text-align:center;"> WareOCR </h2>
    </div>
    </body>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
if __name__ == '__main__':
    main()

def get_words(letters):
    words = []

    for letter in letters:
        if letter.isalpha():
            if len(letter) > 1:
                words.extend(list(letter))
            else:
                words.append(letter)
        else:
            words.extend(list(letter))

    return words


# Inisialisasi DataFrame global
data = {'PR': [], 'NAMA': []}
df = pd.DataFrame(data)


img_file_buffer = None
image_file = None

if "Live Camera" in PO_letter:
    img_file_buffer = st.camera_input("Take a picture")

    if img_file_buffer is not None:
        # To read image file buffer as a 3D uint8 tensor with TensorFlow:
        bytes_data = img_file_buffer.getvalue()
        img_tensor = tf.io.decode_image(bytes_data, channels=3)

        # Check the type of img_tensor:
        # Should output: <class 'tensorflow.python.framework.ops.EagerTensor'>
        st.write(type(img_tensor))

        # Check the shape of img_tensor:
        # Should output shape: (height, width, channels)
        st.write(img_tensor.shape)

if "Insert Picture" in PO_letter:
    image_file = st.file_uploader("Upload your Document", type=['jpg', 'png', 'jpeg'])
    if image_file is not None:
        file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

if st.button("Recognize"):
    letter, opencv_image = get_letters(opencv_image)
    word = get_words(letter)
    df = update_dataframe(word)
    st.image(opencv_image)
    my_table = st.table(df)

