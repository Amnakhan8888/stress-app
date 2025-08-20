# -*- coding: utf-8 -*-
import streamlit as st
import numpy as np

# ---------- Introduction ----------
st.title("📱 Digital Stress Scale Web App")
st.write("""
**Developer:** Amna Khan – Clinical Psychologist, Researcher, and Data Analyst

Welcome! This bilingual (Urdu + English) app will help you assess your digital stress level.
Please complete the payment to unlock the full assessment.
""")

st.markdown("""
### Introduction

This tool is based on the **Multidimensional Digital Stressor Scale (MDSS)**.
It is designed **only** for individuals aged **18 to 30 years**.
It diagnoses the **level of digital stress** you may be experiencing due to usage of devices such as mobile phones, laptops, and social media.

⚠️ **Important Notes:**
- This tool specifically measures **digital stress**, not other types of stress.
- It does **not** assess professional or work-related stress caused by using devices for your job or study.
- Please answer all questions honestly based on your experience in the **past 7 days**.
- While it is a diagnostic tool for digital stress, it should be used for **awareness and guidance**, not as a substitute for professional medical or psychological evaluation.
""")

# ---------- Part 1: Sample Questions ----------
st.subheader("Sample Questions")
sample_items = [
    ("Most of my friends approve of me being constantly available online",
     "میرے زیادہ تر دوست میرے مسلسل آن لائن رہنے سے متفق ہیں"),
    ("I feel a social obligation to be constantly available online",
     "مسلسل آن لائن رہنا مجھے ایک سماجی ذمہ داری محسوس ہوتا ہے")
]
scale_labels = ["0 - Strongly Disagree", "1 - Disagree", "2 - Neutral", "3 - Agree", "4 - Strongly Agree"]

for idx, item in enumerate(sample_items, 1):
    st.markdown(f"**Q{idx}. {item[0]}**  \n_{item[1]}_")
    st.radio("", scale_labels, key=f"sample_{idx}")

# ---------- Payment Instructions ----------
st.title("💳 Payment Instructions & Verification")

# Your payment details
EASYPaisa_NUMBER = "03290120728"  # Your Easypaisa number
MY_NAME = "Amna Khan"
EXPECTED_AMOUNT_PKR = "560"
EXPECTED_AMOUNT_USD = "2"

st.markdown(f"""
### Payment Instructions
1. Send the payment via **Easypaisa** to the following number:  
   **Number:** {EASYPaisa_NUMBER}  
   **Account Name:** {MY_NAME}
2. Amount to be sent: **{EXPECTED_AMOUNT_PKR} PKR** or **{EXPECTED_AMOUNT_USD} USD**
3. After completing the payment, you will receive a **transaction ID** from Easypaisa.
4. Enter the transaction ID below to verify your payment and unlock the full assessment.
""")

# ---------- Payment Verification ----------
if 'payment_verified' not in st.session_state:
    st.session_state['payment_verified'] = False  # Default: not verified

transaction_id = st.text_input("Enter your Easypaisa Transaction ID here:")

if st.button("Verify Payment"):
    if transaction_id:
        st.session_state['payment_verified'] = True
        st.success("✅ Payment Verified! You can now access the full assessment.")
    else:
        st.error("❌ Invalid transaction ID. Please try again.")

# ---------- Full Assessment (Hidden Until Payment Verified) ----------
if st.session_state['payment_verified']:
    st.subheader("📝 Full Digital Stress Assessment")
    st.write("Full assessment questions go here...")  # Replace with your actual questions
else:
    st.info("🔒 Full assessment is hidden. Complete payment to unlock it.")

