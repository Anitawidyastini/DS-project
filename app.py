import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="OCR Receipt Dashboard",
    page_icon="📄",
    layout="wide"
)

# ==========================
# LOAD DATA
# ==========================
df = pd.read_csv("ocr_bersih.csv")

# ==========================
# SIDEBAR
# ==========================
st.sidebar.title("OCR Dashboard")

menu = st.sidebar.radio(
    "Pilih Menu",
    ["Dashboard", "Dataset"]
)

# ==========================
# DASHBOARD
# ==========================
if menu == "Dashboard":

    st.title("OCR Receipt Analytics Dashboard")

    st.markdown("""
    Dashboard ini digunakan untuk menganalisis hasil ekstraksi OCR dari dataset receipt.
    Data telah melalui proses OCR, preprocessing, cleaning, dan transformasi mata uang dari Dollar ke Rupiah.
    """)

    # ==========================
    # METRICS
    # ==========================
    total_data = len(df)

    avg_transaksi = int(
        df["total_amount_rupiah"].mean()
    )

    max_transaksi = int(
        df["total_amount_rupiah"].max()
    )

    total_rupiah = int(
        df["total_amount_rupiah"].sum()
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Jumlah Receipt",
            total_data
        )

    with col2:
        st.metric(
        "Rata-rata Transaksi",
        f"Rp {avg_transaksi/1_000_000:.2f} Jt"
    )
        
    with col3:
        st.metric(
        "Total Transaksi",
        f"Rp {total_rupiah/1_000_000:.2f} Jt"
    )
        
    with col4:
        st.metric(
        "Transaksi Tertinggi",
        f"Rp {max_transaksi/1_000_000:.2f} Jt"
    )

    st.divider()

    # ==========================# 
    # TOP 10 CHART # 
    # ==========================#
    
    st.subheader("📈 Top 10 Transaksi Terbesar")
    top10 = (
        df.sort_values(
            by="total_amount_rupiah",
            ascending=False
            )
            .head(10)
            )
    fig, ax = plt.subplots(figsize=(10, 5))
    
    ax.bar(
        top10["image_name"],
        top10["total_amount_rupiah"]
        )
    
    plt.xticks(
        rotation=45,
        ha="right"
        )
    
    ax.set_title(
        "Top 10 Transaksi Terbesar"
        )
    
    ax.set_xlabel(
        "Nama Receipt"
        )
    
    ax.set_ylabel(
        "Nominal Rupiah"
        )
    
    st.pyplot(fig)
    
    st.divider()

    # ==========================
    # TOP 10
    # ==========================
    st.subheader("🏆 Top 10 Transaksi Terbesar")

    top10 = (
        df.sort_values(
            by="total_amount_rupiah",
            ascending=False
        )
        .head(10)
    )

    st.dataframe(
        top10[
            [
                "image_name",
                "total_amount_rupiah"
            ]
        ],
        use_container_width=True
    )

    st.divider()

    # ==========================
    # MISSING VALUE
    # ==========================
    st.subheader("✅ Kualitas Data")

    missing = df.isnull().sum().sum()

    if missing == 0:
        st.success(
            "Tidak ditemukan missing value pada dataset."
        )
    else:
        st.warning(
            f"Ditemukan {missing} missing value."
        )

# ==========================
# DATASET
# ==========================
elif menu == "Dataset":

    st.title("Dataset OCR Receipt")

    st.subheader("Preview Dataset")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader("Informasi Dataset")
    info_df = pd.DataFrame({
        "Nama Kolom": df.columns,
        "Tipe Data": df.dtypes.values.astype(str)
        })
    
    st.dataframe(
        info_df,
        hide_index=True,
        use_container_width=True
        )

    st.subheader("Missing Value")

    missing_df = (
        df.isnull()
        .sum()
        .reset_index()
        .rename(
            columns={
                "index": "Kolom",
                0: "Jumlah Missing"
            }
        )
    )

    st.dataframe(
        missing_df,
        use_container_width=True
    )

    st.subheader("Statistik Deskriptif")

    st.dataframe(
        df[
            [
                "total_amount_dollar",
                "total_amount_rupiah"
            ]
        ].describe(),
        use_container_width=True
    )

    # FILTER
    st.subheader("🔍 Filter Nominal Transaksi")

    min_amount = int(
        df["total_amount_rupiah"].min()
    )

    max_amount = int(
        df["total_amount_rupiah"].max()
    )

    selected_range = st.slider(
        "Pilih Rentang Nominal",
        min_amount,
        max_amount,
        (min_amount, max_amount)
    )

    filtered_df = df[
        (
            df["total_amount_rupiah"]
            >= selected_range[0]
        )
        &
        (
            df["total_amount_rupiah"]
            <= selected_range[1]
        )
    ]

    st.dataframe(
        filtered_df,
        use_container_width=True
    )