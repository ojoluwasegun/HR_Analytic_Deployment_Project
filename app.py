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