# ---------- Full Assessment (Hidden Until Payment Verified) ----------
if st.session_state['payment_verified']:
    st.subheader("📝 Full Digital Stress Assessment")

    # All 22 items
    digital_stress_items = [
        {"id": 1, "en_text": "Most of my friends approve of me being constantly available online",
         "ur_text": "میرے زیادہ تر دوست میرے مسلسل آن لائن رہنے سے متفق ہیں"},
        {"id": 2, "en_text": "I feel a social obligation to be constantly available online",
         "ur_text": "مسلسل آن لائن رہنا مجھے ایک سماجی ذمہ داری محسوس ہوتا ہے"},
        {"id": 3, "en_text": "I am nervous about how people will respond to my posts and photos",
         "ur_text": "میں پریشان ہوتا ہوں کہ لوگ میرے پوسٹ اور تصویر کا کس طرح سے جواب دیں گے؟"},
        {"id": 4, "en_text": "I feel anxious about how others will respond when I share a new photo on social media",
         "ur_text": "میری طرف سے سوشل میڈیا پر کوئی نئی تصویر شیئر کی جاتی ہے تو مجھے بیچینی ہوتی ہے کہ دوسرے کیسے جواب دیں گے؟"},
        {"id": 5, "en_text": "I feel nervous after I share a post or photo to see how others responded to it",
         "ur_text": "مجھے پوسٹ یا تصویر کو شیئر کرنے کے بعد گھبراہٹ محسوس ہوتی ہے کہ دوسروں نے اس پر کیا ردعمل دیا ہوگا؟"},
        {"id": 6, "en_text": "I feel nervous about how others will respond when I post new updates on social media",
         "ur_text": "مجھے پریشانی محسوس ہوتی ہے کہ لوگ میرے تازہ ترین پوسٹ پر کیسے جواب دیں گے؟"},
        {"id": 7, "en_text": "I put a lot of effort into finding or creating a photo that others will approve of when I post it online",
         "ur_text": "مجھے آن لائن پوسٹ کرنے کے لیے تصویر ڈھونڈنے اور بنانے میں بہت کوشش کرنی پڑتی ہے تاکہ دوسروں کی منظوری مل سکے"},
        {"id": 8, "en_text": "I put a lot of effort into composing messages and posts I share online",
         "ur_text": "مجھے اُن پیغامات اور پوسٹ کو تیار کرنے میں بہت محنت درکار ہوتی ہے جو میں آن لائن شیئر کرتا ہوں۔"},
        {"id": 9, "en_text": "I fear my friends are having more rewarding experiences than me",
         "ur_text": "مجھے ڈر ہے کہ میرے دوستوں کے مجھ سے زیادہ خوشگوار تجربات ہیں"},
        {"id": 10, "en_text": "I fear that others have more rewarding experiences than me",
         "ur_text": "مجھے لگتا ہے کہ دوسروں کے مجھ سے زیادہ تسکین آور تجربات ہیں"},
        {"id": 11, "en_text": "I get worried when I find out my friends are having fun without me",
         "ur_text": "مجھے پریشانی ہوتی ہے جب مجھے معلوم ہوتا ہے کہ میرے دوست میرے بغیر مزہ کر رہے ہیں"},
        {"id": 12, "en_text": "I get anxious when I don’t know what my friends are up to",
         "ur_text": "مجھے پریشانی ہوتی ہے جب مجھے معلوم نہیں ہوتا کہ میرے دوست کیا کر رہے ہیں"},
        {"id": 13, "en_text": "I have to check too many notifications",
         "ur_text": "مجھے بہت زیادہ اطلاعات دیکھنی پڑتی ہیں"},
        {"id": 14, "en_text": "I feel overwhelmed with the flow of messages/notifications on my phone",
         "ur_text": "مجھے اپنے فون پر پیغامات اور اطلاعات کے مسلسل بہاؤ سے بے انتہا دباؤ محسوس ہوتا ہے"},
        {"id": 15, "en_text": "It feels like there is always a reminder—like a flashing light or buzz—that there is some other message that I need to attend to",
         "ur_text": "چمکتی روشنی یا بھنبناہٹ سے ایسا محسوس ہوتا ہے کہ کوئی دوسرا پیغام ہے جو مجھے دیکھنا ضروری ہے"},
        {"id": 16, "en_text": "I feel stress because I must sift through a lot of unimportant notifications to get to the important ones",
         "ur_text": "میں تناؤ محسوس کرتا ہوں کیونکہ مجھے اہم اطلاع تک پہنچنے کے لیے بہت ساری غیر اہم اطلاعات کو جانچنا پڑتی ہے۔"},
        {"id": 17, "en_text": "On top of the other things I must do, keeping up with notifications is a chore",
         "ur_text": "دیگر اہم کاموں کے ساتھ ساتھ اطلاعات دیکھنا بھی ایک کام ہے"},
        {"id": 18, "en_text": "I spend too much time responding to notifications/messages",
         "ur_text": "مجھے پیغامات کا جواب دینے میں بہت زیادہ وقت لگتا ہے"},
        {"id": 19, "en_text": "I must have my phone with me to know what is going on",
         "ur_text": "یہ جاننے کے لیے کہ کیا چل رہا ہے، میرے پاس میرا فون ہونا ضروری ہے"},
        {"id": 20, "en_text": "I feel lost or 'naked' without my phone",
         "ur_text": "مجھے فون کے بغیر کھویا ہوا یا خالی محسوس ہوتا ہے۔"},
        {"id": 21, "en_text": "I am constantly checking my phone for messages/notifications",
         "ur_text": "میں مسلسل اپنے فون پر پیغامات یا اطلاعات دیکھتا ہوں"},
        {"id": 22, "en_text": "I feel socially unavailable when I do not have my phone",
         "ur_text": "جب میرے پاس میرا فون نہیں ہوتا تو میں سماجی طور پر خود کو غیر دستیاب محسوس کرتا ہوں۔"}
    ]

    scale_labels = ["0 - Strongly Disagree", "1 - Disagree", "2 - Neutral", "3 - Agree", "4 - Strongly Agree"]
    responses = []

    for idx, item in enumerate(digital_stress_items, 1):
        st.markdown(f"**Q{idx}. {item['en_text']}**  \n_{item['ur_text']}_")
        score = st.radio("", scale_labels, key=f"q{idx}")
        responses.append(int(score.split(" - ")[0]))

    if st.button("Submit Full Assessment"):
        total_score = sum(responses)
        st.write(f"**Your total digital stress score: {total_score}**")

        if total_score <= 21:
            st.info("Low digital stress")
        elif total_score <= 44:
            st.info("Moderate digital stress")
        elif total_score <= 66:
            st.warning("Elevated digital stress")
        else:
            st.error("High digital stress")
else:
    st.info("🔒 Full assessment is hidden. Complete payment to unlock it.")
