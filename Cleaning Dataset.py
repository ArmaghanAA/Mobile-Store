import numpy as np
import pandas as pd

import re

df = pd.read_csv('Step1_df.csv')
links = pd.read_csv('AllLinks.csv')

####### Display Part
def extract_display_size(input_string):
    try:
        screen_size_inch, screen_area_cm, screen_to_body_ratio = list(map(float, re.findall(r'\d+\.\d+', input_string)))
    except:
        return np.nan, np.nan, np.nan

    return screen_size_inch, screen_area_cm, screen_to_body_ratio

def extract_display_resolution(input_string):

    try:
        width, height = re.findall(r'(\d+)\s*x\s*(\d+)\s*pixels', input_string)[0]
        screen_resolution = f'{width} x {height}'
    except:
        width, height, screen_resolution = np.nan, np.nan, np.nan
    
    try:
        ratio = re.findall(r'(\d+:\d+)\s*ratio', input_string)[0]
    except:
        ratio = np.nan
    
    try:
        ppi_density = re.findall(r'(~\d+)\s*ppi density', input_string)[0][1:]
    except:
        ppi_density = np.nan

    return float(width), float(height), screen_resolution, ratio, float(ppi_density)

##### Platform
def extract_platform(input_string):

    try:
        input_string = re.sub(r'\([^)]*\)|[/-]| Professional| compatible', ',', input_string).split(',')[0].strip()
        input_string = re.sub(r' Oreo| Mango| Pie| Standard| Tango II| Harmattan| OS| Wear', '', input_string)
        input_string = re.sub(r'bada', 'Bada', input_string)
        input_string = re.sub(r'Android 12 or Android 12', 'Android 12', input_string)
        input_string = re.sub(r' or Android ', ',', input_string)
        input_string = re.sub(r' or ', ',', input_string)
        
        input_string = re.sub(r'\^', ' ', input_string)
        split_values = input_string.split()
        
    except:
        return np.nan, np.nan
        
    try:
        check = int(split_values[-1][0])
        version = split_values[-1]
        platform = ' '.join(split_values[:-1])
    except:
        version = np.nan
        platform = input_string
    
    return platform, version

##### Memory 
def extract_memory(input_string):

    if input_string in ['No', 'Unspecified storage', 'Unspecified']:
        return np.nan, np.nan

    else:
        try:
            input_string = re.sub(r' \([^)]*\)|[,;/]| ROM| user available| internal', '', input_string)
            input_string = re.sub(r' KB', 'KB', input_string)
            input_string = re.sub(r' RAM', '-', input_string)
            input_string = re.sub(r'  ', ' ', input_string)
            split_values = list(set(input_string.split()))

            ram_values = []
            memory_values = []

            for val in split_values:
                if val[-1] == '-':
                    ram_values.append(val[:-1])
                else:
                    if val != '':
                        memory_values.append(val)

            memory_values = ','.join(sorted(memory_values))
            ram_values = ','.join(sorted(ram_values))

            if memory_values == '':
                memory_values = np.nan
            if ram_values == '':
                ram_values = np.nan

        except:
            memory_values, ram_values = np.nan, np.nan
        
    return memory_values, ram_values

############# CPU
def extract_cpu(input_string):

    try:
        input_string = re.sub(r'-', ' ', input_string)
        split_values = input_string.strip().split()
        
        if ('Dual' in split_values) or ('dual' in split_values):
            core_num = 2
        elif 'Triple' in split_values:
            core_num = 3
        elif 'Quad' in split_values:
            core_num = 4
        elif 'Hexa' in split_values:
            core_num = 6
        elif ('Octa' in split_values) or ('8' in split_values):
            core_num = 8
        elif 'Deca' in split_values:
            core_num = 10
        else:
            core_num = 1

    except:
        core_num = np.nan
        
    return core_num

################## Display Type
def extract_display_type_specific(input_string):

    input_string = re.sub(r'S-LCD|SLCD', 'Super LCD', input_string)
    input_string = re.sub(r'S-IPS|SIPS', 'Super IPS', input_string)
    input_string = re.sub(r'TFT  LCD', 'TFT LCD', input_string)
    input_string = re.sub(r' or ', ',', input_string)
    input_string = re.sub(r'Super clear |SC-', 'Super Clear ', input_string)
    input_string = re.sub(r'HD IPS\+|HD IPS \+|HD-IPS \+|HD IPS Plus', 'HD-IPS+', input_string)
    input_string = re.sub(r' \(single white color\)| resistive touchscreen|Samsung ', '', input_string)

    if input_string == 'Super IPS+':
        input_string = 'Super IPS+ LCD'
        
    type = input_string.split(',')[0].strip()


    return type

