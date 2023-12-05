import streamlit as st
import numpy as np
import os
import sys
from views import google_translate, convert_pdf_column

st.title("ファイルの変換・翻訳")
st.write("\n")

# このアプリフォルダの絶対パスを取得
this_file_abspath = os.path.abspath(sys.argv[0])
last_slash_index = this_file_abspath.rfind("/")  # 最後の '/' のインデックスを取得
this_app_root_abspath = this_file_abspath[:last_slash_index]
# 外部ファイルとの通信用ファイル
async_np_file = os.path.join(this_app_root_abspath, "media/async/recognition.npz")


def change_page(page):
    st.session_state["page"] = page


def index_page():
    page_subtitle = "<p></p><h3>目次</h3><p></p>"
    st.write(page_subtitle, unsafe_allow_html=True)
    st.button("google翻訳はこちら >", on_click=change_page, args=["google_translate_page"])
    st.button(
        "2列の論文pdfを1列に変換はこちら >", on_click=change_page, args=["convert_pdf_column_page"]
    )


def google_translate_page():
    # 別ページへの遷移
    st.write("\n")
    page_subtitle = "<h3>google翻訳</h3><p></p>"
    st.write(page_subtitle, unsafe_allow_html=True)
    st.write("<p>アップロード方法を選択</p>", unsafe_allow_html=True)

    st.button("テキストを入力 >", on_click=change_page, args=["translate_text_page"])
    st.button("Wordをアップロード >", on_click=change_page, args=["translate_word_page"])
    st.button("PDFをアップロード >", on_click=change_page, args=["translate_pdf_page"])
    st.button("PowerPointをアップロード >", on_click=change_page, args=["translate_pptx_page"])


def translate_text_page():
    st.button("アップロード方法を再選択 >", on_click=change_page, args=["google_translate_page"])
    page_subtitle = "<h3>テキストをgoogle翻訳</h3><p></p>"
    google_translate.main(page_subtitle, "text")


def translate_word_page():
    st.button("アップロード方法を再選択 >", on_click=change_page, args=["google_translate_page"])
    page_subtitle = "<h3>Wordをgoogle翻訳</h3><p></p>"
    google_translate.main(page_subtitle, "word")


def translate_pdf_page():
    st.button("アップロード方法を再選択 >", on_click=change_page, args=["google_translate_page"])
    page_subtitle = "<h3>PDFをgoogle翻訳</h3><p></p>"
    google_translate.main(page_subtitle, "pdf")


def translate_pptx_page():
    st.button("アップロード方法を再選択 >", on_click=change_page, args=["google_translate_page"])
    page_subtitle = "<h3>PowerPointをgoogle翻訳</h3><p></p>"
    google_translate.main(page_subtitle, "pptx")


def convert_pdf_column_page():
    # st.button("別ページ >", on_click=change_page, args=["other_page"])
    page_subtitle = "<h3>2列の論文pdfを1列に変換</h3><p></p>"
    convert_pdf_column.main(page_subtitle)


# メイン
def main():
    # セッション状態を取得
    session_state = st.session_state

    # セッション状態によってページを表示
    if "page" not in session_state:
        session_state["page"] = "index_page"

    if session_state["page"] == "index_page":
        index_page()
    else:
        st.button("目次はこちら >", on_click=change_page, args=["index_page"])
    if session_state["page"] == "google_translate_page":
        google_translate_page()
    if session_state["page"] == "translate_text_page":
        translate_text_page()
    if session_state["page"] == "translate_word_page":
        translate_word_page()
    if session_state["page"] == "translate_pdf_page":
        translate_pdf_page()
    if session_state["page"] == "translate_pptx_page":
        translate_pptx_page()
    if session_state["page"] == "convert_pdf_column_page":
        convert_pdf_column_page()


if __name__ == "__main__":
    main()
