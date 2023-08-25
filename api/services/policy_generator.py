from fillpdf import fillpdfs
import replicate
import os
import sys
sys.path.insert(0, 'LLM policy generator\\api\\')
from services.send_email import send_email_with_attachment
os.environ["REPLICATE_API_TOKEN"] = os.getenv('REPLICATE_API_TOKEN')


def policy_suggestion(response):
   
    # Prompts
    pre_prompt = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
    prompt_input = f"""suggest a health insurance policy from the list['HDFC ERGO Health Insurance Plan'] in india for {response['name']} whose age is {response['age']} years is a {response['gender']} {response['marital_status']} having {response['child']} children. 
    total amount they can pay is {response['sum_insured']} lakhs for a period of {response['policy_period']} years, lives in {response['city']}, {response['state']}. give me the suggested policy name, why this policy is suggested and give me the benefits of the policy all 
    in a dictionary format with proper quotes and without new line give me result in one line """ + """{'policy_name': 'give the name of the policy here', 
    'why_this_policy_guggested': 'give the result of why policy is suggestedd', 'policy_benefits': 'give the benefits of the policy here'"""

    #Generate LLM response
    output = replicate.run('replicate/llama-2-70b-chat:58d078176e02c219e11eb4da5a02a7830a283b14cf8f94537af893ccff5ee781', # LLM model
                            input={"prompt": f"{pre_prompt} {prompt_input} Assistant: ", # Prompts
                            "temperature":0.1, "top_p":0.9, "max_length":2800, "repetition_penalty":1})  # Mod

    

    full_response = ""

    for item in output:
        full_response += item


    full_response = full_response.replace("Assistant: ", "")

    policy_dict = eval(full_response)

    if policy_dict['policy_name'] == 'HDFC ERGO Health Insurance Plan':
        policy_path = "LLM policy generator/api/source/HDFC-ERGO-Proposal-Form-My-Health-Suraksha-Gold-Smart.pdf"


    fillpdfs.get_form_fields(policy_path)

    # fillpdfs.print_form_fields(policy_path)


    details_person_proposed_insured = response['details_person_proposed_insured']['1'].__dict__
    data_dict = {
    'Text1': response['name'],
    'Text2': response['address'],
    'Text4': response['landmark'],
    'Text5': response['city'],
    'Text7': response['state'],
    'Text8': response['pincode'],
    'Text9': response['nationality'],
    'Text10': response['dob'],
    'Text12': response['marital_status'],
    'Text13': response['mobile_no'],
    'Text14': response['email_id'],
    'Text15': response['profession'],
    'Text17': response['eia_no'],
    'Text18': response['policy_type'],
    'Text19': response['policy_period'],
    'Text20': response['policy_period_from'],
    'Text21': response['policy_period_to'],
    'Text22': details_person_proposed_insured['name'],
    'Text24': details_person_proposed_insured['gender'],
    'Text26': details_person_proposed_insured['dob'],
    'Text27': details_person_proposed_insured['height'],
    'Text28': details_person_proposed_insured['weight'],
    'Text29': details_person_proposed_insured['relationship_with_proposer'],
    'Text30': details_person_proposed_insured['premium_tier'],
    'Text31': details_person_proposed_insured['basic_sum_insured'],
    'Text115': response['sum_insured'],
    'Text110': response['place'],
    'Text111': response['date']

    }
    

    report_path =  policy_dict['policy_name']+'_Health_policy.pdf'
    fillpdfs.write_fillable_pdf(policy_path, report_path, data_dict)
    send_email_with_attachment(response['email_id'],report_path)
    os.remove(report_path)
    return "successfully"