def extract_display_type(input_string):

    input_string = re.sub(r'[-\+]', ' ', input_string)
    input_string = re.sub(r'LCD[2356]|TDDI', 'LCD', input_string)
    input_string = re.sub(r'CSTN|STN', 'TN', input_string)

    split_values = input_string.strip().split()

    if 'AMOLED' in split_values:
        type = 'AMOLED'
    elif 'IPS' in split_values:
        type = 'IPS'
    elif 'TFT' in split_values:
        type = 'TFT'
    elif 'PLS' in split_values:
        type = 'PLS'
    elif 'OLED' in split_values:
        type = 'OLED'
    elif 'LCD' in split_values:
        type = 'LCD'
    else:
        type = 'Other'

    return type

#### Comms Part

def boolian_extract(input_string):
    try:
        input_string = re.sub(r'No\, included adaptor for 3.5mm', 'No', input_string)
        if input_string in ['Unspecified', 'No', 'TBC']:
            return 0
        else:
            return 1
    except:
        return 0

#### Sensor Part
def extract_sensor(input_string):

    
    try:

        input_string = re.sub(r' \([^)]*\)|[/;]|always-on |Infrared |Dual |unspecified sensors', '', input_string)
        input_string = re.sub(r' - North America| - other markets', ',', input_string)
        input_string = re.sub(r'[Cc]ompass', 'compass', input_string)
        input_string = re.sub(r' light| infrared', '', input_string)
        input_string = re.sub(r'Fingerprints', 'Fingerprint', input_string)
        input_string = re.sub(r'[Ff]ingerprint', 'fingerprint', input_string)
        input_string = re.sub(r'[Pp]roximity', 'proximity', input_string)
        input_string = re.sub(r'[Aa]ccelerometer', 'accelerometer', input_string)
        input_string = re.sub(r'gyroscope', 'gyro', input_string)
        input_string = re.sub(r'temperature', 'thermometer', input_string)
        input_string = re.sub(r'recognition', 'ID', input_string)
        input_string = re.sub(r' ID', '-ID', input_string)
        input_string = re.sub(r'proximity ', 'proximity,', input_string)
        
        sensors = input_string.split(',')
        sensors = [sen.strip() for sen in sensors]
        sensors = ','.join(sensors)

        if input_string in ['Unspecified', 'No']:
            sensors = np.nan

    except:
        sensors = np.nan

    return sensors

# Year
def extract_year(launch_announced):
    year_match = re.findall(r'^(\d+)', launch_announced)
    return int(year_match[0]) if year_match else np.nan

# network_technology
def extract_network_technology(Net_tech):
    is_2g = 0
    is_3g = 0
    is_4g = 0
    is_5g = 0
    Network = np.nan
    if Net_tech:

        if 'GSM' or 'CDMA' or 'TDMA' in Net_tech:
            is_2g = 1
            Network = '2G'
        if 'HSPA' or 'EVDO' or 'UMTS' in Net_tech:
            is_3g = 1
            Network = '3G'
        if 'LTE' or 'WiMAX' in Net_tech:
            is_4g = 1
            Network = '4G'
        if '5G' in Net_tech:
            is_5g = 1
            Network = '5G'
        if 'No cellular connectivity' in Net_tech:
            Network = 'No'
    else:
        is_2g = np.nan
        is_3g = np.nan
        is_4g = np.nan
        is_5g = np.nan
        Network = np.nan
    return Network, is_2g, is_3g, is_4g, is_5g

### Body
def extract_body_dimensions(body_dimensions):
    try:
        dimensions_mm = re.findall(r'^(.+) mm', body_dimensions)
        dimensions_mm = dimensions_mm[0]
    except:
        dimensions_mm = np.nan
    try:
        dimensions_inches = re.findall(r'\((.+) in\)', body_dimensions)
        dimensions_inches = dimensions_inches[0]
    except:
        dimensions_inches = np.nan
    return dimensions_mm, dimensions_inches

