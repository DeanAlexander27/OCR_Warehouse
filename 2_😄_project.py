import pandas as pd
import cv2
from PIL import Image
import numpy as np
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import imutils
import tensorflow as tf
from sklearn.preprocessing import LabelBinarizer

cam = cv2.VideoCapture(0)
model = tf.keras.models.load_model("model1")
LB = LabelBinarizer()


st.set_page_config(page_title = "OCR Warehouse",
                   page_icon = ":bar_chart:",
                   layout = "wide"
                   )


st.sidebar.success("Select a page above")

# ---- SIDEBAR ----
st.sidebar.header("Please Choose Here:")
PO_letter = st.sidebar.multiselect(
    "Select Your Necessary:",
    options= ["PO","Invoice"]
)

st.sidebar.markdown('---')

# ---- SIDEBAR ----
st.sidebar.header("What tools you are going to use?")
PO_letter = st.sidebar.multiselect(
    "Select Your Necessary:",
    options= ["Live Camera","Insert Picture"]
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
    key=lambda b:b[1][i], reverse=reverse))
    # return the list of sorted contours and bounding boxes
    return (cnts, boundingBoxes)


def get_letters(img):
    letters = []
    image = cv2.imread(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(gray ,127,255,cv2.THRESH_BINARY_INV)
    dilated = cv2.dilate(thresh1, None, iterations=2)

    cnts = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sort_contours(cnts, method="left-to-right")[0]
    # loop over the contours
    for c in cnts:
        if cv2.contourArea(c) > 20:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi = gray[y:y + h, x:x + w]
        thresh = cv2.threshold(roi, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        thresh = cv2.resize(thresh, (32, 32), interpolation = cv2.INTER_CUBIC)
        thresh = thresh.astype("float32") / 255.0
        thresh = np.expand_dims(thresh, axis=-1)
        thresh = thresh.reshape(1,32,32,1)
        ypred = model.predict(thresh)
        ypred = LB.inverse_transform(ypred)
        [x] = ypred
        letters.append(x)
    cam.release()
    cv2.destroyAllWindows()


def main() :
    """OCR Warehouse"""

    st.title("Streamlit Tutorial")
    html_body = """<body style="background-color:red;"> </body>"""
    st.markdown(html_body, unsafe_allow_html = True)
    html_temp = """
    <body style ="background-color:red;">
    <div style ="background-color:teal ;padding:10px">
    <h2 style = "color:white; text-align:center;"> OCR Warehouse </h2>
    </div>
    </body>
    """

    st.markdown(html_temp, unsafe_allow_html=True)

if __name__ == '__main__':
    main()

if "Live Camera" in PO_letter:
    webrtc_streamer(key="key")

image_file = None

if "Insert Picture" in PO_letter:
    image_file = st.file_uploader("Choose a file", type=['jpg', 'png', 'jpeg'])
    if image_file is not None:
        our_image = Image.open(image_file)
        st.text("Original Image")
        st.image(our_image)

if st.button("Recognise"):
    result_img = get_letters(our_image)
    st.image(result_img)

