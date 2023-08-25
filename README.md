# goML - LLM marketplace ( Policy generator)
### This policy generator's main goal is to suggest a health insurance policy and  provide a pre-filled document based on the user 

### model input:
{
  "name": "string",
  "address": "string",
  "age": "string",
  "gender": "string",
  "insurance_type": "string",
  "child": "string",
  "landmark": "string",
  "city": "string",
  "state": "string",
  "pincode": "string",
  "nationality": "string",
  "dob": "string",
  "marital_status": "string",
  "mobile_no": "string",
  "email_id": "string",
  "profession": "string",
  "eia_no": "string",
  "policy_type": "string",
  "policy_period": "string",
  "policy_period_from": "string",
  "policy_period_to": "string",
  "sum_insured": "string",
  "details_person_proposed_insured": {},
  "nominee": {},
  "health_conditions": {
    "high_blood_pressure": "string",
    "tuberculosis": "string",
    "ulcer": "string",
    "kidney_failure": "string"
  },
  "place": "string",
  "date": "string"
}

### model output:
An email sent to the user's provided email address with a pre-filled Health insurance policy document which is suggested by the LLM model

### Execution
> run requirements.txt
> run app.py (run uvicorn api.app:app --reload)
> open this url on a browser http://127.0.0.1:8000/docs
> provide the necessary inputs in the as required, don't forget to remove the sample values already provided
> check your email to get the generated policy form