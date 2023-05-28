# Mengimpor library
import pandas as pd
import streamlit as st
import pickle

# Menghilangkan warning
import warnings
warnings.filterwarnings("ignore")

# Menulis judul
st.markdown("<h1 style='text-align: center; '> Prediksi Nilai Kalor Lab</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; '>PLN Indonesia Power JPR PGU</h1>", unsafe_allow_html=True)

# Pilihan utama
pilihan = st.sidebar.selectbox('Penasaran kan mau liat hasil prediksinya ?', ('Prediksi NK Lab', 'Prediksi HPH 2', 'Prediksi HPH 3'))

if pilihan == 'Prediksi NK Lab':

    st.markdown('---'*10)

    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            ks = st.number_input('Kode Shipper', value=1)
        with col2:
            NKLoading = st.number_input('Nilai Kalor Loading', value=4000)
        with col3:
            NKUnloading = st.number_input('Nilai Kalor Unloading', value=3900)

    data1 = {
        'Kode Shipper': ks,
        'Nilai kalor AR kcal/kg Loading': NKLoading,
        'Nilai kalor AR kcal/kg Unloading': NKUnloading,
    }

    kolom = list(data1.keys())
    df_final= pd.DataFrame([data1.values()], columns=kolom)

    # Load model
    my_model1 = pickle.load(open('C:\\Users\\agus.kurniawan\\model_NK.pkl', 'rb'))



    # Predict
    result = round(float(my_model1.predict(df_final)), 2)

    st.write("<center><b><h4>Prediksi Nilai Kalor Lab =", result, "</b></h4>Kcal/Kg", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; '>Kode Shipper</h4>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>1 = PT ADARO</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>2 = PT AI</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>3 = PT ARA</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>4 = PT BEK</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>5 = PT BGG</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>6 = PT BP</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>7 = PT BSR</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>8 = PT DP</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>9 = PT GEL</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>10 = PT HE</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>11 = PT HE LRC</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>12 = PT IGN</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>13 = PT KII</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>14 = PT KJA</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>15 = PT MANDIRI</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>16 = PT MIP</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>17 = PT MME</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>18= PT NLN</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>19 = PT PLNBB</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>20 = PT PLNBB LRC</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>21 = PT PLNBB NIAGA</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>22 = PT PT BA</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>23 = PT SDJ</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>24 = PT SESM</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>25= PT SPC</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>26 = PT SPE</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>27 = PT TBC</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>28 = PT TBR</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>29 = PT TIE</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>30 = PT TIE LRC</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; '>31 = PT TIE MRC</h5>", unsafe_allow_html=True)


















    st.markdown('---' * 10)
