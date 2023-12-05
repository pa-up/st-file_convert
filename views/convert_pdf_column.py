import streamlit as st
import fitz  # PyMuPDFの別名
import os
import sys

# このアプリフォルダの絶対パスを取得
this_file_abspath = os.path.abspath(sys.argv[0])
last_slash_index = this_file_abspath.rfind("/")  # 最後の '/' のインデックスを取得
this_app_root_abspath = this_file_abspath[:last_slash_index]

# 外部ファイルとの通信用ファイル
input_pdf_path = os.path.join(this_app_root_abspath, "media/pdf/input.pdf")
output_pdf_path = os.path.join(this_app_root_abspath, "media/pdf/output.pdf")


def convert_to_single_column(input_pdf, output_pdf):
    # 入力PDFを開く
    pdf_document = fitz.open(input_pdf)

    # 出力PDFを作成
    output_document = fitz.open()

    for page_number in range(pdf_document.page_count):
        # ページを取得
        page = pdf_document[page_number]

        # 新しいページを出力ドキュメントに追加
        output_page = output_document.new_page(
            width=page.rect.width, height=page.rect.height
        )

        # 左側の列のみを取得して新しいページに描画
        left_column_width = page.rect.width // 2  # ページの幅の半分を左側の列とする
        left_column_rect = fitz.Rect(
            page.rect.tl, (page.rect.tl[0] + left_column_width, page.rect.br[1])
        )
        output_page.insert_text(
            left_column_rect.tl, page.get_text("text", clip=left_column_rect)
        )

    # 出力PDFを保存
    output_document.save(output_pdf)
    output_document.close()

    # 入力PDFを閉じる
    pdf_document.close()


    


def main(page_subtitle="<h1>2列の論文pdfを1列に変換</h1><p></p>"):
    st.write(page_subtitle, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("PDFをアップロードしてください", type=["pdf"])
    if uploaded_file is not None:
        with open(input_pdf_path, "wb") as pdf_file:
            pdf_file.write(uploaded_file.read())

        convert_to_single_column(input_pdf_path, output_pdf_path)

        with open(output_pdf_path, "rb") as file:
            st.download_button("翻訳後のPDFをダウンロード", file.read(), output_pdf_path)


if __name__ == "__main__":
    main()
