import streamlit as st
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_travel_request_email(summary, receiver_email):
    SENDER_EMAIL = "mohamed.bahaa.saadawy@gmail.com"
    SENDER_PASSWORD = "jjbm hvni xltv ucqw"
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587

    subject = "New Travel Request Submitted"
    # Format summary for email (simple text, or you can use HTML)
    body = f"New travel request received:\n\n{summary}"

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print("Error sending email:", e)
        return False

st.set_page_config(page_title="Travel Request Form", layout="centered")

st.title("Travel Request Form")
st.write("Please fill in the travel request form. This should be done at least 2 weeks ahead of your trip.")

# --- SECTION 2: Traveler Info ---
st.header("Traveler's Info")
name = st.text_input("Traveler name *")
mobile = st.text_input("Traveler Mobile number *")
department = st.selectbox("Department *", [
    "Sales & Business", "Customer Care", "Operations", "HR", "Finance", "R&D"
])
passport = st.text_input("Traveler Passport Number *")
travel_purpose = st.selectbox("Travel purpose *", [
    "Sales / Business", "Implementation", "Training", "Support", "Conference"
])
zone = st.selectbox("Zone Area *", ["Zone 1", "Zone 2", "Zone 3"])
customers = st.text_area("Please list the customers' name(s) to be visited *")
brex = st.radio("Do you have Brex card?", ["Yes", "No"])
prob_change = st.radio("For this booking request, what is the probability of flight / accommodation changes?",
                       ["To be changed >50%", "to be changed <50%"])
manager_approval = st.text_area("Please add your manager approval & advance claim if applicable *")

# --- SECTION 3: Travel Zone ---
st.header("Travel Zone")
travel_zone = st.radio("The Travel for your trip is *", ["Domestic", "International"])
flight_data = []
hotel_data = []
# ---------- DOMESTIC ----------
if travel_zone == "Domestic":
    st.header("Domestic Travel")
    booking_type = st.selectbox("Required Booking *", [
        "Train Booking only", "Flight Booking only", "Hotel Reservation only",
        "Train & Hotel reservation", "Flight & Hotel reservation"
    ])

    if booking_type == "Train Booking only":
        st.subheader("Train Booking Only")
        dom_travel_date = st.date_input("Travel Date *")
        dom_travel_time = st.time_input("Travel Time *")
        dom_arrival_date = st.date_input("Arrival Date *")
        dom_arrival_time = st.time_input("Arrival Time *")
        dom_from = st.text_input("From (City, Country) *")
        dom_to = st.text_input("To (City, Country) *")
        dom_note = st.text_area("Special Note")

    elif booking_type == "Flight Booking only":
        st.subheader("Flight Booking Only")
        dom_travel_date = st.date_input("Travel Date *")
        dom_travel_time = st.time_input("Travel Time *")
        dom_arrival_date = st.date_input("Arrival Date *")
        dom_arrival_time = st.time_input("Arrival Time *")
        dom_from = st.text_input("From (City, Country) *")
        dom_to = st.text_input("To (City, Country) *")
        dom_note = st.text_area("Special Note")

    elif booking_type == "Hotel Reservation only":
        st.subheader("Hotel Reservation Only")
        dom_check_in = st.date_input("Check-in Date *")
        dom_check_in_time = st.time_input("Check-in Time *")
        dom_check_out = st.date_input("Check-out Date *")
        dom_check_out_time = st.time_input("Check-out Time *")
        dom_nights = st.number_input("Number of nights *", min_value=1, step=1)
        dom_hotel_area = st.text_input("Hotel area / landmark *")
        dom_note = st.text_area("Special Note")

    elif booking_type == "Train & Hotel reservation":
        st.subheader("Train & Hotel Reservation")
        dom_travel_date = st.date_input("Travel Date *")
        dom_travel_time = st.time_input("Travel Time *")
        dom_arrival_date = st.date_input("Arrival Date *")
        dom_arrival_time = st.time_input("Arrival Time *")
        dom_from = st.text_input("From (City, Country) *")
        dom_to = st.text_input("To (City, Country) *")
        dom_check_in = st.date_input("Check-in Date *")
        dom_check_in_time = st.time_input("Check-in Time *")
        dom_check_out = st.date_input("Check-out Date *")
        dom_check_out_time = st.time_input("Check-out Time *")
        dom_nights = st.number_input("Number of nights *", min_value=1, step=1)
        dom_hotel_area = st.text_input("Hotel area / landmark *")
        dom_note = st.text_area("Special Note")

    elif booking_type == "Flight & Hotel reservation":
        st.subheader("Flight & Hotel Reservation")
        dom_travel_date = st.date_input("Travel Date *")
        dom_travel_time = st.time_input("Travel Time *")
        dom_arrival_date = st.date_input("Arrival Date *")
        dom_arrival_time = st.time_input("Arrival Time *")
        dom_from = st.text_input("From (City, Country) *")
        dom_to = st.text_input("To (City, Country) *")
        dom_check_in = st.date_input("Check-in Date *")
        dom_check_in_time = st.time_input("Check-in Time *")
        dom_check_out = st.date_input("Check-out Date *")
        dom_check_out_time = st.time_input("Check-out Time *")
        dom_nights = st.number_input("Number of nights *", min_value=1, step=1)
        dom_hotel_area = st.text_input("Hotel area / landmark *")
        dom_note = st.text_area("Special Note")

