import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="Dashboard Fintech",
    layout="wide"
)

st.title("Dashboard Analisis Data Fintech")
st.write("Dashboard sederhana untuk menampilkan hasil analisis data transaksi kartu kredit.")

@st.cache_data
def load_data():
    df = pd.read_csv("data_koran.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()

st.sidebar.header("Filter Dashboard")

metode_pembayaran = st.sidebar.multiselect(
    "Pilih Metode Pembayaran",
    options=df["Use Chip"].unique(),
    default=df["Use Chip"].unique()
)

status_fraud = st.sidebar.multiselect(
    "Pilih Status Fraud",
    options=df["Is Fraud?"].unique(),
    default=df["Is Fraud?"].unique()
)

df_filtered = df[
    (df["Use Chip"].isin(metode_pembayaran)) &
    (df["Is Fraud?"].isin(status_fraud))
]

st.subheader("Ringkasan Transaksi")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Pengeluaran", f"Rp {df_filtered['Amount_Rupiah'].sum():,.0f}")
col2.metric("Total Transaksi", f"{len(df_filtered):,}")
col3.metric("Rata-rata Transaksi", f"Rp {df_filtered['Amount_Rupiah'].mean():,.0f}")
col4.metric("Jumlah Fraud", df_filtered[df_filtered["Is Fraud?"] == "Yes"].shape[0])

st.divider()

monthly_expense = df_filtered.groupby(
    df_filtered["date"].dt.to_period("M")
)["Amount_Rupiah"].sum().reset_index()

monthly_expense["date"] = monthly_expense["date"].astype(str)

st.subheader("Tren Total Pengeluaran Bulanan")

fig_trend = px.line(
    monthly_expense,
    x="date",
    y="Amount_Rupiah",
    markers=True,
    title="Tren Total Pengeluaran Bulanan Pengguna"
)

fig_trend.update_layout(
    xaxis_title="Periode Bulan",
    yaxis_title="Total Pengeluaran (Rupiah)"
)

st.plotly_chart(fig_trend, use_container_width=True)

if not monthly_expense.empty:
    highest_month = monthly_expense.loc[monthly_expense["Amount_Rupiah"].idxmax()]
    lowest_month = monthly_expense.loc[monthly_expense["Amount_Rupiah"].idxmin()]

    col5, col6 = st.columns(2)

    col5.success(
        f"Pengeluaran tertinggi terjadi pada {highest_month['date']} "
        f"dengan total Rp {highest_month['Amount_Rupiah']:,.0f}"
    )

    col6.info(
        f"Pengeluaran terendah terjadi pada {lowest_month['date']} "
        f"dengan total Rp {lowest_month['Amount_Rupiah']:,.0f}"
    )

st.divider()

col7, col8 = st.columns(2)

with col7:
    st.subheader("Top 10 Kategori Transaksi MCC")

    top_mcc = df_filtered.groupby("MCC")["Amount_Rupiah"] \
        .sum() \
        .sort_values(ascending=False) \
        .head(10) \
        .reset_index()

    fig_mcc = px.bar(
        top_mcc,
        x="MCC",
        y="Amount_Rupiah",
        title="Top 10 MCC Berdasarkan Total Pengeluaran",
        text_auto=True
    )

    fig_mcc.update_layout(
        xaxis_title="Kode MCC",
        yaxis_title="Total Pengeluaran (Rupiah)"
    )

    st.plotly_chart(fig_mcc, use_container_width=True)

with col8:
    st.subheader("Distribusi Metode Pembayaran")

    payment_method = df_filtered["Use Chip"].value_counts().reset_index()
    payment_method.columns = ["Metode Pembayaran", "Jumlah Transaksi"]

    fig_payment = px.pie(
        payment_method,
        names="Metode Pembayaran",
        values="Jumlah Transaksi",
        title="Jumlah Transaksi Berdasarkan Metode Pembayaran"
    )

    st.plotly_chart(fig_payment, use_container_width=True)

st.divider()

col9, col10 = st.columns(2)

with col9:
    st.subheader("Analisis Status Fraud")

    fraud_analysis = df_filtered["Is Fraud?"].value_counts().reset_index()
    fraud_analysis.columns = ["Status Fraud", "Jumlah Transaksi"]

    fig_fraud = px.bar(
        fraud_analysis,
        x="Status Fraud",
        y="Jumlah Transaksi",
        title="Perbandingan Transaksi Fraud dan Non-Fraud",
        text_auto=True
    )

    fig_fraud.update_layout(
        xaxis_title="Status Fraud",
        yaxis_title="Jumlah Transaksi"
    )

    st.plotly_chart(fig_fraud, use_container_width=True)

with col10:
    st.subheader("Prediksi Pengeluaran Bulan Berikutnya")

    monthly_prediction = df_filtered.groupby(
        df_filtered["date"].dt.to_period("M")
    )["Amount_Rupiah"].sum().reset_index()

    monthly_prediction["Index"] = np.arange(len(monthly_prediction))

    if len(monthly_prediction) > 1:
        X = monthly_prediction[["Index"]]
        y = monthly_prediction["Amount_Rupiah"]

        model = LinearRegression()
        model.fit(X, y)

        next_month = pd.DataFrame({"Index": [len(monthly_prediction)]})
        prediction = model.predict(next_month)[0]

        st.metric(
            "Estimasi Pengeluaran Bulan Berikutnya",
            f"Rp {prediction:,.0f}"
        )

        st.write(
            "Prediksi ini menggunakan Linear Regression sederhana berdasarkan data pengeluaran bulanan."
        )
    else:
        st.warning("Data belum cukup untuk melakukan prediksi.")

st.divider()

st.subheader("Data Transaksi Fintech")

st.dataframe(df_filtered.head(100), use_container_width=True)