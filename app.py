from flask import Flask, render_template, request, redirect
import quip
ACCESS_TOKEN = "U0dlQU1BYU5xblM=|1639179528|YBNnuB7ERHMNArcQl7o2Q8DfeRaOgFkHbuW8qYFcqRc="
client = quip.QuipClient(access_token=ACCESS_TOKEN)
#,"CDr.","Col.","FatherGen.","Gov.","Hon.","JudgeJusticeMaj.","MissRabbiRep.","Rev.","Sen.","PastorSr."
salutationPicklist = ["Mr.","Ms.","Mrs.","Mx.","Dr.","Prof.","Capt."]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', array = salutationPicklist)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/contactPost', methods=['POST'])
def contactPost():
    title = "SCRM-Migration Contact Demo"
    jso = client.get_matching_threads(query=title, only_match_titles=True)
    #print(jso)
    thread_id = jso[0]["thread"]["id"]
    #contactSheet = client.get_named_spreadsheet(name="Picklist_Mapping",thread_id=thread_id)
    #print(contactSheet)
    #print(request.form)
    #print(thread_id)
    
    client.add_to_spreadsheet(thread_id, [request.form["salutation-scrm-api"], request.form["salutation-scrm-field"], request.form["salutation-scrm-desc"], request.form["salutation-scrm-datatype"], ", ".join(salutationPicklist), request.form["salutation-entity"], request.form["salutation-displayName"], request.form["salutation-FieldName"], request.form["salutation-dataType"]], args = {"name": "Contact"})
    client.add_to_spreadsheet(thread_id, [request.form["firstname-scrm-api"], request.form["firstname-scrm-field"], request.form["firstname-scrm-desc"], request.form["firstname-scrm-datatype"], "", request.form["firstname-entity"], request.form["firstname-displayName"], request.form["firstname-FieldName"], request.form["firstname-dataType"]], args = {"name": "Contact"})
    #client.add_to_spreadsheet(thread_id, [request.form["middlename-scrm-api"], request.form["middlename-scrm-field"], request.form["middlename-scrm-desc"], request.form["middlename-scrm-datatype"], "", request.form["middlename-entity"], request.form["middlename-displayName"], request.form["middlename-FieldName"], request.form["middlename-dataType"]], args = {"name": "Contact"})
    #client.add_to_spreadsheet(thread_id, [request.form["lastname-scrm-api"], request.form["lastname-scrm-field"], request.form["lastname-scrm-desc"], request.form["lastname-scrm-datatype"], "", request.form["lastname-entity"], request.form["lastname-displayName"], request.form["lastname-FieldName"], request.form["lastname-dataType"]], args = {"name": "Contact"})
    #client.add_to_spreadsheet(thread_id, [request.form["suffix-scrm-api"], request.form["suffix-scrm-field"], request.form["suffix-scrm-desc"], request.form["suffix-scrm-datatype"], "", request.form["suffix-entity"], request.form["suffix-displayName"], request.form["suffix-FieldName"], request.form["suffix-dataType"]], args = {"name": "Contact"})
    #client.add_to_spreadsheet(thread_id, [request.form["nickname-scrm-api"], request.form["nickname-scrm-field"], request.form["nickname-scrm-desc"], request.form["nickname-scrm-datatype"], "", request.form["nickname-entity"], request.form["nickname-displayName"], request.form["nickname-FieldName"], request.form["nickname-dataType"]], args = {"name": "Contact"})
    #client.add_to_spreadsheet(thread_id, [request.form["public_recognition-scrm-api"], request.form["public_recognition-scrm-field"], request.form["public_recognition-scrm-desc"], request.form["public_recognition-scrm-datatype"], "", request.form["public_recognition-entity"], request.form["public_recognition-displayName"], request.form["public_recognition-FieldName"], request.form["public_recognition-dataType"]], args = {"name": "Contact"})
    #client.add_to_spreadsheet(thread_id, [request.form["luw_contact_mgr-scrm-api"], request.form["luw_contact_mgr-scrm-field"], request.form["luw_contact_mgr-scrm-desc"], request.form["luw_contact_mgr-scrm-datatype"], "", request.form["luw_contact_mgr-entity"], request.form["luw_contact_mgr-displayName"], request.form["luw_contact_mgr-FieldName"], request.form["luw_contact_mgr-dataType"]], args = {"name": "Contact"})
    #client.add_to_spreadsheet(thread_id, [request.form["ethnicity-scrm-api"], request.form["ethnicity-scrm-field"], request.form["ethnicity-scrm-desc"], request.form["ethnicity-scrm-datatype"], "", request.form["ethnicity-entity"], request.form["ethnicity-displayName"], request.form["ethnicity-FieldName"], request.form["ethnicity-dataType"]], args = {"name": "Contact"})
    #client.add_to_spreadsheet(thread_id, [request.form["other_race-scrm-api"], request.form["other_race-scrm-field"], request.form["other_race-scrm-desc"], request.form["other_race-scrm-datatype"], "", request.form["other_race-entity"], request.form["other_race-displayName"], request.form["other_race-FieldName"], request.form["other_race-dataType"]], args = {"name": "Contact"})
    #client.add_to_spreadsheet(thread_id, [request.form["other_gender-scrm-api"], request.form["other_gender-scrm-field"], request.form["other_gender-scrm-desc"], request.form["other_gender-scrm-datatype"], "", request.form["other_gender-entity"], request.form["other_gender-displayName"], request.form["other_gender-FieldName"], request.form["other_gender-dataType"]], args = {"name": "Contact"})
    #client.add_to_spreadsheet(thread_id, [request.form["birthdate-scrm-api"], request.form["birthdate-scrm-field"], request.form["birthdate-scrm-desc"], request.form["birthdate-scrm-datatype"], "", request.form["birthdate-entity"], request.form["birthdate-displayName"], request.form["birthdate-FieldName"], request.form["birthdate-dataType"]], args = {"name": "Contact"})
    #client.add_to_spreadsheet(thread_id, [request.form["birth_day-scrm-api"], request.form["birth_day-scrm-field"], request.form["birth_day-scrm-desc"], request.form["birth_day-scrm-datatype"], "", request.form["birth_day-entity"], request.form["birth_day-displayName"], request.form["birth_day-FieldName"], request.form["birth_day-dataType"]], args = {"name": "Contact"})
    #client.add_to_spreadsheet(thread_id, [request.form["birth_month-scrm-api"], request.form["birth_month-scrm-field"], request.form["birth_month-scrm-desc"], request.form["birth_month-scrm-datatype"], "", request.form["birth_month-entity"], request.form["birth_month-displayName"], request.form["birth_month-FieldName"], request.form["birth_month-dataType"]], args = {"name": "Contact"})
    #client.add_to_spreadsheet(thread_id, [request.form["birth_year-scrm-api"], request.form["birth_year-scrm-field"], request.form["birth_year-scrm-desc"], request.form["birth_year-scrm-datatype"], "", request.form["birth_year-entity"], request.form["birth_year-displayName"], request.form["birth_year-FieldName"], request.form["birth_year-dataType"]], args = {"name": "Contact"})
    #client.add_to_spreadsheet(thread_id, [request.form["npsp_Deceased-scrm-api"], request.form["npsp_Deceased-scrm-field"], request.form["npsp_Deceased-scrm-desc"], request.form["npsp_Deceased-scrm-datatype"], "", request.form["npsp_Deceased-entity"], request.form["npsp_Deceased-displayName"], request.form["npsp_Deceased-FieldName"], request.form["npsp_Deceased-dataType"]], args = {"name": "Contact"})
    
    title = "SCRM-Migration Picklist_Mapping Demo"
    jso = client.get_matching_threads(query=title, only_match_titles=True)
    #print(jso)
    thread_id = jso[0]["thread"]["id"]
    for idx,sal in enumerate(salutationPicklist):
        client.add_to_spreadsheet(thread_id, ["Contacts", request.form["salutation-scrm-field"], request.form["salutation-scrm-api"], request.form["salutation-entity"], request.form["salutation-FieldName"], "", request.form["salutation-entity-picklist-value_"+str(idx+1)], str(idx+1), sal],args={"name": "PicklistMapping"})
    #print(res)
    
    return redirect('/success')
if __name__ == '__main__':
    app.run(debug=True)

