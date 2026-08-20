
import streamlit as st

st.set_page_config(
    page_title="My Business App",
    page_icon="📦"
)

st.title("📦 My Business App")
st.write("Welcome to my business app!")

menu = st.sidebar.selectbox(
    "Menu",
    ["Home", "Products", "Order", "Contact"]
)

if menu == "Home":
    st.header("🏠 Home")
    st.write("Welcome to our business!")

elif menu == "Products":
    st.header("📦 Products")

    st.write("Product 1 — ₹500")
    st.write("Product 2 — ₹800")
    st.write("Product 3 — ₹1200")

elif menu == "Order":
    st.header("🛒 Place Your Order")

    name = st.text_input("Customer Name")
    phone = st.text_input("Phone Number")
    address = st.text_area("Delivery Address")

    product = st.selectbox(
        "Select Product",
        ["Product 1 - ₹500", "Product 2 - ₹800", "Product 3 - ₹1200"]
    )

    quantity = st.number_input("Quantity", min_value=1, value=1)

    if st.button("✅ Place Order"):
        if name and phone and address:
            st.success("🎉 Order Placed Successfully!")
            st.write("Name:", name)
            st.write("Phone:", phone)
            st.write("Address:", address)
            st.write("Product:", product)
            st.write("Quantity:", quantity)
        else:
            st.warning("Please fill all details.")

elif menu == "Contact":
    st.header("📞 Contact Us")
    st.write("Phone: +91 XXXXX XXXXX")
    st.write("Email: business@example.com")

    st.subheader("📍 Address")
    st.write("Khalilabad, Uttar Pradesh, India
    import streamlit as st

st.set_page_config(
    page_title="My Business App",
    page_icon="📦"
)

st.title("📦 My Business App")
st.write("Welcome to My Business App")

menu = st.selectbox(
    "Menu",
    ["Home", "Products", "Contact"]
)

if menu == "Home":
    st.header("🏠 Home")
    st.write("Welcome to our business app.")

elif menu == "Products":
    st.header("📦 Products")

    product = st.selectbox(
        "Select Product",
        [
            "Product 1 - ₹500",
            "Product 2 - ₹800",
            "Product 3 - ₹1200"
        ]
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        value=1
    )

    name = st.text_input("Name")
    phone = st.text_input("Phone")
    address = st.text_area("Address")

    if st.button("Place Order"):
        if name and phone and address:
            st.success("Order not Placed Successfully!")
            st.write("Name:", name)
            st.write("Phone:", phone)
            st.write("Address:", address)
            st.write("Product:", product)
            st.write("Quantity:", quantity)
        else:
            st.warning("Please fill all details.")

elif menu == "Contact":
    st.header("📞 Contact Us")
    st.write("Phone: +91 XXXXXXXXXX")
    st.write("Email: business@example.com")

    st.subheader("📍 Address")
    st.write("Khalilabad, Uttar Pradesh, India")
