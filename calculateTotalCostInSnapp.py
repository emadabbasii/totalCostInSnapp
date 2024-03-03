import requests

# Initialize total price
total_price = 0
your_token = ''

# Loop through each page from 1 to 50
for page in range(1, 50):
    url = f'https://app.snapp.taxi/api/api-base/v2/passenger/ride/history?page={page}'
    headers = {
        'authority': 'app.snapp.taxi',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'app-version': 'pwa',
        'authorization': f'Bearer {your_token}',
        'content-type': 'application/json',
        'locale': 'fa-IR',
        'referer': 'https://app.snapp.taxi/ride-history',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        'x-app-name': 'passenger-pwa',
        'x-app-version': '17.12.1'
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    # Check if 'data' key exists in the response
    if 'data' in data:
        rides = data['data']['rides']
        for ride in rides:
            title = ride['title']
            if 'لغو' in title:
                continue
            final_price = ride['final_price']
            total_price += final_price

# Print the total price
print("Total final price (excluding canceled rides):", total_price)