def extract_body_weight(body_weight):
    try:
        body_weight_g = re.sub(r' \([^)]*\)[^)]*|[/or][^)]*', '', body_weight)
        weight_g = re.findall(r'^(.+) g', body_weight_g)
        weight_g = float(weight_g[0])
    except:
        weight_g = np.nan
    try:
        weight_oz = re.findall(r'\((.+) oz\)', body_weight)
        try:
            weight_oz = float(weight_oz[0])
        except:
            weight_oz = float(weight_oz.split('(')[-1])
    except:
        weight_oz = np.nan
    return weight_g, weight_oz

def extract_sim(input_string):
    try:
        Nano_SIM = 1 if 'Nano' in input_string else 0
        Micro_SIM = 1 if 'Micro' in input_string else 0
        Mini_SIM = 1 if 'Mini' in input_string else 0
        eSIM = 1 if 'eSIM' in input_string else 0

        Single_SIM = 1 if 'Single' in input_string else 0
        Dual_SIM = 1 if 'Dual' in input_string else 0
    except:
        return np.nan, np.nan, np.nan, np.nan, np.nan, np.nan
    
    return Nano_SIM, Micro_SIM, Mini_SIM, eSIM, Single_SIM, Dual_SIM

### Batery

def price_detect(item):
    if item == np.nan:
        return np.nan
    eur1 = re.findall('About (\d+) EUR', str(item))
    if len(eur1) > 0:
        return float(eur1[0])
    eur2 = re.findall('€ (\d+)\.\d\d', str(item))
    if len(eur2) > 0:
        return float(eur2[0])
    else:
        return np.nan

def battery_capacity_detect(item):
    mAh = re.findall('(\d\d\d\d?) mAh', str(item))
    if len(mAh) > 0:
        return int(mAh[0])
    else:
        return np.nan
    
def bat_kind_detect(item):

    item = re.sub(r',', ' ', str(item))
    parts = str(item).split()
    
    if ('Li-ion' in parts) or ('Li-Ion' in parts):
        return 'Li-ion'
    elif 'Li-Po' in parts:
        return 'Li-Po'
    elif 'Silicon-carbon' in parts:
        return 'Silicon-Carbon'
    else:
        return np.nan

goal_columns=['Body_Dimensions', 'Body_SIM','Body_Weight','Display_Resolution', 'Display_Size', 'Display_Type',
       'Launch_Announced','Memory_Card slot', 'Memory_Internal', 'Name','Network_Technology', 'Platform_CPU', 'Platform_OS',
       'Battery_Type','Comms_Bluetooth','Comms_Infrared port', 'Comms_NFC', 'Comms_Positioning', 'Comms_Radio',
       'Comms_USB', 'Comms_WLAN', 'Features_Sensors', 'Main Camera_Dual', 'Main Camera_Features',
       'Main Camera_Single', 'Main Camera_Triple', 'Main Camera_Video', 'Misc_Price', 'Selfie camera_Features',
       'Selfie camera_Single', 'Selfie camera_Video', 'Sound_3.5mm jack','Sound_Loudspeaker',
       'Selfie camera_Dual', 'Selfie camera_Triple', 'Main Camera_Quad', 'Main Camera_Dual or Triple',
       'Main Camera_Penta', 'Main Camera_Five', 'Device_label', 'Brand']

df = df.loc[:, goal_columns]

### Display Part
df['Display_Size_inches'], df['Display_Size_cm2'], df['screen_to_body_ratio'] = zip(*df['Display_Size'].apply(extract_display_size))

(df['Display_Resolution_width'], df['Display_Resolution_hight'], 
 df['Display_Resolution_pixels'], df['Display_Resolution_ratio'], 
 df['Display_Resolution_ppi']) = zip(*df['Display_Resolution'].apply(extract_display_resolution))

df['Display_Type_Specific'] = df['Display_Type'].apply(extract_display_type_specific)
df['Display_Type'] = df['Display_Type_Specific'].apply(extract_display_type)

### Platform Part
df['Platform_OS'], df['Platform_OS_version'] = zip(*df['Platform_OS'].apply(extract_platform))
df['Platform_CPU'] = df['Platform_CPU'].apply(extract_cpu)

### Memory Part
df.loc[df['Memory_Card slot'] != 'No', 'Memory_Card slot'] = 1
df.loc[df['Memory_Card slot'] == 'No', 'Memory_Card slot'] = 0
df['external memroy'] = df['Memory_Card slot']

