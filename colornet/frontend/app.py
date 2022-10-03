import time

import requests
import streamlit as st
from requests_toolbelt.multipart.encoder import MultipartEncoder


def request_process(image, server_url: str):
    m = MultipartEncoder(fields={"file": ("filename", image, "image/jpeg"),
                                 'accept': 'application/json'
                                 }
                         )

    r = requests.put(
        server_url, data=m, headers={"Content-Type": m.content_type}, timeout=8000
    )

    return r


def main():
    st.title("Photo colorization app")

    # image = None
    image = st.file_uploader("Upload an image")

    col1, col2 = st.columns(2)

    if image is not None:
        with col1:

            try:
                st.image(image=image, caption="Original image", width=256)
            except:
                st.write(
                    "An error occured when trying to display uploaded file. Please make sure it's a valid image of valid size")
                return None

        with col2:
            with st.spinner("Loading..."):
                ret_image = request_process(image, 'http://127.0.0.1:8000/transform')

                st.image(image=ret_image.content, caption="Colorized image")


if __name__ == '__main__':
    main()
