from PIL import Image
import pytesseract
import streamlit as st

LANGS = pytesseract.get_languages()

import script

st.set_page_config(
    page_title="Extract Details from ID Card"
)



def main():
    st.title("Document Classifier - Sasank Chowdary")

    st.markdown("<hr>", True)
    

    file = st.file_uploader(
        "Upload an image", ["png", "jpg", "jpeg", "webp", "bmp"]
    )


    # lang = st.selectbox("Select language :", LANGS)

    submit_button = st.button("Process")

    outputCont = st.container()

    st.divider()

    cont = st.container()
    cont.markdown('<h2>PowerBI Dashboard</h2><br><iframe title="Sasank - Documet classification" width="700" height="441.25" src="https://app.powerbi.com/reportEmbed?reportId=d6a3f8cb-7569-47ec-beaf-f9518daa2fa0&autoAuth=true&ctid=1159260e-bcda-43c8-b300-45899ea8600f" frameborder="0" allowFullScreen="true"></iframe>', True)

    if file  and submit_button:
        name, gender, ayear, uid = script.fetchData(file)

        outputCont.markdown("<h2>Fetched Data from the uploaded document : </h2>", True)
        outputCont.markdown("<ul><li>NAME : "+str(name)+"</li>", True)
        outputCont.markdown("<ul><li>GENDER : "+str(gender)+"</li>", True)
        outputCont.markdown("<ul><li>AGE : "+str(ayear)+"</li>", True)
        outputCont.markdown("<ul><li>ID : "+str(uid)+"</li></ul>", True)

    # show select for lang

    st.markdown("<hr>", True)





if __name__ == "__main__":
    main()