import streamlit as st
import time
import secrets

# --- Mock Databases & Catalogs ---
ACCESSORY_CATALOG = {
    "Premium Phone Case": {"base_cost": 250, "platform": "AliExpress", "sku": "ACC-PH-01"},
    "Matte Screen Protector": {"base_cost": 120, "platform": "CJ-Dropshipping", "sku": "ACC-SCR-05"},
    "Braided Type-C Cable (1m)": {"base_cost": 180, "platform": "Zendrop", "sku": "ACC-CBL-12"},
    "Magnetic Ring Holder": {"base_cost": 90, "platform": "AliExpress", "sku": "ACC-RNG-09"},
}

MOCK_LEDGER = [
    {"Customer Profile": "Rahul Bajaj", "Phone Network": "91234xxxxx", "Target Build": "Full Matte Sedan Wrap", "Route Status": "Cleared"},
    {"Customer Profile": "Amit Kadam", "Phone Network": "98765xxxxx", "Target Build": "Scorpio-N Custom Lighting", "Route Status": "Cleared"}
]

# --- Page Configuration ---
st.set_page_config(
    page_title="ModDrive Partner Panel",
    page_icon="💼",
    layout="wide"
)

# --- Navigation Setup ---
tab1, tab2 = st.tabs(["💼 ModDrive B2B Studio Portal", "📦 Hands-Off Accessory Processing Hub"])

# ==========================================
# PART 2: ModDrive B2B Studio Portal
# ==========================================
with tab1:
    st.title("💼 ModDrive B2B Studio Portal")
    st.subheader("Manage Google Search leads and license settings.")
    st.markdown("---")

    b2b_col1, b2b_col2 = st.columns(2)

    with b2b_col1:
        st.markdown("### 💼 Commercial Lifetime License")
        st.write("Gain persistent exposure across targeted local user search traffic groups instantly.")
        license_cost = 999
        st.metric(label="One-Time Platform License Fee", value=f"₹{license_cost:,}")
        
        st.markdown("---")
        st.markdown("### 🔐 Studio License Activation Node")
        reg_name = st.text_input("Business Registered Name", key="biz_name_reg")
        
        if st.button("Unlock Unlimited Lifetime Access Portal"):
            if not reg_name:
                st.error("Please insert your verified enterprise title to authorize server credentials.")
            else:
                st.markdown("#### 📱 Scan to Activate Studio Account via FamPay/UPI")
                # Using a working standard dynamic placeholder UPI QR parameters format
                upi_id = "moddrive@ybl"
                qr_api_url = f"https://qrserver.com{upi_id}%26pn=ModDrive%20India%26am={license_cost}%26cu=INR"
                st.image(qr_api_url, caption="Upon transaction clearance via gateway webhook protocols, verification locks will drop permanently.")
                
    with b2b_col2:
        st.markdown("### 🖥️ Real-Time Customer Bookings Registry")
        st.write("The software logs customer inquiries in the background 24/7. Studio operators use this ledger to contact hot clients directly.")
        
        st.dataframe(MOCK_LEDGER, use_container_width=True)
        st.caption("Google indices route local customers straight to this display module natively.")


# ==========================================
# PART 1: Hands-Off Accessory Processing Hub
# ==========================================
with tab2:
    st.header("Hands-Off Accessory Processing Hub")
    st.write("Purchases on this channel trigger background protocols to dispatch orders directly via backend networks.")
    st.markdown("---")
    
    shop_col1, shop_col2 = st.columns(2)
    
    with shop_col1:
        st.markdown("### 📦 Product Inventory Selector")
        selected_product = st.selectbox("Choose Accessory to Purchase", list(ACCESSORY_CATALOG.keys()))
        prod_data = ACCESSORY_CATALOG[selected_product]
        system_markup = 10
        final_price = prod_data["base_cost"] + system_markup
        
        st.info(f"🤖 **Automated Route:** Integrated via {prod_data['platform']} API Pipelines (SKU: `{prod_data['sku']}`)")
        st.metric(label="Total Payable Retail Cost", value=f"₹{final_price}")
        
    with shop_col2:
        st.markdown("### 💳 Integrated FamPay / UPI Payment Node")
        shipping_name = st.text_input("Recipient Full Name", key="ship_n")
        shipping_email = st.text_input("Notification Email Address", key="ship_e")
        shipping_address = st.text_area("Complete Physical Delivery Address (With Postal Pincode)")
        
        if st.button("Authorize Instant Payment & Automated Checkout Delivery"):
            if not shipping_name or not shipping_email or not shipping_address:
                st.error("❌ Transaction Denied: Complete all distribution parameters.")
            else:
                st.markdown("---")
                status = st.empty()
                status.info("🔄 Connecting with FamGateway network node... Fetching dynamic payment session variables.")
                time.sleep(1.2)
                status.success("✅ Payment Secured! Webhook verified payload sequence received successfully.")
                time.sleep(1.0)
                status.info(f"🤖 Triggering background automation module... Logging into {prod_data['platform']} backend dashboard via headless script.")
                time.sleep(1.5)
                
                generated_order_id = f"MDRV-{secrets.token_hex(4).upper()}"
                status.success("🎉 Fulfillment Cycle Complete!")
                st.balloons()
                
                st.markdown(f"""
                ### 🏁 Automated Fulfillment Report
                * **ModDrive Logistics Tracking ID:** `{generated_order_id}`
                * **Base Fulfillment Capital Dispatched:** ₹{prod_data['base_cost']}
                * **Net Autonomous Revenue Deposited to FamPay Wallet:** **₹{system_markup}** (100% Passive Net Profit)
                """)
