import io
import logging
from dataclasses import dataclass
from typing import Optional

import requests
import streamlit as st
from colornet.frontend.footer import link, footer, image
from requests_toolbelt import MultipartEncoder
from htbuilder.units import px

from colornet.logging import log_decorator


@dataclass
class App:
    logger: logging.Logger
    request_url: str
    request_timeout: int
    image: Optional[io.BytesIO] = None

    @log_decorator.log_decorator()
    def request_process(self):
        m = MultipartEncoder(
            fields={"file": ("filename", self.image, "image/jpeg"), "accept": "application/json"}
        )

        r = requests.put(
            self.request_url, data=m, headers={"Content-Type": m.content_type}, timeout=self.request_timeout
        )

        return r

    @log_decorator.log_decorator()
    def display_input_img(self) -> None:
        try:
            st.image(image=self.image, caption="Original image", width=256)
        except:
            st.write(
                "An error occured when trying to display uploaded file. Please make sure it's a valid image of valid size"
            )
            raise

    @log_decorator.log_decorator()
    def request_colorization_display_result(self) -> None:
        with st.spinner("Loading..."):
            ret_image = self.request_process()

            st.image(image=ret_image.content, caption="Colorized image")

    @log_decorator.log_decorator()
    def build_table_with_io_images(self) -> None:
        col1, col2 = st.columns(2)

        if self.image is not None:
            with col1:
                self.display_input_img()
            with col2:
                self.request_colorization_display_result()

    @log_decorator.log_decorator()
    def construct_footer(self):
        args = [
            image('https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png', width=px(25), height=px(25)),
            "Checkout the ",
            link("https://github.com/Orest02/colornet", "project repo"),
            "!"
        ]

        footer(*args)

    @log_decorator.log_decorator()
    def run(self):
        st.title("Photo colorization app")

        self.image = st.file_uploader("Upload an image")

        try:
            self.build_table_with_io_images()
        finally:
            self.construct_footer()
