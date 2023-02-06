from django.shortcuts import render
from .forms import CSVUploadForm
from .models import CSVFile
import pandas as pd
import asyncio
import json
from django.http import FileResponse

# function to download the JSON file
def download_json(request):
    file = open("processed_data.json", "rb")
    response = FileResponse(file)
    response['Content-Disposition'] = 'attachment; filename="processed_data.json"'
    return response


# Async function to process the data and store it in a JSON file
async def data_timeframe(list_csv, timeframe):
    result = []
    for i in range(0, len(list_csv), int(timeframe)):
        row = list_csv[i:i+10]
        Nifty = row[0][0]
        date = row[1][1]
        time = row[0][2]
        openval = row[0][3]
        high = max([data[4] for data in row])
        low = min([data[5] for data in row])
        close = row[-1][6]
        volume = row[-1][7]
        # Adding the processed data to the result list
        result.append("{} {} {} {} {} {} {} {}".format(Nifty, date, time, openval, high, low, close, volume))
    with open("processed_data.json", "w") as json_file:
        # Writing the processed data to the JSON file
        json.dump(result, json_file)
    return result


# to handle the uploaded CSV file
def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        timeframe = request.POST.get('timeframe_in_minutes')
        print(timeframe)
        if form.is_valid():
            csvfile = request.FILES['file']
            df = pd.read_csv(csvfile)
            print(df.head())
            list_csv = df.values.tolist()  # Converting the pandas DataFrame to a list
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            future = loop.run_in_executor(None, asyncio.run, data_timeframe(list_csv, timeframe))
            print(future)
            loop.run_until_complete(future)
            updated_data = future.result()
            return render(request, 'mainapp/success.html', {'data':updated_data[1:11]})
    else:
        form = CSVUploadForm()
    return render(request, 'mainapp/uploadfile.html', {'form': form})

