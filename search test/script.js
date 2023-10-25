var simplifiedItineraries = [];
var error = false;

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('searchForm');
  
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
    
        const nights = parseInt(form.nights.value);  // Fixed to 7 nights
        const startDate = new Date(form.startDate.value);
        const endDate = new Date(form.endDate.value);
        let loopEndDate = new Date(endDate);
        loopEndDate.setDate(loopEndDate.getDate() - nights);

        // Iterate through each start date within the modified range
        for (let d = new Date(startDate); d <= loopEndDate; d.setDate(d.getDate() + 1)) {
            let returnDate = new Date(d);
            returnDate.setDate(returnDate.getDate() + nights);
    
            if (returnDate > endDate) {
                break;
            }
    
            let requestData = JSON.stringify(
            {
                "query": "query SearchReturnItinerariesQuery(\n  $search: SearchReturnInput\n  $filter: ItinerariesFilterInput\n  $options: ItinerariesOptionsInput\n) {\n  returnItineraries(search: $search, filter: $filter, options: $options) {\n    __typename\n    ... on AppError {\n      error: message\n    }\n    ... on Itineraries {\n      server {\n        requestId\n        environment\n        packageVersion\n        serverToken\n      }\n      metadata {\n        eligibilityInformation {\n          baggageEligibilityInformation {\n            topFiveResultsBaggageEligibleForPrompt\n            topFifteenResultsBaggageEligibleForPrompt\n            searchIsLongTrip\n            searchIsFamilyTrip\n            numberOfBags\n          }\n        }\n        ...AirlinesFilter_data\n        ...CountriesFilter_data\n        ...WeekDaysFilter_data\n        ...TravelTip_data\n        ...Sorting_data\n        ...MobileSorting_data\n        ...MobileSortingLink_data\n        ...PriceAlert_data\n        itinerariesCount\n        hasMorePending\n        missingProviders {\n          code\n        }\n        searchFingerprint\n        statusPerProvider {\n          provider {\n            id\n          }\n          errorHappened\n          errorMessage\n        }\n        topFiveOriginalItinerariesContainTHC\n        hasTier1MarketItineraries\n        sharedItinerary {\n          __typename\n          ... on ItineraryReturn {\n            ... on Itinerary {\n              __isItinerary: __typename\n              __typename\n              id\n              shareId\n              price {\n                amount\n                priceBeforeDiscount\n              }\n              priceEur {\n                amount\n              }\n              provider {\n                name\n                code\n                hasHighProbabilityOfPriceChange\n                contentProvider {\n                  code\n                }\n                id\n              }\n              bagsInfo {\n                includedCheckedBags\n                includedHandBags\n                hasNoBaggageSupported\n                hasNoCheckedBaggage\n                checkedBagTiers {\n                  tierPrice {\n                    amount\n                  }\n                  bags {\n                    weight {\n                      value\n                    }\n                  }\n                }\n                handBagTiers {\n                  tierPrice {\n                    amount\n                  }\n                  bags {\n                    weight {\n                      value\n                    }\n                  }\n                }\n                includedPersonalItem\n                personalItemTiers {\n                  tierPrice {\n                    amount\n                  }\n                  bags {\n                    weight {\n                      value\n                    }\n                    height {\n                      value\n                    }\n                    width {\n                      value\n                    }\n                    length {\n                      value\n                    }\n                  }\n                }\n              }\n              bookingOptions {\n                edges {\n                  node {\n                    token\n                    bookingUrl\n                    trackingPixel\n                    itineraryProvider {\n                      code\n                      name\n                      subprovider\n                      hasHighProbabilityOfPriceChange\n                      contentProvider {\n                        code\n                      }\n                      id\n                    }\n                    price {\n                      amount\n                    }\n                  }\n                }\n              }\n              travelHack {\n                isTrueHiddenCity\n                isVirtualInterlining\n                isThrowawayTicket\n              }\n            }\n            legacyId\n            outbound {\n              id\n              sectorSegments {\n                guarantee\n                segment {\n                  id\n                  source {\n                    localTime\n                    utcTime\n                    station {\n                      id\n                      legacyId\n                      name\n                      code\n                      type\n                      gps {\n                        lat\n                        lng\n                      }\n                      city {\n                        legacyId\n                        name\n                        id\n                      }\n                      country {\n                        code\n                        id\n                      }\n                    }\n                  }\n                  destination {\n                    localTime\n                    utcTime\n                    station {\n                      id\n                      legacyId\n                      name\n                      code\n                      type\n                      gps {\n                        lat\n                        lng\n                      }\n                      city {\n                        legacyId\n                        name\n                        id\n                      }\n                      country {\n                        code\n                        id\n                      }\n                    }\n                  }\n                  duration\n                  type\n                  code\n                  carrier {\n                    id\n                    name\n                    code\n                  }\n                  operatingCarrier {\n                    id\n                    name\n                    code\n                  }\n                  cabinClass\n                  hiddenDestination {\n                    city {\n                      name\n                      id\n                    }\n                    id\n                  }\n                  throwawayDestination {\n                    id\n                  }\n                }\n                layover {\n                  duration\n                  isBaggageRecheck\n                  isWalkingDistance\n                  transferDuration\n                  id\n                }\n              }\n              duration\n            }\n            inbound {\n              id\n              sectorSegments {\n                guarantee\n                segment {\n                  id\n                  source {\n                    localTime\n                    utcTime\n                    station {\n                      id\n                      legacyId\n                      name\n                      code\n                      type\n                      gps {\n                        lat\n                        lng\n                      }\n                      city {\n                        legacyId\n                        name\n                        id\n                      }\n                      country {\n                        code\n                        id\n                      }\n                    }\n                  }\n                  destination {\n                    localTime\n                    utcTime\n                    station {\n                      id\n                      legacyId\n                      name\n                      code\n                      type\n                      gps {\n                        lat\n                        lng\n                      }\n                      city {\n                        legacyId\n                        name\n                        id\n                      }\n                      country {\n                        code\n                        id\n                      }\n                    }\n                  }\n                  duration\n                  type\n                  code\n                  carrier {\n                    id\n                    name\n                    code\n                  }\n                  operatingCarrier {\n                    id\n                    name\n                    code\n                  }\n                  cabinClass\n                  hiddenDestination {\n                    city {\n                      name\n                      id\n                    }\n                    id\n                  }\n                  throwawayDestination {\n                    id\n                  }\n                }\n                layover {\n                  duration\n                  isBaggageRecheck\n                  isWalkingDistance\n                  transferDuration\n                  id\n                }\n              }\n              duration\n            }\n            stopover {\n              nightsCount\n              arrival {\n                type\n                city {\n                  name\n                  id\n                }\n                id\n              }\n              departure {\n                type\n                id\n              }\n              duration\n            }\n            lastAvailable {\n              seatsLeft\n            }\n            extendedFareOptionsPricing {\n              standardFarePrice {\n                amount\n              }\n              flexiFarePrice {\n                amount\n              }\n            }\n          }\n          id\n        }\n        kayakEligibilityTest {\n          containsKayakWithNewRules\n          containsKayakWithCurrentRules\n        }\n      }\n      itineraries {\n        __typename\n        ... on ItineraryReturn {\n          ... on Itinerary {\n            __isItinerary: __typename\n            __typename\n            id\n            shareId\n            price {\n              amount\n              priceBeforeDiscount\n            }\n            priceEur {\n              amount\n            }\n            provider {\n              name\n              code\n              hasHighProbabilityOfPriceChange\n              contentProvider {\n                code\n              }\n              id\n            }\n            bagsInfo {\n              includedCheckedBags\n              includedHandBags\n              hasNoBaggageSupported\n              hasNoCheckedBaggage\n              checkedBagTiers {\n                tierPrice {\n                  amount\n                }\n                bags {\n                  weight {\n                    value\n                  }\n                }\n              }\n              handBagTiers {\n                tierPrice {\n                  amount\n                }\n                bags {\n                  weight {\n                    value\n                  }\n                }\n              }\n              includedPersonalItem\n              personalItemTiers {\n                tierPrice {\n                  amount\n                }\n                bags {\n                  weight {\n                    value\n                  }\n                  height {\n                    value\n                  }\n                  width {\n                    value\n                  }\n                  length {\n                    value\n                  }\n                }\n              }\n            }\n            bookingOptions {\n              edges {\n                node {\n                  token\n                  bookingUrl\n                  trackingPixel\n                  itineraryProvider {\n                    code\n                    name\n                    subprovider\n                    hasHighProbabilityOfPriceChange\n                    contentProvider {\n                      code\n                    }\n                    id\n                  }\n                  price {\n                    amount\n                  }\n                }\n              }\n            }\n            travelHack {\n              isTrueHiddenCity\n              isVirtualInterlining\n              isThrowawayTicket\n            }\n          }\n          legacyId\n          outbound {\n            id\n            sectorSegments {\n              guarantee\n              segment {\n                id\n                source {\n                  localTime\n                  utcTime\n                  station {\n                    id\n                    legacyId\n                    name\n                    code\n                    type\n                    gps {\n                      lat\n                      lng\n                    }\n                    city {\n                      legacyId\n                      name\n                      id\n                    }\n                    country {\n                      code\n                      id\n                    }\n                  }\n                }\n                destination {\n                  localTime\n                  utcTime\n                  station {\n                    id\n                    legacyId\n                    name\n                    code\n                    type\n                    gps {\n                      lat\n                      lng\n                    }\n                    city {\n                      legacyId\n                      name\n                      id\n                    }\n                    country {\n                      code\n                      id\n                    }\n                  }\n                }\n                duration\n                type\n                code\n                carrier {\n                  id\n                  name\n                  code\n                }\n                operatingCarrier {\n                  id\n                  name\n                  code\n                }\n                cabinClass\n                hiddenDestination {\n                  city {\n                    name\n                    id\n                  }\n                  id\n                }\n                throwawayDestination {\n                  id\n                }\n              }\n              layover {\n                duration\n                isBaggageRecheck\n                isWalkingDistance\n                transferDuration\n                id\n              }\n            }\n            duration\n          }\n          inbound {\n            id\n            sectorSegments {\n              guarantee\n              segment {\n                id\n                source {\n                  localTime\n                  utcTime\n                  station {\n                    id\n                    legacyId\n                    name\n                    code\n                    type\n                    gps {\n                      lat\n                      lng\n                    }\n                    city {\n                      legacyId\n                      name\n                      id\n                    }\n                    country {\n                      code\n                      id\n                    }\n                  }\n                }\n                destination {\n                  localTime\n                  utcTime\n                  station {\n                    id\n                    legacyId\n                    name\n                    code\n                    type\n                    gps {\n                      lat\n                      lng\n                    }\n                    city {\n                      legacyId\n                      name\n                      id\n                    }\n                    country {\n                      code\n                      id\n                    }\n                  }\n                }\n                duration\n                type\n                code\n                carrier {\n                  id\n                  name\n                  code\n                }\n                operatingCarrier {\n                  id\n                  name\n                  code\n                }\n                cabinClass\n                hiddenDestination {\n                  city {\n                    name\n                    id\n                  }\n                  id\n                }\n                throwawayDestination {\n                  id\n                }\n              }\n              layover {\n                duration\n                isBaggageRecheck\n                isWalkingDistance\n                transferDuration\n                id\n              }\n            }\n            duration\n          }\n          stopover {\n            nightsCount\n            arrival {\n              type\n              city {\n                name\n                id\n              }\n              id\n            }\n            departure {\n              type\n              id\n            }\n            duration\n          }\n          lastAvailable {\n            seatsLeft\n          }\n          extendedFareOptionsPricing {\n            standardFarePrice {\n              amount\n            }\n            flexiFarePrice {\n              amount\n            }\n          }\n        }\n        id\n      }\n    }\n  }\n}\n\nfragment AirlinesFilter_data on ItinerariesMetadata {\n  carriers {\n    id\n    code\n    name\n  }\n}\n\nfragment CountriesFilter_data on ItinerariesMetadata {\n  stopoverCountries {\n    code\n    name\n    id\n  }\n}\n\nfragment MobileSortingLink_data on ItinerariesMetadata {\n  topResults {\n    best {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    cheapest {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    fastest {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    sourceTakeoffAsc {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    destinationLandingAsc {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n  }\n}\n\nfragment MobileSorting_data on ItinerariesMetadata {\n  topResults {\n    best {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    cheapest {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    fastest {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    sourceTakeoffAsc {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    destinationLandingAsc {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n  }\n}\n\nfragment PriceAlert_data on ItinerariesMetadata {\n  priceAlertExists\n  existingPriceAlert {\n    id\n  }\n  searchFingerprint\n  hasMorePending\n  priceAlertsTopResults {\n    best {\n      price {\n        amount\n      }\n    }\n    cheapest {\n      price {\n        amount\n      }\n    }\n    fastest {\n      price {\n        amount\n      }\n    }\n    sourceTakeoffAsc {\n      price {\n        amount\n      }\n    }\n    destinationLandingAsc {\n      price {\n        amount\n      }\n    }\n  }\n}\n\nfragment Sorting_data on ItinerariesMetadata {\n  topResults {\n    best {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    cheapest {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    fastest {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    sourceTakeoffAsc {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n    destinationLandingAsc {\n      __typename\n      duration\n      price {\n        amount\n      }\n      id\n    }\n  }\n}\n\nfragment TravelTip_data on ItinerariesMetadata {\n  travelTips {\n    __typename\n    ... on TravelTipRadiusMoney {\n      radius\n      params {\n        name\n        value\n      }\n      savingMoney: saving {\n        amount\n        currency {\n          id\n          code\n          name\n        }\n        formattedValue\n      }\n      location {\n        __typename\n        id\n        legacyId\n        name\n        slug\n      }\n    }\n    ... on TravelTipRadiusTime {\n      radius\n      params {\n        name\n        value\n      }\n      saving\n      location {\n        __typename\n        id\n        legacyId\n        name\n        slug\n      }\n    }\n    ... on TravelTipRadiusSome {\n      radius\n      params {\n        name\n        value\n      }\n      location {\n        __typename\n        id\n        legacyId\n        name\n        slug\n      }\n    }\n    ... on TravelTipDateMoney {\n      dates {\n        start\n        end\n      }\n      params {\n        name\n        value\n      }\n      savingMoney: saving {\n        amount\n        currency {\n          id\n          code\n          name\n        }\n        formattedValue\n      }\n    }\n    ... on TravelTipDateTime {\n      dates {\n        start\n        end\n      }\n      params {\n        name\n        value\n      }\n      saving\n    }\n    ... on TravelTipDateSome {\n      dates {\n        start\n        end\n      }\n      params {\n        name\n        value\n      }\n    }\n    ... on TravelTipExtend {\n      destination {\n        __typename\n        id\n        name\n        slug\n      }\n      locations {\n        __typename\n        id\n        name\n        slug\n      }\n      price {\n        amount\n        currency {\n          id\n          code\n          name\n        }\n        formattedValue\n      }\n    }\n  }\n}\n\nfragment WeekDaysFilter_data on ItinerariesMetadata {\n  inboundDays\n  outboundDays\n}\n",
                "variables": {
                    "search": {
                        "itinerary": {
                            "source": {
                                "ids": [
                                    "City:beirut_lb"
                                ]
                            },
                            "destination": {
                                "ids": [
                                    "Station:airport:CDG"
                                ]
                            },
                            "outboundDepartureDate": {
                                "start": formatDate(d) + "T00:00:00",
                                "end": formatDate(d) + "T23:59:59"
                            },
                            "inboundDepartureDate": {
                                "start": formatDate(returnDate) + "T00:00:00",
                                "end": formatDate(returnDate) + "T23:59:59"
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
                            "applyMixedClasses": true
                        }
                    },
                    "filter": {
                        "allowReturnFromDifferentCity": true,
                        "allowChangeInboundDestination": true,
                        "allowChangeInboundSource": true,
                        "allowDifferentStationConnection": true,
                        "enableSelfTransfer": true,
                        "enableThrowAwayTicketing": true,
                        "enableTrueHiddenCity": true,
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
                    "options": {
                        "sortBy": "QUALITY",
                        "mergePriceDiffRule": "INCREASED",
                        "currency": "usd",
                        "apiUrl": null,
                        "locale": "en",
                        "partner": "skypicker",
                        "partnerMarket": "en",
                        "affilID": "acquisition000performance000sem000google",
                        "storeSearch": false,
                        "searchStrategy": "REDUCED",
                        "abTestInput": {
                            "kayakABCTest": "REMOVE_KAYAK_COMPLETELY",
                            "applyRecommendedDestinationsSorting": false
                        },
                        "serverToken": null
                    }
                }
            });
    
            // Send POST request
            await fetch('https://api.skypicker.com/umbrella/v2/graphql?featureName=SearchReturnItinerariesQuery', {
            method: 'POST',
            headers: {
                'Accept':'*/*',
                'Accept-Encoding':'gzip, deflate, br',
                'Accept-Language':'en-US,en;q=0.9',
                'Content-Type':'application/json',
                'Kw-Skypicker-Visitor-Uniqid':'b2bc59fe-9ac4-431a-9331-42c5f20ffc49',
                'Kw-Umbrella-Token':'d6d4f47ccdad80c2faa8c8edca2b8196d6845c5303151ea493e5405cdb97b284',
                'Origin':'https://www.kiwi.com',
                'Referer':'https://www.kiwi.com/',
                'Sec-Ch-Ua':'"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
                'Sec-Ch-Ua-Mobile':'?0',
                'Sec-Ch-Ua-Platform':'"Windows"',
                'Sec-Fetch-Dest':'empty',
                'Sec-Fetch-Mode':'cors',
                'Sec-Fetch-Site':'cross-site',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
            },
            body: JSON.stringify(requestData)
            })
            .then(response => response.json())
            .then(data => {
                var originalItineraries = data.data.returnItineraries.itineraries;
                simplifiedItineraries = [];
            
                originalItineraries.forEach(itinerary => {
                    var simplified = {
                        priceAmount: itinerary.price.amount,
                        includedCheckedBags: itinerary.bagsInfo.includedCheckedBags,
                        includedHandBags: itinerary.bagsInfo.includedHandBags,
                        outboundDepartureTime: itinerary.outbound.sectorSegments[0].segment.source.localTime,
                        outboundArrivalTime: itinerary.outbound.sectorSegments[0].segment.destination.localTime,
                        outboundDuration: itinerary.outbound.sectorSegments[0].duration,
                        inboundDepartureTime: itinerary.inbound.sectorSegments[0].segment.source.localTime,
                        inboundArrivalTime: itinerary.inbound.sectorSegments[0].segment.destination.localTime,
                        inboundDuration: itinerary.inbound.sectorSegments[0].duration,
                        carrierOutboundName: itinerary.outbound.sectorSegments[0].carrier.name,
                        carrierInboundName: itinerary.inbound.sectorSegments[0].carrier.name,
                        seatsLeft: itinerary.lastAvailable.seatsLeft,
                        standardFarePrice: itinerary.extendedFareOptionsPricing.standardFarePrice.amount,
                        flexiFarePrice: itinerary.extendedFareOptionsPricing.flexiFarePrice.amount
                    };
            
                    simplifiedItineraries.push(simplified);
                });
            })
            .catch(error => {
                error = true;
                console.error('Error:', error);
            });
    
            // Wait for 5 seconds before sending the next request
            await new Promise(resolve => setTimeout(resolve, 5000));
        }
        if(!error) downloadExcel(simplifiedItineraries);

    });
  
    function downloadExcel(simplifiedItineraries) {
        // Sort by priceAmount in ascending order
        simplifiedItineraries.sort((a, b) => parseFloat(a.priceAmount) - parseFloat(b.priceAmount));
        
        // Create workbook and worksheet
        const wb = XLSX.utils.book_new();
        const ws = XLSX.utils.json_to_sheet(simplifiedItineraries);
        
        // Add worksheet to workbook
        XLSX.utils.book_append_sheet(wb, ws, 'Itineraries');
        
        // Generate Excel file and trigger download
        const wbout = XLSX.write(wb, {bookType: 'xlsx', type: 'binary'});
        const blob = new Blob([s2ab(wbout)], {type: 'application/octet-stream'});
        saveAs(blob, 'Itineraries.xlsx');
    }
        
    // Helper function to convert string to ArrayBuffer
    function s2ab(s) {
        const buf = new ArrayBuffer(s.length);
        const view = new Uint8Array(buf);
        for (let i = 0; i < s.length; i++) view[i] = s.charCodeAt(i) & 0xFF;
        return buf;
    }

});

function formatDate(date) {
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0'); // Months are 0-indexed, add 1 and pad with zeros
    const day = date.getDate().toString().padStart(2, '0'); // Pad with zeros

    return `${year}-${month}-${day}`;
}


      
  