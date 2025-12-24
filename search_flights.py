import json
import requests
from datetime import datetime, timedelta
import brotli
import time
import random
import utils

def search_round(form_data):
    simplified_itineraries = []
    error = False

    minNights = int(form_data['minNights'])
    maxNights = int(form_data['maxNights'])
    start_date = datetime.strptime(form_data['startDate'], '%Y-%m-%d')
    end_date = datetime.strptime(form_data['endDate'], '%Y-%m-%d')
    loop_end_date = end_date - timedelta(days=minNights)

    d = start_date
    while d <= loop_end_date:  # Loop through the start dates
        print(f"Scanning departure date: {utils.format_date(d)}")

        for nights in range(minNights, maxNights + 1):  # Loop through the nights
            return_date = d + timedelta(days=nights)

            if return_date > end_date:  # Ensure return date is not beyond the specified end date
                break
            request_data = {
                        "query": "query SearchReturnItinerariesQuery(\n  $search: SearchReturnInput\n  $filter: ItinerariesFilterInput\n  $options: ItinerariesOptionsInput\n) {\n  returnItineraries(search: $search, filter: $filter, options: $options) {\n    __typename\n    ... on AppError {\n      error: message\n    }\n    ... on Itineraries {\n      server {\n        requestId\n        environment\n        packageVersion\n        serverToken\n      }\n      metadata {\n        eligibilityInformation {\n          baggageEligibilityInformation {\n            topFiveResultsBaggageEligibleForPrompt\n            topFifteenResultsBaggageEligibleForPrompt\n            searchIsLongTrip\n            searchIsFamilyTrip\n            numberOfBags\n          }\n        }\n        ...AirlinesFilter_data\n        ...CountriesFilter_data\n        ...WeekDaysFilter_data\n        ...TravelTip_data\n        ...Sorting_data\n        ...MobileSorting_data\n        ...MobileSortingLink_data\n        ...PriceAlert_data\n        itinerariesCount\n        hasMorePending\n        missingProviders {\n          code\n        }\n        searchFingerprint\n        statusPerProvider {\n          provider {\n            id\n          }\n          errorHappened\n          errorMessage\n        }\n        topFiveOriginalItinerariesContainTHC\n        hasTier1MarketItineraries\n        sharedItinerary {\n          __typename\n          ... on ItineraryReturn {\n            ... on Itinerary {\n              __isItinerary: __typename\n              __typename\n              id\n              shareId\n              price {\n                amount\n                priceBeforeDiscount\n              }\n              priceEur {\n                amount\n              }\n              provider {\n                name\n                code\n                hasHighProbabilityOfPriceChange\n                contentProvider {\n                  code\n                }\n                id\n              }\n              bagsInfo {\n                includedCheckedBags\n                includedHandBags\n                hasNoBaggageSupported\n                hasNoCheckedBaggage\n                checkedBagTiers {\n                  tierPrice {\n                    amount\n                  }\n                  bags {\n                    weight {\n                      value\n                    }\n                  }\n                }\n                handBagTiers {\n                  tierPrice {\n                    amount\n                  }\n                  bags {\n                    weight {\n                      value\n                    }\n                  }\n                }\n                includedPersonalItem\n                personalItemTiers {\n                  tierPrice {\n                    amount\n                  }\n                  bags {\n                    weight {\n                      value\n                    }\n                    height {\n                      value\n                    }\n                    width {\n                      value\n                    }\n                    length {\n                      value\n                    }\n                  }\n                }\n              }\n              bookingOptions {\n                edges {\n                  node {\n                    token\n                    bookingUrl\n                    trackingPixel\n                    itineraryProvider {\n                      code\n                      name\n                      subprovider\n                      hasHighProbabilityOfPriceChange\n                      contentProvider {\n                        code\n                      }\n                      id\n                    }\n                    price {\n                      amount\n                    }\n                  }\n                }\n              }\n              travelHack {\n                isTrueHiddenCity\n                isVirtualInterlining\n                isThrowawayTicket\n              }\n            }\n            legacyId\n            outbound {\n              id\n              sectorSegments {\n                guarantee\n                segment {\n                  id\n                  source {\n                    localTime\n                    utcTime\n                    station {\n                      id\n                      legacyId\n                      name\n                      code\n                      type\n                      gps {\n                        lat\n                        lng\n                      }\n                      city {\n                        legacyId\n                        name\n                        id\n                      }\n                      country {\n                        code\n                        id\n                      }\n                    }\n                  }\n                  destination {\n                    localTime\n                    utcTime\n                    station {\n                      id\n                      legacyId\n                      name\n                      code\n                      type\n                      gps {\n                        lat\n                        lng\n                      }\n                      city {\n                        legacyId\n                        name\n                        id\n                      }\n                      country {\n                        code\n                        id\n                      }\n                    }\n                  }\n                  duration\n                  type\n                  code\n                  carrier {\n                    id\n                    name\n                    code\n                  }\n                  operatingCarrier {\n                    id\n                    name\n                    code\n                  }\n                  cabinClass\n                  hiddenDestination {\n                    city {\n                      name\n                      id\n                    }\n                    id\n                  }\n                  throwawayDestination {\n                    id\n                  }\n                }\n                layover {\n                  duration\n                  isBaggageRecheck\n                  isWalkingDistance\n                  transferDuration\n                  id\n                }\n              }\n              duration\n            }\n            inbound {\n              id\n              sectorSegments {\n                guarantee\n                segment {\n                  id\n                  source {\n                    localTime\n                    utcTime\n                    station {\n                      id\n                      legacyId\n                      name\n                      code\n                      type\n                      gps {\n                        lat\n                        lng\n                      }\n                      city {\n                        legacyId\n                        name\n                        id\n                      }\n                      country {\n                        code\n                        id\n                      }\n                    }\n                  }\n                  destination {\n                    localTime\n                    utcTime\n                    station {\n                      id\n                      legacyId\n                      name\n                      code\n                      type\n                      gps {\n                        lat\n                        lng\n                      }\n                      city {\n                        legacyId\n                        name\n                        id\n                      }\n                      country {\n                        code\n                        id\n                      }\n                    }\n                  }\n                  duration\n                  type\n                  code\n                  carrier {\n                    id\n                    name\n                    code\n                  }\n                  operatingCarrier {\n                    id\n                    name\n                    code\n                  }\n                  cabinClass\n                  hiddenDestination {\n                    city {\n                      name\n                      id\n                    }\n                    id\n                  }\n                  throwawayDestination {\n                    id\n                  }\n                }\n                layover {\n                  duration\n                  isBaggageRecheck\n                  isWalkingDistance\n                  transferDuration\n                  id\n                }\n              }\n              duration\n            }\n            stopover {\n              nightsCount\n              arrival {\n                type\n                city {\n                  name\n                  id\n                }\n                id\n              }\n              departure {\n                type\n                id\n              }\n              duration\n            }\n            lastAvailable {\n              seatsLeft\n            }\n            extendedFareOptionsPricing {\n              standardFarePrice {\n                amount\n              }\n              flexiFarePrice {\n                amount\n              }\n            }\n          }\n          id\n        }\n        kayakEligibilityTest {\n          containsKayakWithNewRules\n          containsKayakWithCurrentRules\n        }\n      }\n      itineraries {\n        __typename\n        ... on ItineraryReturn {\n          ... on Itinerary {\n            __isItinerary: __typename\n            __typename\n            id\n            shareId\n            price {\n              amount\n              priceBeforeDiscount\n            }\n            priceEur {\n              amount\n            }\n            provider {\n              name\n              code\n              hasHighProbabilityOfPriceChange\n              contentProvider {\n                code\n              }\n              id\n            }\n            bagsInfo {\n              includedCheckedBags\n              includedHandBags\n              hasNoBaggageSupported\n              hasNoCheckedBaggage\n              checkedBagTiers {\n                tierPrice {\n                  amount\n                }\n                bags {\n                  weight {\n                    value\n                  }\n                }\n              }\n              handBagTiers {\n                tierPrice {\n                  amount\n                }\n                bags {\n                  weight {\n                    value\n                  }\n                }\n              }\n              includedPersonalItem\n              personalItemTiers {\n                tierPrice {\n                  amount\n                }\n                bags {\n                  weight {\n                    value\n                  }\n                  height {\n                    value\n                  }\n                  width {\n                    value\n                  }\n                  length {\n                    value\n                  }\n                }\n              }\n            }\n            bookingOptions {\n              edges {\n                node {\n                  token\n                  bookingUrl\n                  trackingPixel\n                  itineraryProvider {\n                    code\n                    name\n                    subprovider\n                    hasHighProbabilityOfPriceChange\n                    contentProvider {\n                      code\n                    }\n                    id\n                  }\n                  price {\n                    amount\n                  }\n                }\n              }\n            }\n            travelHack {\n              isTrueHiddenCity\n              isVirtualInterlining\n              isThrowawayTicket\n            }\n          }\n          legacyId\n          outbound {\n            id\n            sectorSegments {\n              guarantee\n              segment {\n                id\n                source {\n                  localTime\n                  utcTime\n                  station {\n                    id\n                    legacyId\n                    name\n                    code\n                    type\n                    gps {\n                      lat\n                      lng\n                    }\n                    city {\n                      legacyId\n                      name\n                      id\n                    }\n                    country {\n                      code\n                      id\n                    }\n                  }\n                }\n                destination {\n                  localTime\n                  utcTime\n                  station {\n                    id\n                    legacyId\n                    name\n                    code\n                    type\n                    gps {\n                      lat\n                      lng\n                    }\n                    city {\n                      legacyId\n                      name\n                      id\n                    }\n                    country {\n                      code\n                      id\n                    }\n                  }\n                }\n                duration\n                type\n                code\n                carrier {\n                  id\n                  name\n                  code\n                }\n                operatingCarrier {\n                  id\n                  name\n                  code\n                }\n                cabinClass\n                hiddenDestination {\n                  city {\n                    name\n                    id\n                  }\n                  id\n                }\n                throwawayDestination {\n                  id\n                }\n              }\n              layover {\n                duration\n                isBaggageRecheck\n                isWalkingDistance\n                transferDuration\n                id\n              }\n            }\n            duration\n          }\n          inbound {\n            id\n            sectorSegments {\n              guarantee\n              segment {\n                id\n                source {\n                  localTime\n                  utcTime\n                  station {\n                    id\n                    legacyId\n                    name\n                    code\n                    type\n                    gps {\n                      lat\n                      lng\n                    }\n                    city {\n                      legacyId\n                      name\n                      id\n                    }\n                    country {\n                      code\n                      id\n                    }\n                  }\n                }\n                destination {\n                  localTime\n                  utcTime\n                  station {\n                    id\n                    legacyId\n                    name\n                    code\n                    type\n                    gps {\n                      lat\n                      lng\n                    }\n                    city {\n                      legacyId\n                      name\n                      id\n                    }\n                    country {\n                      code\n                      id\n                    }\n                  }\n                }\n                duration\n                type\n                code\n                carrier {\n                  id\n                  name\n                  code\n                }\n                operatingCarrier {\n                  id\n                  name\n                  code\n                }\n                cabinClass\n                hiddenDestination {\n                  city {\n                    name\n                    id\n                  }\n                  id\n                }\n                throwawayDestination {\n                  id\n                }\n              }\n              layover {\n                duration\n                isBaggageRecheck\n                isWalkingDistance\n                transferDuration\n                id\n              }\n            }\n            duration\n          }\n          stopover {\n            nightsCount\n            arrival {\n              type\n              city {\n                name\n                id\n              }\n              id\n            }\n            departure {\n              type\n              id\n            }\n            duration\n          }\n          lastAvailable {\n            seatsLeft\n          }\n          extendedFareOptionsPricing {\n            standardFarePrice {\n              amount\n            }\n            flexiFarePrice {\n              amount\n            }\n          }\n        }\n        id\n      }\n    }\n  }\n}\n\nfragment AirlinesFilter_data on ItinerariesMetadata {\n  carriers {\n    id\n    code\n    name\n  }\n}\n\nfragment CountriesFilter_data on ItinerariesMetadata {\n  stopoverCountries {\n    code\n    name\n    id\n  }\n}\n\nfragment MobileSortingLink_data on ItinerariesMetadata {\n  topResults {\n    best {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    cheapest {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    fastest {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    sourceTakeoffAsc {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    destinationLandingAsc {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n  }\n}\n\nfragment MobileSorting_data on ItinerariesMetadata {\n  topResults {\n    best {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    cheapest {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    fastest {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    sourceTakeoffAsc {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    destinationLandingAsc {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n  }\n}\n\nfragment PriceAlert_data on ItinerariesMetadata {\n  priceAlertExists\n  existingPriceAlert {\n    id\n  }\n  searchFingerprint\n  hasMorePending\n  priceAlertsTopResults {\n    best {\n      price {\n        amount\n      }\n    }\n    cheapest {\n      price {\n        amount\n      }\n    }\n    fastest {\n      price {\n        amount\n      }\n    }\n    sourceTakeoffAsc {\n      price {\n        amount\n      }\n    }\n    destinationLandingAsc {\n      price {\n        amount\n      }\n    }\n  }\n}\n\nfragment Sorting_data on ItinerariesMetadata {\n  topResults {\n    best {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    cheapest {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    fastest {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    sourceTakeoffAsc {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    destinationLandingAsc {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n  }\n}\n\nfragment TravelTip_data on ItinerariesMetadata {\n  travelTips {\n    __typename\n    ... on TravelTipRadiusMoney {\n      radius\n      params {\n        name\n        value\n      }\n      savingMoney: saving {\n        amount\n        currency {\n          id\n          code\n          name\n        }\n        formattedValue\n      }\n      location {\n        __typename\n        id\n        legacyId\n        name\n        slug\n      }\n    }\n    ... on TravelTipRadiusTime {\n      radius\n      params {\n        name\n        value\n      }\n      saving\n      location {\n        __typename\n        id\n        legacyId\n        name\n        slug\n      }\n    }\n    ... on TravelTipRadiusSome {\n      radius\n      params {\n        name\n        value\n      }\n      location {\n        __typename\n        id\n        legacyId\n        name\n        slug\n      }\n    }\n    ... on TravelTipDateMoney {\n      dates {\n        start\n        end\n      }\n      params {\n        name\n        value\n      }\n      savingMoney: saving {\n        amount\n        currency {\n          id\n          code\n          name\n        }\n        formattedValue\n      }\n    }\n    ... on TravelTipDateTime {\n      dates {\n        start\n        end\n      }\n      params {\n        name\n        value\n      }\n      saving\n    }\n    ... on TravelTipDateSome {\n      dates {\n        start\n        end\n      }\n      params {\n        name\n        value\n      }\n    }\n    ... on TravelTipExtend {\n      destination {\n        __typename\n        id\n        name\n        slug\n      }\n      locations {\n        __typename\n        id\n        name\n        slug\n      }\n      price {\n        amount\n        currency {\n          id\n          code\n          name\n        }\n        formattedValue\n      }\n    }\n  }\n}\n\nfragment WeekDaysFilter_data on ItinerariesMetadata {\n  inboundDays\n  outboundDays\n}\n",
                        "variables": {
                            "search": {
                                "itinerary": {
                                    "source": form_data["source"],
                                    "destination": form_data["destination"],
                                    "outboundDepartureDate": {
                                        "start": utils.format_date(d) + "T00:00:00",
                                        "end": utils.format_date(d) + "T23:59:59"
                                    },
                                    "inboundDepartureDate": {
                                        "start": utils.format_date(return_date) + "T00:00:00",
                                        "end": utils.format_date(return_date) + "T23:59:59"
                                    }
                                },
                                "passengers": {
                                    "adults": 1,
                                    "children": 0,
                                    "infants": 0,
                                    "adultsHoldBags": [
                                        0
                                    ],
                                    "adultsHandBags": [
                                        0
                                    ],
                                    "childrenHoldBags": [],
                                    "childrenHandBags": []
                                },
                                "cabinClass": {
                                    "cabinClass": "ECONOMY",
                                    "applyMixedClasses": False
                                }
                            },
                            "filter": {
                                "allowReturnFromDifferentCity": True,
                                "allowChangeInboundDestination": True,
                                "allowChangeInboundSource": True,
                                "allowDifferentStationConnection": True,
                                "enableSelfTransfer": True,
                                "enableThrowAwayTicketing": True,
                                "enableTrueHiddenCity": True,
                                "maxStopsCount": 0,
                                "transportTypes": [
                                    "FLIGHT"
                                ],
                                "contentProviders": [
                                    "KIWI",
                                    "FRESH"
                                ],
                                "flightsApiLimit": 25,
                                "limit": 30
                            },
                            # minimal options payload to satisfy GraphQL schema (avoid None/unknown fields)
                            "options": {
                                "sortBy": "QUALITY",
                                "currency": form_data.get("currency", "usd"),
                                "locale": form_data.get("locale", "en"),
                                "partner": form_data.get("partner", "skypicker"),
                                "storeSearch": False
                            }
                        },
                    }

            # Add optional website-proven option fields only if provided (avoid schema 400s)
            extra_option_keys = [
                "market",
                "partnerMarket",
                "affilID",
                "searchStrategy",
                "mergePriceDiffRule",
                "searchSessionId",
                "serverToken",
            ]
            for k in extra_option_keys:
                if form_data.get(k) is not None:
                    request_data["variables"]["options"][k] = form_data.get(k)
            headers = {
                'Accept':'*/*',
                'Accept-Encoding':'gzip, deflate, br',
                'Accept-Language':'en-US,en;q=0.9',
                'Content-Type':'application/json',
                'Kw-Skypicker-Visitor-Uniqid': form_data.get('Kw-Skypicker-Visitor-Uniqid', 'b2bc59fe-9ac4-431a-9331-42c5f20ffc49'),
                'Kw-Umbrella-Token':form_data['Kw-Umbrella-Token'],
                'Origin':'https://www.kiwi.com',
                'Referer':'https://www.kiwi.com/',
                'Sec-Ch-Ua':'"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
                'Sec-Ch-Ua-Mobile':'?0',
                'Sec-Ch-Ua-Platform':'"Windows"',
                'Sec-Fetch-Dest':'empty',
                'Sec-Fetch-Mode':'cors',
                'Sec-Fetch-Site':'cross-site',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
            }

            # Allow passing through additional headers from captured website request
            for hk, hv in (form_data.get("extra_headers") or {}).items():
                if hv is not None and hv != "":
                    headers[hk] = hv
            
            try:
                # retry up to 3 times for non-200 responses with simple exponential backoff
                max_retries = 3
                backoff = 1
                response = None
                for attempt in range(1, max_retries + 1):
                    try:
                        response = requests.post('https://api.skypicker.com/umbrella/v2/graphql?featureName=SearchReturnItinerariesQuery', headers=headers, json=request_data, timeout=30)
                    except requests.exceptions.RequestException as e:
                        # network error — retry
                        if attempt == max_retries:
                            raise
                        time.sleep(backoff)
                        backoff *= 2
                        continue

                    if response.status_code == 200:
                        break
                    # for 4xx/5xx, log snippet and retry a few times
                    # Try to print structured GraphQL errors (esp. important for HTTP 400 validation problems)
                    try:
                        body = response.content.decode("utf-8", errors="replace")
                        parsed = json.loads(body)
                        gql_errors = parsed.get("errors")
                        if gql_errors:
                            print(
                                f"Error: HTTP {response.status_code} (attempt {attempt}) for {utils.format_date(d)} -> {request_data['variables']['search']['itinerary'].get('outboundDepartureDate')}; errors: {json.dumps(gql_errors, ensure_ascii=False)}"
                            )
                        else:
                            print(
                                f"Error: HTTP {response.status_code} (attempt {attempt}) for {utils.format_date(d)} -> {request_data['variables']['search']['itinerary'].get('outboundDepartureDate')}; body: {body[:1500]}"
                            )
                    except Exception:
                        snippet = response.content[:500]
                        print(f"Error: HTTP {response.status_code} (attempt {attempt}) for {utils.format_date(d)} -> {request_data['variables']['search']['itinerary'].get('outboundDepartureDate')}; snippet: {snippet}")
                    if attempt == max_retries:
                        error = True
                        # stop retrying this date
                        response = None
                        break
                    time.sleep(backoff)
                    backoff *= 2

                if response is None:
                    # no successful response for this request — continue to next nights/date
                    continue

                # Parse string to Python dictionary safely
                try:
                    string_response = response.content.decode('utf-8')
                    json_response = json.loads(string_response)
                except Exception as e:
                    error = True
                    print(f"Error decoding JSON response: {e}; snippet: {response.content[:200]}")
                    continue

                # Navigate response with guards
                data = json_response.get('data') or {}
                returnItineraries = data.get('returnItineraries') or {}
                original_itineraries = returnItineraries.get('itineraries')

                # High-signal debug info (helps detect parsing vs genuinely empty)
                ri_typename = returnItineraries.get('__typename')
                if ri_typename and ri_typename != 'Itineraries':
                    # Union type: AppError etc.
                    if returnItineraries.get('error'):
                        print(f"returnItineraries type={ri_typename} error={returnItineraries.get('error')}")
                    else:
                        print(f"returnItineraries type={ri_typename} (no error message field found)")

                if not original_itineraries:
                    # Nothing to process for this search
                    meta = returnItineraries.get('metadata') or {}
                    # print debug line with metadata counts/providers
                    print(
                        f"No itineraries returned for {utils.format_date(d)} -> {utils.format_date(return_date)}; "
                        f"__typename={ri_typename}; itinerariesCount={meta.get('itinerariesCount')}; "
                        f"hasMorePending={meta.get('hasMorePending')}; missingProviders={meta.get('missingProviders')}"
                    )
                    continue

                # helper to safely get nested values
                def safe_get(obj, *keys, default=None):
                    try:
                        for k in keys:
                            if obj is None:
                                return default
                            obj = obj[k]
                        return obj
                    except Exception:
                        return default

                for itinerary in original_itineraries:
                    # extract fields safely; skip itinerary if essential fields are missing
                    price = safe_get(itinerary, 'price', 'amount')
                    if price is None:
                        # skip incomplete itinerary
                        continue

                    simplified = {
                        'Price Amount': price,
                        'included Checked Bags': safe_get(itinerary, 'bagsInfo', 'includedCheckedBags'),
                        'Included Hand Bags': safe_get(itinerary, 'bagsInfo', 'includedHandBags'),
                        'Nights': safe_get(itinerary, 'stopover', 'nightsCount'),
                        'Departure Time Out': safe_get(itinerary, 'outbound', 'sectorSegments', 0, 'segment', 'source', 'localTime'),
                        'Departure Time Return': safe_get(itinerary, 'inbound', 'sectorSegments', 0, 'segment', 'source', 'localTime'),
                        'Seats Left': safe_get(itinerary, 'lastAvailable', 'seatsLeft'),
                        'Carrier Out': safe_get(itinerary, 'outbound', 'sectorSegments', 0, 'segment', 'carrier', 'name'),
                        'Carrier Return': safe_get(itinerary, 'inbound', 'sectorSegments', 0, 'segment', 'carrier', 'name'),
                        'Out Duration': None,
                        'Return  Duration': None,
                        'Out Arrival Time': safe_get(itinerary, 'outbound', 'sectorSegments', 0, 'segment', 'destination', 'localTime'),
                        'Return Arrival Time': safe_get(itinerary, 'inbound', 'sectorSegments', 0, 'segment', 'destination', 'localTime'),
                        'Standard Fare Price': safe_get(itinerary, 'extendedFareOptionsPricing', 'standardFarePrice', 'amount'),
                        'Flexi Fare Price': safe_get(itinerary, 'extendedFareOptionsPricing', 'flexiFarePrice', 'amount')
                    }

                    out_dur = safe_get(itinerary, 'outbound', 'duration')
                    in_dur = safe_get(itinerary, 'inbound', 'duration')
                    try:
                        if out_dur is not None:
                            simplified['Out Duration'] = str(round((out_dur/3600), 2)) + " hours"
                        if in_dur is not None:
                            simplified['Return  Duration'] = str(round((in_dur/3600), 2)) + " hours"
                    except Exception:
                        pass

                    simplified_itineraries.append(simplified)

            except requests.exceptions.RequestException as e:
                error = True
                print(f"Request error: {e}")
            except Exception as e:
                error = True
                print(f"Unexpected error: {e}")
            
            # Wait for x seconds before sending the next request (optional)
            random_float = random.uniform(form_data['minWaitTime'], form_data['maxWaitTime'])
            time.sleep(random_float)

            
        d += timedelta(days=1)
            
            

    if not error:
        # Sort by 'priceAmount' in ascending order
        sorted_itineraries = sorted(simplified_itineraries, key=lambda x: float(x['Price Amount']))
        return sorted_itineraries
    
    return simplified_itineraries

