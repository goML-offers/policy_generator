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
    prompt_input = f"""suggest a {response['insurance_type']} from the list['HDFC ERGO Health'] in india for {response['name']} whose age is {response['age']} years is a {response['gender']} {response['marital_status']} having {response['child']} children. 
    total amount they can pay is {response['sum_insured']} lakhs for a period of {response['policy_period']} years, lives in {response['city']}, {response['state']}. give me the suggested policy name, why this policy is suggested and give me the benefits of the policy all 
    in a dictionary format with proper quotes and without new line give me result in one line """ + """{'policy_name': 'give the name of the policy here', 
    'why_this_policy_suggested': 'give the result of why policy is suggested', 'policy_benefits': 'give the benefits of the policy here'"""
    #Generate LLM response
    output = replicate.run('replicate/llama-2-70b-chat:58d078176e02c219e11eb4da5a02a7830a283b14cf8f94537af893ccff5ee781', # LLM model
                            input={"prompt": f"{pre_prompt} {prompt_input} Assistant: ", # Prompts
                            "temperature":0.1, "top_p":0.9, "max_length":2800, "repetition_penalty":1})  # Mod

    
#     output = """suggest a Health insurance from the list['HDFC ERGO Health'] in india for John Doe whose age is 35 years is a Male Married having 2 children.        
#     total amount they can pay is 500000 lakhs for a period of 1 Year years, lives in Cityville, Stateland. give me the suggested policy name, why this policy is suggested and give me the benefits of the policy all
#     in a dictionary format with proper quotes and without new line give me result in one line {'policy_name': 'give the name of the policy here',    
#     'why_this_policy_suggested': 'give the result of why policy is suggested', 'policy_benefits': 'give the benefits of the policy here'
#  Assistant: {
#    'policy_name': 'HDFC ERGO Health Insurance Plan',
#    'why_this_policy_suggested': 'HDFC ERGO Health Insurance Plan is suggested for John Doe because it offers comprehensive coverage for medical expenses, including hospitalization, surgical procedures, and critical illnesses. The plan also provides additional benefits such as maternity coverage and newborn baby coverage.',
#    'policy_benefits': 'The policy benefits include coverage for medical expenses up to 500000 lakhs for a period of 1 year, coverage for pre-existing diseases after a 3-year waiting period, and a 10% discount on premiums for online purchases. Additionally, the policy offers a free health check-up facility every 3 years and a cumulative bonus of 5% for every claim-free year.'
# }"""
    full_response = ""

    for item in output:
        full_response += item
    full_response
    
    # # policy_dict = eval(full_response)
    policy_dict = {}
    lines = full_response.split('\n')
    
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip().strip("'").strip(',').strip()
            value = value.strip().strip("'").strip(',').strip()
            value = value.replace("'", "").replace(",", "").replace("{", "").strip()
            policy_dict[key] = value
    # policy_dict = policy_dict["Assistant"]

    if policy_dict['policy_name'] == 'HDFC ERGO Health Insurance Plan':
        policy_path = "api/source/HDFC-ERGO-Proposal-Form-My-Health-Suraksha-Gold-Smart (1).pdf"

    fillpdfs.get_form_fields(policy_path)

    # # fillpdfs.print_form_fields(policy_path)


    details_person_proposed_insured = response['details_person_proposed_insured']['1'].__dict__
    nominee = response['nominee']['1'].__dict__
    health_conditions = response["health_conditions"].__dict__
    data_dict = {

    'Text1': response['name'],

    'Text2': response['address'],

    'Text4': response['landmark'],

    'Text5': response['city'],

    'Text7': response['pincode'],

    'Text8': response['state'],

    'Text10': response['nationality'],

    'Text12': response['dob'],

    'Text13': response['marital_status'],

    'Text14': response['mobile_no'],

    'Text18': response['email_id'],

    'Text16': response['profession'],

    'Text17': response['eia_no'],

    'Text19': response['policy_type'],

    'Text22': response['policy_period'],

    'Text20': response['policy_period_from'],

    'Text21': response['policy_period_to'],

    'Text23': response['sum_insured'],

    'Text24': details_person_proposed_insured['name'],

    'Text25': details_person_proposed_insured['gender'],

    'Text26': details_person_proposed_insured['dob'],

    'Text27': details_person_proposed_insured['height'],

    'Text28': details_person_proposed_insured['weight'],

    'Text29': details_person_proposed_insured['relationship_with_proposer'],

    'Text30': details_person_proposed_insured['premium_tier'],

    'Text31': details_person_proposed_insured['basic_sum_insured'],

    'Text41': nominee['name'],

    'Text43': nominee['nominee_name'],

    'Text44': nominee['relationship'],

    'Text45': nominee['nominee_address'],

    'Text46': '',

    'Text47': '',

    'Text48': '',

    'Text49': '',

    'Text50': health_conditions['high_blood_pressure'],

    'Text51': health_conditions['tuberculosis'],

    'Text52': health_conditions['ulcer'],

    'Text53': health_conditions['kidney_failure'],

    'Text54': response['place'],

    'Text56': response['date']

    }
    

    report_path =  policy_dict['policy_name']+'_Health_policy.pdf'
    fillpdfs.write_fillable_pdf(policy_path, report_path, data_dict)

    send_email_with_attachment(response['email_id'],report_path)
    os.remove(report_path)
    return "successfully"

