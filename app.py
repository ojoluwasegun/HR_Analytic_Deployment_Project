import joblib
import pandas as pd
import streamlit as st

@st.cache_data
def load_model():
    return joblib.load('hr_attrition_model.pkl')

model = load_model()


st.set_page_config(
    page_title="HR Predictive Management System",
    page_icon='HR',
    layout='wide'

)

st.title("HR Predictive Management System")
st.write("Predict Employee Attrition Risk using your saved ML model")


col1, col2 = st.columns(2)



with col1:
    satisfaction_level = st.number_input("Satisfaction Level", 0.0, 100.0, 38.0)
    last_evaluation = st.number_input("Last Evaluation", 0.0, 100.0, 38.0)
    number_project = st.number_input("Number of Projects", 1, 10, 2)
    average_montly_hours = st.number_input("Average Monthly Hour", 50, 400, 157)
    time_spend_company = st.number_input("Time Spent in Company", 1, 20, 3)
    Work_accident = st.selectbox("Work Accident", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")


with col2:
    promotion_last_5years = st.selectbox("Promotion in last 5yrs", [0,1],
                                            format_func=lambda x: "Yes" if x == 1 else "No")
    Department = st.selectbox("Department", ["sales", "technical", "support", "IT", "product",
                                             "marketing", "RanD", "accounting", "HR", "Management"])   
    salary = st.selectbox("Salary", ["Low", "Medium", "High"])
    overworked = st.selectbox("Overworked", ["No", "Yes"])
    satisfaction = st.selectbox("Satisfaction Level", ["Low", "Medium", "High"])

input_data = pd.DataFrame([{
    "satisfaction_level": satisfaction_level,
    "last_evaluation": last_evaluation,
    "number_project": number_project,
    "average_montly_hours": average_montly_hours,
    "time_spend_company": time_spend_company,
    "Work_accident": Work_accident,
    "promotion_last_5years": promotion_last_5years,
    "Department": Department,
    "salary": salary,
    "overworked": overworked,
    "satisfaction": satisfaction
}])




if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    percent = round(probability * 100, 2)
    status = "Left" if prediction == 1 else "Stayed"
    col1, col2 = st.columns(2)

    
    st.markdown("#### Prediction Result")
    with col1:
        st.metric("#### Attrition Status", status)
    with col2:
        st.metric("#### Attrition Probability", f"{percent:.1f}%")
    st.progress(int(percent))

    if percent < 40:
        st.success("Low Attrition Risk")
        st.success("Recommendation: Employee is likely stable. Continue Engagement and recognition")
    elif percent < 70:
        st.write("Medium Attrition Risk (at Benchmark)")
        st.write("Recommendation: Monitor Employee Satisfaction, Workload, Manager Feedback and growth opportunity")
    else:
        st.warning("Recommendation: Immediate HR action recommendation. Review workload, compensation, promotion path  and retention plan.")
    
    st.subheader("Employee Input Preview")
    st.dataframe(input_data, width='content')
 def generate_pdf_from_html(html_content):
        pdf_buffer = BytesIO()
        pisa.CreatePDF(html_content, dest=pdf_buffer)
        pdf_buffer.seek(0)
        return pdf_buffer

    recommendation = (
        "Employee is likely stable. Continue engagement, recognition, and career support."
        if percent < 40 else
        "Monitor employee satisfaction, workload, manager feedback, and growth opportunities."
        if percent < 70 else
        "Immediate HR intervention is recommended. Review workload, compensation, promotion path, and retention plan."
    )

    risk_level = (
        "Low Attrition Risk"
        if percent < 40 else
        "Medium Attrition Risk"
        if percent < 70 else
        "High Attrition Risk"
    )

    html_report = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            @page {{
                size: A4;
                margin: 30px;
            }}

            body {{
                font-family: Arial, sans-serif;
                color: #222;
                font-size: 12px;
                line-height: 1.6;
            }}

            .header {{
                text-align: center;
                border-bottom: 3px solid #003366;
                padding-bottom: 12px;
                margin-bottom: 25px;
            }}

            .hospital-name {{
                font-size: 22px;
                font-weight: bold;
                color: #003366;
            }}

            .contact {{
                font-size: 11px;
                color: #555;
            }}

            .report-title {{
                text-align: center;
                font-size: 18px;
                font-weight: bold;
                color: #003366;
                margin-top: 20px;
                margin-bottom: 20px;
                text-transform: uppercase;
            }}

            .section-title {{
                background-color: #003366;
                color: white;
                padding: 6px;
                font-size: 13px;
                font-weight: bold;
                margin-top: 18px;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 8px;
                margin-bottom: 15px;
            }}

            td, th {{
                border: 1px solid #ccc;
                padding: 7px;
                font-size: 11px;
            }}

            th {{
                background-color: #f0f4f8;
                font-weight: bold;
            }}

            .result-box {{
                border: 2px solid #003366;
                padding: 12px;
                text-align: center;
                margin: 20px 0;
                background-color: #f8fbff;
            }}

            .result {{
                font-size: 20px;
                font-weight: bold;
                color: #b30000;
            }}

            .signature {{
                margin-top: 35px;
            }}

            .disclaimer {{
                margin-top: 25px;
                font-size: 10px;
                color: #555;
                border-top: 1px solid #ccc;
                padding-top: 10px;
            }}

            .footer {{
                text-align: center;
                font-size: 10px;
                color: #777;
                margin-top: 25px;
            }}
        </style>
    </head>

    <body>

        <div class="header">
            <div class="hospital-name">ABC Corporate Health & HR Analytics Centre</div>
            <div class="contact">
                12 Enterprise Avenue, Lagos, Nigeria<br>
                Phone: +234 800 123 4567 | Email: hr@abccorp.com
            </div>
        </div>

        <div class="report-title">
            HR Predictive Analytics Report
        </div>

        <div class="section-title">Employee Information</div>

        <table>
            <tr>
                <td><b>Employee Name</b></td>
                <td>Employee User</td>
                <td><b>Employee ID</b></td>
                <td>EMP/2026/HR/0036</td>
            </tr>
            <tr>
                <td><b>Department</b></td>
                <td>{Department}</td>
                <td><b>Requesting Unit</b></td>
                <td>Human Resource Department</td>
            </tr>
            <tr>
                <td><b>Consultant</b></td>
                <td>HR Analytics Unit</td>
                <td><b>Report Type</b></td>
                <td>Attrition Risk Assessment</td>
            </tr>
        </table>

        <p>
            Dear Employee User,
        </p>

        <p>
            This report presents the findings from an automated employee attrition risk analysis
            using a machine learning-based HR Predictive Analytics System.
        </p>

        <div class="section-title">Prediction Result</div>

        <div class="result-box">
            <p>Based on the submitted employee performance and engagement data, the attrition risk assessment is reported as:</p>
            <div class="result">{risk_level}</div>
            <p><b>Prediction Status:</b> {"Likely to Leave" if prediction == 1 else "Likely to Stay"}</p>
            <p><b>Confidence Level:</b> {percent:.2f}%</p>
        </div>

        <div class="section-title">Employee Analytics Summary</div>

        <table>
            <tr>
                <th>Feature</th>
                <th>Submitted Value</th>
            </tr>
            <tr><td>Satisfaction Level</td><td>{satisfaction_level}</td></tr>
            <tr><td>Last Evaluation Score</td><td>{last_evaluation}</td></tr>
            <tr><td>Number of Projects</td><td>{number_project}</td></tr>
            <tr><td>Average Monthly Hours</td><td>{average_montly_hours}</td></tr>
            <tr><td>Time Spent in Company</td><td>{time_spend_company} Years</td></tr>
            <tr><td>Work Accident Record</td><td>{"Yes" if Work_accident == 1 else "No"}</td></tr>
            <tr><td>Promotion in Last 5 Years</td><td>{"Yes" if promotion_last_5years == 1 else "No"}</td></tr>
            <tr><td>Salary Level</td><td>{salary}</td></tr>
            <tr><td>Overworked</td><td>{overworked}</td></tr>
            <tr><td>Satisfaction Category</td><td>{satisfaction}</td></tr>
        </table>

        <div class="section-title">Professional Recommendation</div>

        <p>
            {recommendation}
        </p>

        <div class="signature">
            Yours sincerely,<br><br>
            <b>HR Analytics Unit</b><br>
            Senior HR Consultant<br>
            ABC Corporate Health & HR Analytics Centre
        </div>

        <div class="disclaimer">
            <b>Disclaimer:</b><br>
            Please note that this prediction is generated by a machine learning model and should be interpreted
            alongside managerial assessment, employee feedback, performance review, and organizational policies.
            It should not be used as the sole basis for employment decisions.
        </div>

        <div class="footer">
            This HR attrition prediction is intended for research, educational, and workforce planning purposes only.
        </div>

    </body>
    </html>
    """

    pdf_file = generate_pdf_from_html(html_report)

    st.download_button(
        label="Download Professional PDF Report",
        data=pdf_file,
        file_name="HR_Predictive_Analytics_Report.pdf",
        mime="application/pdf"
    )
