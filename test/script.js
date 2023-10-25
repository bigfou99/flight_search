// Extract the itineraries and sort them by price in ascending order
const itineraries = jsonData.data.onewayItineraries.itineraries;
itineraries.sort((a, b) => parseFloat(a.price.amount) - parseFloat(b.price.amount));

// Get the container to display the sorted itineraries
const itineraryListDiv = document.getElementById("itineraryList");

// Iterate through sorted itineraries and display them
itineraries.forEach((itinerary) => {
  const price = itinerary.price.amount;
  const includedCheckedBags = itinerary.bagsInfo.includedCheckedBags;
  const includedHandBags = itinerary.bagsInfo.includedHandBags;
  const durationHours = (itinerary.sector.duration / 3600).toFixed(2);
  const seatsLeft = itinerary.lastAvailable.seatsLeft;
  const flightTime = itinerary.sector.sectorSegments[0].segment.source.localTime;
  const flightName = itinerary.sector.sectorSegments[0].segment.carrier.name;

  const itineraryInfo = document.createElement("p");
  itineraryInfo.textContent = `Price: ${price}, Included Checked Bags: ${includedCheckedBags}, Included Hand Bags: ${includedHandBags}, Duration: ${durationHours} hours, Seats Left: ${seatsLeft}, Flight Time: ${flightTime}, Flight Name: ${flightName}`;
  
  itineraryListDiv.appendChild(itineraryInfo);
});