# ---------- INTERNATIONAL ----------
if travel_zone == "International":
    st.header("International Travel")
    intl_booking_type = st.selectbox("Required Booking *", [
        "Flight Booking only", "Hotel Reservation only", "Flight & Hotel reservation"
    ])
    cities_count = st.selectbox("How many cities are you planning to visit?", [
        "1 city", "2 cities", "3 cities", "More than 3 cities"
    ])

    def city_flight_inputs(idx):
        st.markdown(f"**Flight ({idx})**")
        from_city = st.text_input(f"Flight ({idx}) - From (City, Country) *", key=f"from_{idx}")
        to_city = st.text_input(f"Flight ({idx}) - To (City, Country) *", key=f"to_{idx}")
        date = st.date_input(f"Flight ({idx}) - Preferred schedule (Date) *", key=f"date_{idx}")
        time = st.time_input(f"Flight ({idx}) - Preferred schedule (Time) *", key=f"time_{idx}")
        return {"from": from_city, "to": to_city, "date": date, "time": time}

    def city_hotel_inputs(idx):
        st.markdown(f"**Hotel ({idx})**")
        city = st.text_input(f"Hotel ({idx}) - City, Country *", key=f"hotel_city_{idx}")
        checkin = st.date_input(f"Hotel ({idx}) - Check-in Date *", key=f"checkin_{idx}")
        checkin_time = st.time_input(f"Hotel ({idx}) - Check-in Time *", key=f"checkin_time_{idx}")
        checkout = st.date_input(f"Hotel ({idx}) - Check-out Date *", key=f"checkout_{idx}")
        checkout_time = st.time_input(f"Hotel ({idx}) - Check-out Time *", key=f"checkout_time_{idx}")
        nights = st.number_input(f"Hotel ({idx}) - Number of nights *", min_value=1, step=1, key=f"nights_{idx}")
        area = st.text_input(f"Hotel ({idx}) - Area / Landmark *", key=f"hotel_area_{idx}")
        return {"city": city, "checkin": checkin, "checkin_time": checkin_time, "checkout": checkout, "checkout_time": checkout_time, "nights": nights, "area": area}

    flight_data = []
    hotel_data = []

    if intl_booking_type == "Flight Booking only":
        if cities_count == "1 city":
            flight_data.append(city_flight_inputs(1))
            special_notes = st.text_area("Special Notes")
        elif cities_count == "2 cities":
            flight_data.append(city_flight_inputs(1))
            flight_data.append(city_flight_inputs(2))
            special_notes = st.text_area("Special Notes")
        elif cities_count == "3 cities":
            for i in range(1, 4):
                flight_data.append(city_flight_inputs(i))
            special_notes = st.text_area("Special Notes")
        else: # More than 3 cities
            for i in range(1, 5):
                flight_data.append(city_flight_inputs(i))
            detailed_itinerary = st.text_area("Please provide a detailed itinerary for your trip")

    if intl_booking_type == "Hotel Reservation only":
        if cities_count == "1 city":
            hotel_data.append(city_hotel_inputs(1))
        elif cities_count == "2 cities":
            hotel_data.append(city_hotel_inputs(1))
            hotel_data.append(city_hotel_inputs(2))
            special_notes = st.text_area("Special Notes")
        elif cities_count == "3 cities":
            for i in range(1, 4):
                hotel_data.append(city_hotel_inputs(i))
            special_notes = st.text_area("Special Notes")
        else:
            for i in range(1, 4):
                hotel_data.append(city_hotel_inputs(i))
            detailed_itinerary = st.text_area("Please provide a detailed itinerary for your trip")

    if intl_booking_type == "Flight & Hotel reservation":
        if cities_count == "1 city":
            flight_data.append(city_flight_inputs(1))
            hotel_data.append(city_hotel_inputs(1))
        elif cities_count == "2 cities":
            for i in range(1, 3):
                flight_data.append(city_flight_inputs(i))
                hotel_data.append(city_hotel_inputs(i))
            special_notes = st.text_area("Special Notes")
        elif cities_count == "3 cities":
            for i in range(1, 4):
                flight_data.append(city_flight_inputs(i))
                hotel_data.append(city_hotel_inputs(i))
            special_notes = st.text_area("Special Notes")
        else:
            for i in range(1, 5):
                flight_data.append(city_flight_inputs(i))
                hotel_data.append(city_hotel_inputs(i))
            detailed_itinerary = st.text_area("Please provide a detailed itinerary for your trip")
import json

if st.button("Submit Request", key="submit_request_button"):
    summary_dict = {
        "Name": name,
        "Mobile": mobile,
        "Department": department,
        "Passport": passport,
        "Travel Purpose": travel_purpose,
        "Zone": zone,
        "Customers": customers,
        "Brex Card": brex,
        "Change Probability": prob_change,
        "Manager Approval": manager_approval,
        "Travel Zone": travel_zone,
        "Domestic/International Details": {
            "Booking Type": locals().get("booking_type", locals().get("intl_booking_type")),
            "Flights": flight_data if flight_data else None,
            "Hotels": hotel_data if hotel_data else None,
        },
    }

    st.success("Travel Request Submitted!")
    st.write("**Summary:**")
    st.json(summary_dict)

    # Convert summary dict to text for email (dates/times handled as strings)
    summary_text = json.dumps(summary_dict, indent=2, default=str)

    # === Send Email ===
    RECEIVER_EMAIL = "mohamed.bahaa@paxerahealth.com"
    sent = send_travel_request_email(summary_text, RECEIVER_EMAIL)
    if sent:
        st.success("Email sent to travel admin!")
    else:
        st.error("Failed to send email. Check your credentials and SMTP settings.")
