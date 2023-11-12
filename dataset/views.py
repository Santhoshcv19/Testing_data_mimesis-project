from django.shortcuts import render
from mimesis import Generic
from mimesis.locales import Locale
from django.http import HttpResponse
import pandas as pd
import warnings

def home(request):

   
    return render(request, 'dataset/home.html')

def generate_csv(request):
    x = request.GET.get('Country')


    if(x=="Czech"):
        generic=Generic(locale=Locale.CS)
    elif(x=="Danish"):
        generic=Generic(locale=Locale.DA)
    elif(x=="German"):
        generic=Generic(locale=Locale.DE)
    elif(x=="Austrian German"):
        generic=Generic(locale=Locale.DE_AT)
    elif(x=="Swiss German"):
        generic=Generic(locale=Locale.DE_CH)
    elif(x=="Greek"):
        generic=Generic(locale=Locale.EL)
    elif(x=="English"):
        generic=Generic(locale=Locale.EN)
    elif(x=="Australian English"):
        generic=Generic(locale=Locale.EN_AU)
    elif(x=="Canadian English"):
        generic=Generic(locale=Locale.EN_CA)
    elif(x=="British English"):
        generic=Generic(locale=Locale.EN_GB)
    elif(x=="Spanish"):
        generic=Generic(locale=Locale.ES)
    elif(x=="Mexican Spanish"):
        generic=Generic(locale=Locale.ES_MX)
    elif(x=="Estonian"):
        generic=Generic(locale=Locale.ET)
    elif(x=="Farsi"):
        generic=Generic(locale=Locale.FA)
    elif(x=="Finnish"):
        generic=Generic(locale=Locale.FI)
    elif(x=="French"):
        generic=Generic(locale=Locale.FR)
    elif(x=="Hungarian"):
        generic=Generic(locale=Locale.HU)
    elif(x=="Icelandic"):
        generic=Generic(locale=Locale.IS)
    elif(x=="Italian"):
        generic=Generic(locale=Locale.IT)
    elif(x=="Japanese"):
        generic=Generic(locale=Locale.JA)
    elif(x=="Kazakh"):
        generic=Generic(locale=Locale.KK)
    elif(x=="Korean"):
        generic=Generic(locale=Locale.KO)
    elif(x=="Dutch"):
        generic=Generic(locale=Locale.NL)
    elif(x=="Belgium Dutch"):
        generic=Generic(locale=Locale.NL_BE)
    elif(x=="Norwegian"):
        generic=Generic(locale=Locale.NO)
    elif(x=="Polish"):
        generic=Generic(locale=Locale.PL)
    elif(x=="Portugese"):
        generic=Generic(locale=Locale.PT)
    elif(x=="Brazilian Portugese"):
        generic=Generic(locale=Locale.PT_BR)
    elif(x=="Russian"):
        generic=Generic(locale=Locale.RU)
    elif(x=="Slovak"):
        generic=Generic(locale=Locale.SK)
    elif(x=="Swedish"):
        generic=Generic(locale=Locale.SV)
    elif(x=="Turkish"):
        generic=Generic(locale=Locale.TR)
    elif(x=="Ukrainian"):
        generic=Generic(locale=Locale.UK)
    elif(x=="Chinese"):
        generic=Generic(locale=Locale.ZH)

    address={1: 'address', 2: 'calling_code', 3: 'city', 4: 'continent', 5: 'coordinates', 6: 'country', 7: 'country_code', 8: 'federal_subject', 9: 'get_current_locale', 10: 'latitude', 11: 'locale', 12: 'longitude', 13: 'postal_code', 14: 'prefecture', 15: 'province', 16: 'region', 17: 'state', 18: 'street_name', 19: 'street_number', 20: 'street_suffix', 21: 'zip_code'}
    code={1: 'ean', 2: 'imei', 3: 'isbn', 4: 'issn', 5: 'locale_code', 6: 'pin'}
    cryptographic={1: 'hash', 2: 'mnemonic_phrase', 3: 'token_bytes', 4: 'token_hex', 5: 'token_urlsafe', 6: 'uuid'}
    datetime={1: 'bulk_create_datetimes', 2: 'century', 3: 'date', 4: 'datetime', 5: 'day_of_month', 6: 'day_of_week', 7: 'formatted_date', 8: 'formatted_datetime', 9: 'formatted_time', 10: 'get_current_locale', 11: 'gmt_offset', 12: 'locale', 13: 'month', 14: 'periodicity', 15: 'time', 16: 'timestamp', 17: 'timezone', 18: 'validate_enum', 19: 'week_date', 20: 'year'}
    development={1: 'boolean', 2: 'os', 3: 'programming_language', 4: 'software_license', 5: 'version'}
    file={1: 'extension', 2: 'file_name', 3: 'mime_type', 4: 'size'}
    finance={1: 'bank', 2: 'company', 3: 'company_type', 4: 'cryptocurrency_iso_code', 5: 'cryptocurrency_symbol', 6: 'currency_iso_code', 7: 'currency_symbol', 8: 'extract', 9: 'get_current_locale', 10: 'locale', 11: 'price', 12: 'price_in_btc', 13: 'stock_exchange', 14: 'stock_name', 15: 'stock_ticker'}
    food={1: 'dish', 2: 'drink', 3: 'fruit', 4: 'get_current_locale', 5: 'spices', 6: 'vegetable'}
    hardware={1: 'cpu', 2: 'cpu_codename', 3: 'cpu_frequency', 4: 'generation', 5: 'graphics', 6: 'manufacturer', 7: 'phone_model', 8: 'ram_size', 9: 'ram_type', 10: 'resolution', 11: 'screen_size', 12: 'ssd_or_hdd'}
    internet={1: 'content_type', 2: 'emoji', 3: 'hashtags', 4: 'hostname', 5: 'http_method', 6: 'http_request_headers', 7: 'http_response_headers', 8: 'http_status_code', 9: 'http_status_message', 10: 'ip_v4', 11: 'ip_v4_object', 12: 'ip_v4_with_port', 13: 'ip_v6', 14: 'ip_v6_object', 15: 'mac_address', 16: 'path', 17: 'port', 18: 'public_dns', 19: 'query_parameters', 20: 'query_string', 21: 'slug', 22: 'stock_image_url', 23: 'tld', 24: 'top_level_domain', 25: 'uri', 26: 'url', 27: 'user_agent'}
    numeric={1: 'complex_number', 2: 'complexes', 3: 'decimal_number', 4: 'decimals', 5: 'float_number', 6: 'floats', 7: 'increment', 8: 'integer_number', 9: 'integers', 10: 'matrix'}
    path={1: 'dev_dir', 2: 'home', 3: 'platform', 4: 'project_dir', 5: 'root', 6: 'user', 7: 'users_folder'}
    payment={1: 'bitcoin_address', 2: 'cid', 3: 'credit_card_expiration_date', 4: 'credit_card_network', 5: 'credit_card_number', 6: 'credit_card_owner', 7: 'cvv', 8: 'ethereum_address', 9: 'paypal'}
    person={1: 'academic_degree', 2: 'age', 3: 'blood_type', 4: 'email', 5: 'first_name', 6: 'full_name', 7: 'gender', 8: 'get_current_locale', 9: 'height', 10: 'identifier', 11: 'language', 12: 'last_name', 13: 'locale', 14: 'name', 15: 'nationality', 16: 'occupation', 17: 'override_locale', 18: 'password', 19: 'phone_number', 20: 'political_views', 21: 'sex', 22: 'surname', 23: 'telephone', 24: 'title', 25: 'university', 26: 'username', 27: 'views_on', 28: 'weight', 29: 'work_experience', 30: 'worldview'}
    science={1: 'dna_sequence', 2: 'measure_unit', 3: 'metric_prefix', 4: 'rna_sequence'}
    text={1: 'alphabet', 2: 'answer', 3: 'color', 4: 'get_current_locale', 5: 'hex_color', 6: 'level', 7: 'quote', 8: 'rgb_color', 9: 'sentence', 10: 'text', 11: 'title', 12: 'word', 13: 'words'}
    transport={1: 'airplane', 2: 'car', 3: 'manufacturer', 4: 'validate_enum'}
    final={"Address":address,"Code":code,"Cryptographic":cryptographic,"DateTime":datetime,"Development":development,"File":file,"Finance":finance,"Food":food,"Hardware":hardware,"Internet":internet,"Numeric":numeric,"Path":path,"Payment":payment,"Person":person,"Science":science,"Text":text,"Transport":transport}
    df = pd.DataFrame()
    num_columns = int(request.GET.get('num_columns'))
    rows = int(request.GET.get('rows'))
    for i in range(num_columns):
        a = request.GET.get(f'Domain_{i}')
        b = int(request.GET.get(f'Subcategory_{i}'))
        
        c = final[a][b]
        row_index=0
        for n in range(rows):
            if a == "Finance":
                if hasattr(generic.finance, c) and callable(getattr(generic.finance, c)):
                    method_to_call = getattr(generic.finance, c)
                    df.loc[row_index, f'{a}_{c}'] = method_to_call()
                    row_index+=1
            elif a == "Address":
                if hasattr(generic.address, c) and callable(getattr(generic.address, c)):
                    method2_to_call = getattr(generic.address, c)
                    df.loc[row_index, f'{a}_{c}'] = method2_to_call()
                    row_index+=1
            elif a == "Code":
                if hasattr(generic.code, c) and callable(getattr(generic.code, c)):
                    method2_to_call = getattr(generic.code, c)
                    df.loc[row_index, f'{a}_{c}'] = method2_to_call()
                    row_index+=1
            elif a == "Cryptographic":
                if hasattr(generic.cryptographic, c) and callable(getattr(generic.cryptographic, c)):
                    method2_to_call = getattr(generic.cryptographic, c)
                    df.loc[row_index, f'{a}_{c}'] = method2_to_call()
                    row_index+=1
            elif a == "DateTime":
                if hasattr(generic.datetime, c) and callable(getattr(generic.datetime, c)):
                    method2_to_call = getattr(generic.datetime, c)
                    df.loc[row_index, f'{a}_{c}'] = method2_to_call()
                    row_index+=1
            elif a == "Development":
                if hasattr(generic.development, c) and callable(getattr(generic.development, c)):
                    method2_to_call = getattr(generic.development, c)
                    df.loc[row_index, f'{a}_{c}'] = method2_to_call()
                    row_index+=1
            elif a == "File":
                if hasattr(generic.file, c) and callable(getattr(generic.file, c)):
                    method2_to_call = getattr(generic.file, c)
                    df.loc[row_index, f'{a}_{c}'] = method2_to_call()
                    row_index+=1
            elif a == "Food":
                if hasattr(generic.food, c) and callable(getattr(generic.food, c)):
                    method2_to_call = getattr(generic.food, c)
                    df.loc[row_index, f'{a}_{c}'] = method2_to_call()
                    row_index+=1
            elif a == "Hardware":
                if hasattr(generic.hardware, c) and callable(getattr(generic.hardware, c)):
                    method2_to_call = getattr(generic.hardware, c)
                    df.loc[row_index, f'{a}_{c}'] = method2_to_call()
                    row_index+=1
            elif a == "Internet":
                if hasattr(generic.internet, c) and callable(getattr(generic.internet, c)):
                    method2_to_call = getattr(generic.internet, c)
                    df.loc[row_index, f'{a}_{c}'] = method2_to_call()
                    row_index+=1
            elif a == "Science":
                if hasattr(generic.science, c) and callable(getattr(generic.science, c)):
                    method2_to_call = getattr(generic.science, c)
                    df.loc[row_index, f'{a}_{c}'] = method2_to_call()
                    row_index+=1
            elif a == "Numeric":
                if hasattr(generic.numeric, c) and callable(getattr(generic.numeric, c)):
                    method2_to_call = getattr(generic.numeric, c)
                    df.loc[row_index, f'{a}_{c}'] = method2_to_call()
                    row_index+=1
            elif a == "Path":
                if hasattr(generic.path, c) and callable(getattr(generic.path, c)):
                    method2_to_call = getattr(generic.path, c)
                    df.loc[row_index, f'{a}_{c}'] = method2_to_call()
                    row_index+=1
            elif a == "Payment":
                if hasattr(generic.payment, c) and callable(getattr(generic.payment, c)):
                    method2_to_call = getattr(generic.payment, c)
                    df.loc[row_index, f'{a}_{c}'] = method2_to_call()
                    row_index+=1
            elif a == "Text":
                if hasattr(generic.text, c) and callable(getattr(generic.text, c)):
                    method2_to_call = getattr(generic.text, c)
                    df.loc[row_index, f'{a}_{c}'] = method2_to_call()
                    row_index+=1
            elif a == "Person":
                if hasattr(generic.person, c) and callable(getattr(generic.person, c)):
                    method2_to_call = getattr(generic.person, c)
                    df.loc[row_index, f'{a}_{c}'] = method2_to_call()
                    row_index+=1
            elif a == "Transport":
                if hasattr(generic.transport, c) and callable(getattr(generic.transport, c)):
                    method2_to_call = getattr(generic.transport, c)
                    df.loc[row_index, f'{a}_{c}'] = method2_to_call()
                    row_index+=1
    print(df)
    df.to_csv("Dataset2.csv")

    filename = "Dataset2.csv"
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Dataset2.csv"'
    with open(filename, 'r') as csv_file:
        response.write(csv_file.read())
    
    return response