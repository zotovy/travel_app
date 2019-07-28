from amadeus import Client, ResponseError
from app import city_code_database as code_db

"""
module is designed for get flights by param
"""


def get_flights(origin, destination, date):
    amadeus = Client(
        client_id='Y8cT8SjAneWZM0piL2xcLArfMxBwepTq',
        client_secret='JIrGuoHOgU5TsDNv'
    )

    try:
        response = amadeus.shopping.flight_offers.get(origin='MAD', destination='LON', departureDate='2019-08-01')

        print(response.data)
        flights = []
        for i in range(len(response.data)):
            base_dir = response.data[i]['offerItems'][0]['services'][0]['segments'][0]['flightSegment']
            class_dir = response.data[i]['offerItems'][0]['services'][0]['segments'][0]['pricingDetailPerAdult']
            price_dir = response.data[i]['offerItems'][0]['price']
            # airport = amadeus.reference_data.airlines.get(airlineCodes=base_dir['carrierCode'])
            data = {
                "departure": {'airport': base_dir['departure']['iataCode'],
                              'date': base_dir['departure']['at']},
                'arrival': {'airport': base_dir['arrival']['iataCode'],
                            'date': base_dir['arrival']['at']},
                'class': class_dir['travelClass'],
                'price': int(float(price_dir['total'])) * 60,  # TODO: парсинг курса и преобразование ПО КУРСУ
                # 'company': airport.data[0]['commonName']
            }
            flights.append(data)
        return flights

    except ResponseError as error:
        print(error)


def find_best(origin, destination, departure_date):
    origin = code_db.city[origin]
    destination = code_db.city[destination]
    # print(origin, destination)
    flights = get_flights(origin, destination, departure_date,)
    # print('flights: ', flights)
    return sorted(flights, key=lambda k: k['price'])[:15]




print(find_best('London', 'Moscow', '2019-08-01'))
