import dh
import flexis
from ask_sdk_model.response import Response
from ask_sdk_core.handler_input import HandlerInput


def lambda_handler(event, context):
    print("It's in lamda_handler at least", event['request']['type'])
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event, context)
    if event['request']['type'] == "IntentRequest":
        return intent_router(event, context)
    


def on_launch(event, context):
    session_attributes = {}
    card_title = ""
    speech_output = "What menu are you looking for?"
    reprompt_text = ""
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def intent_router(event, context):
    print("INSIDE intent_router")
    intent = event['request']['intent']['name']
    print(intent)
    if intent == "DiningHallMenuIntent":
        return Dining_Hall_Menu_Intent(event, context)
    if intent == "FlexiCheckIntent":
        return Flexi_Check_Intent(event, context)
    if intent == "GuestSwipeCheckIntent":
        return Guest_Swipe_Check_Intent(event, context)

def Flexi_Check_Intent(event, context):
    slots = event['request']['intent']['slots']
    print(slots)
    result = flexis.scrape_flexis()
    card_title=""
    session_attributes ={}
    speech_output = ""
    reprompt_text = ""
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(card_title, result, reprompt_text, should_end_session))
    
def Guest_Swipe_Check_Intent(event, context):
    slots = event['request']['intent']['slots']
    print(slots)
    result = flexis.scrape_guest()
    card_title=""
    session_attributes ={}
    speech_output = ""
    reprompt_text = ""
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(card_title, result, reprompt_text, should_end_session))

def Dining_Hall_Menu_Intent(event, context):
    slots = event['request']['intent']['slots']
    college_name = slots['colleges']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
    if 'resolutions' in slots['meal']:
        meal_name = slots['meal']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
    result = ""
    if college_name == "Cowell":
        if 'resolutions' in slots['meal']:
            menu = dh.scrape_dining_hall("Cowell/Stevenson", meal_name.capitalize())
        else:
            menu = dh.scrape_dining_hall("Cowell/Stevenson")
    if college_name == "Crown":
        if 'resolutions' in slots['meal']:
            menu = dh.scrape_dining_hall("Crown/Merrill", meal_name.capitalize())
        else:
            menu = dh.scrape_dining_hall("Crown/Merrill")
    if college_name == "9":
        if 'resolutions' in slots['meal']:
            menu = dh.scrape_dining_hall("9/10", meal_name.capitalize())
        else:
            menu = dh.scrape_dining_hall("9/10")
    if college_name == "Porter":
        if 'resolutions' in slots['meal']:
            menu = dh.scrape_dining_hall("Porter/Kresge", meal_name.capitalize())
        else:
            menu = dh.scrape_dining_hall("Porter/Kresge")
    if college_name == "Oakes":
        if 'resolutions' in slots['meal']:
            menu = dh.scrape_dining_hall("Rachel Carson/Oakes", meal_name.capitalize())
        else:
            menu = dh.scrape_dining_hall("Rachel Carson/Oakes")
    if len(menu) == 0:
        result = "Sorry, " + slots['colleges']['value'] + " is closed"
    else:  
        for item in menu:
            result += (str(item) + ", ") 
        result = result[:len(result)-2]
    
    card_title=""
    session_attributes ={}
    speech_output = ""
    reprompt_text = ""
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(card_title, result, reprompt_text, should_end_session))
  

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        "outputSpeech": {
            "type": "PlainText",
            "text": output
        },
        "card": {
            "type": "Simple",
            "title": title,
            "content": output
        },
        "reprompt": {
            "outputSpeech": {
                "type": "PlainText",
                "text": reprompt_text
            }
        },
        "shouldEndSession": should_end_session
    }
    

def build_response(session_attributes, speechlet_response):
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response
    }
