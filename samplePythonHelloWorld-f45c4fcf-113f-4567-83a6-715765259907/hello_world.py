import dh
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


def Dining_Hall_Menu_Intent(event, context):
    print("Dining_Hall intent method")
    slots = event['request']['intent']['slots']
    print(slots)
    # if slots[0].name == "Cowell":
    #     if slots[1]['name'] is "Dinner":
    menu = dh.scrape_dining_hall("Cowell/Stevenson", "Dinner")
    print(str(menu[0]))
        # menu = dh.scrape_dining_hall("Cowell/Stevenson")
    card_title="bitch we dont even have a gui"
    session_attributes ={}
    speech_output = ""
    reprompt_text = ""
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(card_title, str(menu[0]), reprompt_text, should_end_session))
    
    # response_builder = handler_input.response_builder
    # return response_builder.speak(menu).response
    
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