df['Memory_Internal'], df['RAM'] = zip(*df['Memory_Internal'].apply(extract_memory))

### Comms Part
df['Comms_Bluetooth'] = df['Comms_Bluetooth'].apply(boolian_extract)
df['Comms_NFC'] = df['Comms_NFC'].apply(boolian_extract)
df['Comms_Positioning'] = df['Comms_Positioning'].apply(boolian_extract)
df['Comms_Radio'] = df['Comms_Radio'].apply(boolian_extract)
df['Comms_USB'] = df['Comms_USB'].apply(boolian_extract)
df['Comms_WLAN'] = df['Comms_WLAN'].apply(boolian_extract)
df['Comms_Infrared port'] = df['Comms_Infrared port'].apply(boolian_extract)

### Sound Part
df['jack_port'] = df['Sound_3.5mm jack'].apply(boolian_extract)
df['LoudSpeaker'] = df['Sound_Loudspeaker'].apply(boolian_extract)

### Sensor
df['Features_Sensors'] = df['Features_Sensors'].apply(extract_sensor)

### Year
df['Year'] = df['Launch_Announced'].apply(extract_year)

### Network
df['Network'], df['is_2g'], df['is_3g'], df['is_4g'], df['is_5g'] = zip(*df['Network_Technology'].apply(extract_network_technology))

### Body
df['Body_Dimensions_mm'], df['Body_Dimensions_inches'] = zip(*df['Body_Dimensions'].apply(extract_body_dimensions))
df['Body_Weight_g'], df['Body_Weight_oz'] = zip(*df['Body_Weight'].apply(extract_body_weight))

(df['Nano_SIM'], df['Micro_SIM'], 
 df['Mini_SIM'], df['eSIM'], 
 df['Single_SIM'], df['Dual_SIM']) = zip(*df['Body_SIM'].apply(extract_sim))

### Battery
df['Battery_Capacity_mAh'] = df['Battery_Type'].apply(battery_capacity_detect)
df['Battery_Type'] = df['Battery_Type'].apply(bat_kind_detect)

### Price
df['Price'] = df['Misc_Price'].apply(price_detect)


### Camera_Num
df['Main_Camera_Num'] = np.nan
df['Selfie_Camera_Num'] = np.nan

df.loc[~df['Main Camera_Single'].isna(),'Main_Camera_Num'] = 1
df.loc[~df['Main Camera_Dual'].isna(),'Main_Camera_Num'] = 2
df.loc[~df['Main Camera_Triple'].isna(),'Main_Camera_Num'] = 3
df.loc[~df['Main Camera_Quad'].isna(),'Main_Camera_Num'] = 4
df.loc[~df['Main Camera_Five'].isna(),'Main_Camera_Num'] = 5
df.loc[~df['Main Camera_Penta'].isna(),'Main_Camera_Num'] = 5
df.loc[~df['Main Camera_Dual or Triple'].isna(),'Main_Camera_Num'] = 3

df.loc[~df['Selfie camera_Single'].isna(),'Selfie_Camera_Num'] = 1
df.loc[~df['Selfie camera_Dual'].isna(),'Selfie_Camera_Num'] = 2
df.loc[~df['Selfie camera_Triple'].isna(),'Selfie_Camera_Num'] = 3

df.drop(columns=['Display_Size', 'Display_Resolution', 'Memory_Card slot', 'Sound_3.5mm jack', 'Sound_Loudspeaker',
                 'Launch_Announced', 'Network_Technology', 'Body_Dimensions', 'Body_Weight', 'Body_SIM',
                 'Main Camera_Dual', 'Main Camera_Features',
       'Main Camera_Single', 'Main Camera_Triple', 'Main Camera_Video', 'Selfie camera_Features',
       'Selfie camera_Single', 'Selfie camera_Video',
       'Selfie camera_Dual', 'Selfie camera_Triple', 'Main Camera_Quad', 'Main Camera_Dual or Triple',
       'Main Camera_Penta', 'Main Camera_Five', 'Misc_Price'], inplace=True)


df['Name'], df['Device_id'] = zip(*links['Link'].apply(lambda col: col.split('/')[-1].split('.')[0].split('-')))

df.to_csv('Cleaned_df.csv', index=False)