def search_1_way(form_data):
    simplified_itineraries = []
    error = False

    start_date = datetime.strptime(form_data['startDate'], '%Y-%m-%d')
    end_date = datetime.strptime(form_data['endDate'], '%Y-%m-%d')

    d = start_date
    while d <= end_date:  # Loop through the start dates
        print(f"Scanning departure date: {utils.format_date(d)}")
        request_data = {
            "query": "query SearchOneWayItinerariesQuery(\n  $search: SearchOnewayInput\n  $filter: ItinerariesFilterInput\n  $options: ItinerariesOptionsInput\n) {\n  onewayItineraries(search: $search, filter: $filter, options: $options) {\n    __typename\n    ... on AppError {\n      error: message\n    }\n    ... on Itineraries {\n      server {\n        requestId\n        environment\n        packageVersion\n        serverToken\n      }\n      metadata {\n        eligibilityInformation {\n          baggageEligibilityInformation {\n            topFiveResultsBaggageEligibleForPrompt\n            topFifteenResultsBaggageEligibleForPrompt\n            searchIsLongTrip\n            searchIsFamilyTrip\n            numberOfBags\n          }\n        }\n        ...AirlinesFilter_data\n        ...CountriesFilter_data\n        ...WeekDaysFilter_data\n        ...TravelTip_data\n        ...Sorting_data\n        ...MobileSorting_data\n        ...MobileSortingLink_data\n        ...PriceAlert_data\n        itinerariesCount\n        hasMorePending\n        missingProviders {\n          code\n        }\n        searchFingerprint\n        statusPerProvider {\n          provider {\n            id\n          }\n          errorHappened\n          errorMessage\n        }\n        topFiveOriginalItinerariesContainTHC\n        hasTier1MarketItineraries\n        sharedItinerary {\n          __typename\n          ... on ItineraryOneWay {\n            ... on Itinerary {\n              __isItinerary: __typename\n              __typename\n              id\n              shareId\n              price {\n                amount\n                priceBeforeDiscount\n              }\n              priceEur {\n                amount\n              }\n              provider {\n                name\n                code\n                hasHighProbabilityOfPriceChange\n                contentProvider {\n                  code\n                }\n                id\n              }\n              bagsInfo {\n                includedCheckedBags\n                includedHandBags\n                hasNoBaggageSupported\n                hasNoCheckedBaggage\n                checkedBagTiers {\n                  tierPrice {\n                    amount\n                  }\n                  bags {\n                    weight {\n                      value\n                    }\n                  }\n                }\n                handBagTiers {\n                  tierPrice {\n                    amount\n                  }\n                  bags {\n                    weight {\n                      value\n                    }\n                  }\n                }\n                includedPersonalItem\n                personalItemTiers {\n                  tierPrice {\n                    amount\n                  }\n                  bags {\n                    weight {\n                      value\n                    }\n                    height {\n                      value\n                    }\n                    width {\n                      value\n                    }\n                    length {\n                      value\n                    }\n                  }\n                }\n              }\n              bookingOptions {\n                edges {\n                  node {\n                    token\n                    bookingUrl\n                    trackingPixel\n                    itineraryProvider {\n                      code\n                      name\n                      subprovider\n                      hasHighProbabilityOfPriceChange\n                      contentProvider {\n                        code\n                      }\n                      id\n                    }\n                    price {\n                      amount\n                    }\n                  }\n                }\n              }\n              travelHack {\n                isTrueHiddenCity\n                isVirtualInterlining\n                isThrowawayTicket\n              }\n            }\n            legacyId\n            sector {\n              id\n              sectorSegments {\n                guarantee\n                segment {\n                  id\n                  source {\n                    localTime\n                    utcTime\n                    station {\n                      id\n                      legacyId\n                      name\n                      code\n                      type\n                      gps {\n                        lat\n                        lng\n                      }\n                      city {\n                        legacyId\n                        name\n                        id\n                      }\n                      country {\n                        code\n                        id\n                      }\n                    }\n                  }\n                  destination {\n                    localTime\n                    utcTime\n                    station {\n                      id\n                      legacyId\n                      name\n                      code\n                      type\n                      gps {\n                        lat\n                        lng\n                      }\n                      city {\n                        legacyId\n                        name\n                        id\n                      }\n                      country {\n                        code\n                        id\n                      }\n                    }\n                  }\n                  duration\n                  type\n                  code\n                  carrier {\n                    id\n                    name\n                    code\n                  }\n                  operatingCarrier {\n                    id\n                    name\n                    code\n                  }\n                  cabinClass\n                  hiddenDestination {\n                    city {\n                      name\n                      id\n                    }\n                    id\n                  }\n                  throwawayDestination {\n                    id\n                  }\n                }\n                layover {\n                  duration\n                  isBaggageRecheck\n                  isWalkingDistance\n                  transferDuration\n                  id\n                }\n              }\n              duration\n            }\n            lastAvailable {\n              seatsLeft\n            }\n            extendedFareOptionsPricing {\n              standardFarePrice {\n                amount\n              }\n              flexiFarePrice {\n                amount\n              }\n            }\n          }\n          id\n        }\n        kayakEligibilityTest {\n          containsKayakWithNewRules\n          containsKayakWithCurrentRules\n        }\n      }\n      itineraries {\n        __typename\n        ... on ItineraryOneWay {\n          ... on Itinerary {\n            __isItinerary: __typename\n            __typename\n            id\n            shareId\n            price {\n              amount\n              priceBeforeDiscount\n            }\n            priceEur {\n              amount\n            }\n            provider {\n              name\n              code\n              hasHighProbabilityOfPriceChange\n              contentProvider {\n                code\n              }\n              id\n            }\n            bagsInfo {\n              includedCheckedBags\n              includedHandBags\n              hasNoBaggageSupported\n              hasNoCheckedBaggage\n              checkedBagTiers {\n                tierPrice {\n                  amount\n                }\n                bags {\n                  weight {\n                    value\n                  }\n                }\n              }\n              handBagTiers {\n                tierPrice {\n                  amount\n                }\n                bags {\n                  weight {\n                    value\n                  }\n                }\n              }\n              includedPersonalItem\n              personalItemTiers {\n                tierPrice {\n                  amount\n                }\n                bags {\n                  weight {\n                    value\n                  }\n                  height {\n                    value\n                  }\n                  width {\n                    value\n                  }\n                  length {\n                    value\n                  }\n                }\n              }\n            }\n            bookingOptions {\n              edges {\n                node {\n                  token\n                  bookingUrl\n                  trackingPixel\n                  itineraryProvider {\n                    code\n                    name\n                    subprovider\n                    hasHighProbabilityOfPriceChange\n                    contentProvider {\n                      code\n                    }\n                    id\n                  }\n                  price {\n                    amount\n                  }\n                }\n              }\n            }\n            travelHack {\n              isTrueHiddenCity\n              isVirtualInterlining\n              isThrowawayTicket\n            }\n          }\n          legacyId\n          sector {\n            id\n            sectorSegments {\n              guarantee\n              segment {\n                id\n                source {\n                  localTime\n                  utcTime\n                  station {\n                    id\n                    legacyId\n                    name\n                    code\n                    type\n                    gps {\n                      lat\n                      lng\n                    }\n                    city {\n                      legacyId\n                      name\n                      id\n                    }\n                    country {\n                      code\n                      id\n                    }\n                  }\n                }\n                destination {\n                  localTime\n                  utcTime\n                  station {\n                    id\n                    legacyId\n                    name\n                    code\n                    type\n                    gps {\n                      lat\n                      lng\n                    }\n                    city {\n                      legacyId\n                      name\n                      id\n                    }\n                    country {\n                      code\n                      id\n                    }\n                  }\n                }\n                duration\n                type\n                code\n                carrier {\n                  id\n                  name\n                  code\n                }\n                operatingCarrier {\n                  id\n                  name\n                  code\n                }\n                cabinClass\n                hiddenDestination {\n                  city {\n                    name\n                    id\n                  }\n                  id\n                }\n                throwawayDestination {\n                  id\n                }\n              }\n              layover {\n                duration\n                isBaggageRecheck\n                isWalkingDistance\n                transferDuration\n                id\n              }\n            }\n            duration\n          }\n          lastAvailable {\n            seatsLeft\n          }\n          extendedFareOptionsPricing {\n            standardFarePrice {\n              amount\n            }\n            flexiFarePrice {\n              amount\n            }\n          }\n        }\n        id\n      }\n    }\n  }\n}\n\nfragment AirlinesFilter_data on ItinerariesMetadata {\n  carriers {\n    id\n    code\n    name\n  }\n}\n\nfragment CountriesFilter_data on ItinerariesMetadata {\n  stopoverCountries {\n    code\n    name\n    id\n  }\n}\n\nfragment MobileSortingLink_data on ItinerariesMetadata {\n  topResults {\n    best {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    cheapest {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    fastest {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    sourceTakeoffAsc {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    destinationLandingAsc {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n  }\n}\n\nfragment MobileSorting_data on ItinerariesMetadata {\n  topResults {\n    best {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    cheapest {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    fastest {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    sourceTakeoffAsc {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    destinationLandingAsc {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n  }\n}\n\nfragment PriceAlert_data on ItinerariesMetadata {\n  priceAlertExists\n  existingPriceAlert {\n    id\n  }\n  searchFingerprint\n  hasMorePending\n  priceAlertsTopResults {\n    best {\n      price {\n        amount\n      }\n    }\n    cheapest {\n      price {\n        amount\n      }\n    }\n    fastest {\n      price {\n        amount\n      }\n    }\n    sourceTakeoffAsc {\n      price {\n        amount\n      }\n    }\n    destinationLandingAsc {\n      price {\n        amount\n      }\n    }\n  }\n}\n\nfragment Sorting_data on ItinerariesMetadata {\n  topResults {\n    best {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    cheapest {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    fastest {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    sourceTakeoffAsc {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    destinationLandingAsc {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n  }\n}\n\nfragment TravelTip_data on ItinerariesMetadata {\n  travelTips {\n    __typename\n    ... on TravelTipRadiusMoney {\n      radius\n      params {\n        name\n        value\n      }\n      savingMoney: saving {\n        amount\n        currency {\n          id\n          code\n          name\n        }\n        formattedValue\n      }\n      location {\n        __typename\n        id\n        legacyId\n        name\n        slug\n      }\n    }\n    ... on TravelTipRadiusTime {\n      radius\n      params {\n        name\n        value\n      }\n      saving\n      location {\n        __typename\n        id\n        legacyId\n        name\n        slug\n      }\n    }\n    ... on TravelTipRadiusSome {\n      radius\n      params {\n        name\n        value\n      }\n      location {\n        __typename\n        id\n        legacyId\n        name\n        slug\n      }\n    }\n    ... on TravelTipDateMoney {\n      dates {\n        start\n        end\n      }\n      params {\n        name\n        value\n      }\n      savingMoney: saving {\n        amount\n        currency {\n          id\n          code\n          name\n        }\n        formattedValue\n      }\n    }\n    ... on TravelTipDateTime {\n      dates {\n        start\n        end\n      }\n      params {\n        name\n        value\n      }\n      saving\n    }\n    ... on TravelTipDateSome {\n      dates {\n        start\n        end\n      }\n      params {\n        name\n        value\n      }\n    }\n    ... on TravelTipExtend {\n      destination {\n        __typename\n        id\n        name\n        slug\n      }\n      locations {\n        __typename\n        id\n        name\n        slug\n      }\n      price {\n        amount\n        currency {\n          id\n          code\n          name\n        }\n        formattedValue\n      }\n    }\n  }\n}\n\nfragment WeekDaysFilter_data on ItinerariesMetadata {\n  inboundDays\n  outboundDays\n}\n",
            "variables": {
                "search": {
                    "itinerary": {
                        "source": form_data['source'],
                        "destination": form_data['destination'],
                        "outboundDepartureDate": {
                            "start": utils.format_date(d) + "T00:00:00",
                            "end": utils.format_date(d) + "T23:59:59"
                        }
                    },
                    "passengers": {
                        "adults": 1,
                        "children": 0,
                        "infants": 0,
                        "adultsHoldBags": [
                            0
                        ],
                        "adultsHandBags": [
                            0
                        ],
                        "childrenHoldBags": [],
                        "childrenHandBags": []
                    },
                    "cabinClass": {
                        "cabinClass": "ECONOMY",
                        "applyMixedClasses": True
                    }
                },
                "filter": {
                    "allowChangeInboundDestination": True,
                    "allowChangeInboundSource": True,
                    "allowDifferentStationConnection": True,
                    "enableSelfTransfer": True,
                    "enableThrowAwayTicketing": True,
                    "enableTrueHiddenCity": True,
                    "maxStopsCount": 0,
                    "transportTypes": [
                        "FLIGHT"
                    ],
                    "contentProviders": [
                        "KIWI"
                    ],
                    "flightsApiLimit": 25,
                    "limit": 30
                },
                # minimal options payload to satisfy GraphQL schema (avoid None/unknown fields)
                "options": {
                    "sortBy": "QUALITY",
                    "currency": "usd",
                    "locale": "en",
                    "partner": "skypicker",
                    "storeSearch": False
                }
            }
        }
        headers = {
            'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'en-US,en;q=0.9',
            'Content-Type':'application/json',
            'Kw-Skypicker-Visitor-Uniqid':'b2bc59fe-9ac4-431a-9331-42c5f20ffc49',
            'Kw-Umbrella-Token':form_data['Kw-Umbrella-Token'],
            'Origin':'https://www.kiwi.com',
            'Referer':'https://www.kiwi.com/',
            'Sec-Ch-Ua':'"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':'"Windows"',
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'cross-site',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
        }
        
        try:
            max_retries = 3
            backoff = 1
            response = None
            for attempt in range(1, max_retries + 1):
                try:
                    response = requests.post('https://api.skypicker.com/umbrella/v2/graphql?featureName=SearchOneWayItinerariesQuery', headers=headers, json=request_data, timeout=30)
                except requests.exceptions.RequestException as e:
                    if attempt == max_retries:
                        raise
                    time.sleep(backoff)
                    backoff *= 2
                    continue

                if response.status_code == 200:
                    break

                snippet = response.content[:500]
                print(f"Error: HTTP {response.status_code} (attempt {attempt}) for oneway {utils.format_date(d)}; snippet: {snippet}")
                if attempt == max_retries:
                    error = True
                    response = None
                    break
                time.sleep(backoff)
                backoff *= 2

            if response is None:
                d += timedelta(days=1)
                continue

            # Parse JSON safely
            try:
                string_response = response.content.decode('utf-8')
                json_response = json.loads(string_response)
            except Exception as e:
                error = True
                print(f"Error decoding JSON (oneway): {e}; snippet: {response.content[:200]}")
                d += timedelta(days=1)
                continue

            data = json_response.get('data') or {}
            one_way = data.get('onewayItineraries') or {}
            original_itineraries = one_way.get('itineraries')

            if not original_itineraries:
                print(f"No one-way itineraries for {utils.format_date(d)}")
                # wait then continue
                random_float = random.uniform(form_data['minWaitTime'], form_data['maxWaitTime'])
                time.sleep(random_float)
                d += timedelta(days=1)
                continue

            # safe_get helper (keep same behavior as round search)
            def safe_get(obj, *keys, default=None):
                try:
                    for k in keys:
                        if obj is None:
                            return default
                        obj = obj[k]
                    return obj
                except Exception:
                    return default

            for itinerary in original_itineraries:
                price = safe_get(itinerary, 'price', 'amount')
                if price is None:
                    continue

                simplified = {
                    'Price Amount': price,
                    'included Checked Bags': safe_get(itinerary, 'bagsInfo', 'includedCheckedBags'),
                    'Included Hand Bags': safe_get(itinerary, 'bagsInfo', 'includedHandBags'),
                    'Departure Time': safe_get(itinerary, 'sector', 'sectorSegments', 0, 'segment', 'source', 'localTime'),
                    'Arrival Time': safe_get(itinerary, 'sector', 'sectorSegments', 0, 'segment', 'destination', 'localTime'),
                    'Seats Left': safe_get(itinerary, 'lastAvailable', 'seatsLeft'),
                    'Carrier': safe_get(itinerary, 'sector', 'sectorSegments', 0, 'segment', 'carrier', 'name'),
                    'Duration': None,
                    'Standard Fare Price': safe_get(itinerary, 'extendedFareOptionsPricing', 'standardFarePrice', 'amount'),
                    'Flexi Fare Price': safe_get(itinerary, 'extendedFareOptionsPricing', 'flexiFarePrice', 'amount')
                }

                dur = safe_get(itinerary, 'sector', 'duration')
                try:
                    if dur is not None:
                        simplified['Duration'] = str(round((dur/3600), 2)) + " hours"
                except Exception:
                    pass

                simplified_itineraries.append(simplified)

        except requests.exceptions.RequestException as e:
            error = True
            print(f"Request error (oneway): {e}")
            
        # Wait for x seconds before sending the next request (optional)
        random_float = random.uniform(form_data['minWaitTime'], form_data['maxWaitTime'])
        time.sleep(random_float)

            
        d += timedelta(days=1)
            
            

    if not error:
        # Sort by 'priceAmount' in ascending order
        sorted_itineraries = sorted(simplified_itineraries, key=lambda x: float(x['Price Amount']))
        return sorted_itineraries
        
         

    return simplified_itineraries 
